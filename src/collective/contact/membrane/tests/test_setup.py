# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.contact.membrane.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of collective.contact.membrane into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.contact.membrane is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.contact.membrane'))

    def test_uninstall(self):
        """Test if collective.contact.membrane is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.contact.membrane'])
        self.assertFalse(self.installer.isProductInstalled('collective.contact.membrane'))
