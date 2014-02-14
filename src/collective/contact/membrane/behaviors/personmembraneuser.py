from five import grok

from dexterity.membrane.behavior.membraneuser import (IMembraneUser,
                                                      MembraneUser,
                                                      IMembraneUserObject,
                                                      IMembraneUserWorkflow)
from Products.membrane.interfaces import IGroup
from Products.membrane.interfaces.user import IMembraneUserGroups


class IPersonMembraneUser(IMembraneUser):
    """Marker/Form interface for Person Membrane User
    """


class PersonMembraneUser(MembraneUser):
    """Person Membrane User
    """
    allowed_states = ('active')
    _default = {'use_email_as_username': True,
                'use_uuid_as_userid': True}

    def get_full_name(self):
        return self.context.get_full_name()


class PersonMembraneUserAdapter(grok.Adapter, PersonMembraneUser):
    grok.context(IPersonMembraneUser)
    grok.implements(IMembraneUserObject)


class PersonMembraneUserWorkflow(grok.Adapter, PersonMembraneUser):
    grok.context(IPersonMembraneUser)
    grok.implements(IMembraneUserWorkflow)


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
