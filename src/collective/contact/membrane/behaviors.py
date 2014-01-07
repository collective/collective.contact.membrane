from five import grok

from dexterity.membrane.behavior.membraneuser import IMembraneUser, MembraneUser, IMembraneUserObject, IMembraneUserWorkflow


class IPersonMembraneUser(IMembraneUser):
    """Marker/Form interface for Person Membrane User
    """


class PersonMembraneUser(MembraneUser):
    """Person Membrane User
    """
    allowed_states = ('active')
    _default = {'use_email_as_username': True,
                'use_uuid_as_userid': True}


class PersonMembraneUserAdapter(grok.Adapter, PersonMembraneUser):
    grok.context(IPersonMembraneUser)
    grok.implements(IMembraneUserObject)


class PersonMembraneUserWorkflow(grok.Adapter, PersonMembraneUser):
    grok.context(IPersonMembraneUser)
    grok.implements(IMembraneUserWorkflow)
