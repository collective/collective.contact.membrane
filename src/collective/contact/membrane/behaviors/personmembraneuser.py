from five import grok

from dexterity.membrane.behavior.membraneuser import (IMembraneUser,
                                                      MembraneUser,
                                                      IMembraneUserObject,
                                                      IMembraneUserWorkflow,
                                                      MyUserProperties)
from Products.membrane.interfaces import IGroup
from Products.membrane.interfaces.user import IMembraneUserGroups,\
    IMembraneUserProperties
from Products.PlonePAS.sheet import MutablePropertySheet
from collective.contact.core.interfaces import IContactable,\
    IPersonHeldPositions
from collective.contact.core.behaviors import IContactDetails


class IPersonMembraneUser(IMembraneUser):
    """Marker/Form interface for Person Membrane User
    """


class PersonMembraneUser(MembraneUser):
    """Person Membrane User
    """
    allowed_states = ('active',)
    _default = {'use_email_as_username': True,
                'use_uuid_as_userid': True}

    def get_full_name(self):
        return self.context.get_full_name()

    def getUserName(self):
        if self._use_email_as_username():
            return self.context.email
        return self.context.getId()


class PersonMembraneUserAdapter(grok.Adapter, PersonMembraneUser):
    grok.context(IPersonMembraneUser)
    grok.implements(IMembraneUserObject)


class PersonMembraneUserWorkflow(grok.Adapter, PersonMembraneUser):
    grok.context(IPersonMembraneUser)
    grok.implements(IMembraneUserWorkflow)


class PersonMembraneUserProperties(MyUserProperties, PersonMembraneUser):
    grok.context(IPersonMembraneUser)
    grok.implements(IMembraneUserProperties)

    property_map = dict(
        email='email',
        home_page='website',
        location='city',
        )

    @property
    def fullname(self):
        return self.context.get_full_name()

    def getPropertiesForUser(self, user, request=None):
        """Get properties for this user.
        Get property from the contactable,
        which fall backs to organization, position, held_position, etc
        """
        properties = dict(
            fullname=self.fullname,
            )
        contactable = IContactable(self.context)
        details = contactable.get_contact_details(keys=self.property_map.values() + ['address'])
        for prop_name, field_name in self.property_map.items():
            properties[prop_name] = details.get(field_name,
                                    details['address'].get(field_name, None)
                                    ) or u""

        return MutablePropertySheet(self.context.getId(),
                                    **properties)

    def setPropertiesForUser(self, user, propertysheet):
        """
        Set the property to the person object if it implements IContactDetails
        else, try to update main held position.
        """
        if IContactDetails.providedBy(self.context):
            storage = self.context
        else:
            main_position = IPersonHeldPositions(self.context).get_main_position()
            if main_position:
                storage = main_position
            else:
                return

        properties = dict(propertysheet.propertyItems())
        for prop_name, field_name in self.property_map.items():
            value = properties.get(prop_name, '').strip()
            setattr(storage, field_name, value)


class PersonMembraneUserGroups(grok.Adapter):
    grok.context(IPersonMembraneUser)
    grok.implements(IMembraneUserGroups)

    def getGroupsForPrincipal(self, principal, request=None):
        person = self.context
        groups = {}
        for held_position in person.get_held_positions():
            group = IGroup(held_position.position.to_object)
            group_id = group.getGroupId()
            groups[group_id] = 1

        return tuple(groups.keys())
