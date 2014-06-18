===========================
collective.contact.membrane
===========================

Integration of dexterity membrane with contacts from collective.contact.core.

Contacts are Plone users
========================

When you install this package, contacts (Person contents) become Plone users.
Once they have a password, they can login,
using the contact id or the contact email (set the parameter in the control panel)

Contact fields are properties of user.
When you change some properties on user settings (for instance: email, location)
contact entry is updated.

Organizations are Plone Groups
==============================

Organizations and positions becomes Plone Groups.
If a person has an held position into the organization or the position,
he/she is a member of this group.
