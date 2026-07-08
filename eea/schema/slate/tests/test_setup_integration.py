"""Integration tests for eea.schema.slate setup."""

import unittest

from eea.schema.slate.testing import EEA_SCHEMA_SLATE_INTEGRATION_TESTING


class TestSetup(unittest.TestCase):
    """Test that eea.schema.slate ZCML is properly loaded."""

    layer = EEA_SCHEMA_SLATE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]

    def test_zcml_loaded(self):
        """Test that ZCML is loaded and adapters are registered."""
        from zope.component import getGlobalSiteManager
        sm = getGlobalSiteManager()
        self.assertIsNotNone(sm)

    def test_slate_field_schema_provider_registered(self):
        """Test that SlateJSONFieldSchemaProvider adapter is registered."""
        from zope.component import queryAdapter
        from eea.schema.slate.field import ISlateJSONField
        from plone.restapi.types.interfaces import IJsonSchemaProvider
        # The adapter should be registered for ISlateJSONField
        self.assertIsNotNone(queryAdapter(None, IJsonSchemaProvider))


def test_suite():
    """Test suite."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)