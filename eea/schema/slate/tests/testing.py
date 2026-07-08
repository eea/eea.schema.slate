"""Test layer for eea.schema.slate."""

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import eea.schema.slate


class EeaSchemaSlateLayer(PloneSandboxLayer):
    """Test layer for eea.schema.slate."""

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=eea.schema.slate)


EEA_SCHEMA_SLATE_FIXTURE = EeaSchemaSlateLayer()

EEA_SCHEMA_SLATE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EEA_SCHEMA_SLATE_FIXTURE,),
    name="EeaSchemaSlateLayer:IntegrationTesting",
)