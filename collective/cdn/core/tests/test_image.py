# -*- coding: utf-8 -*-
import os
import unittest2 as unittest

from Globals import package_home

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from Products.CMFCore.utils import getToolByName

from collective.cdn.core.testing import INTEGRATION_TESTING

PACKAGE_HOME = package_home(globals())


class TestImageCDN(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def createImage(self):
        path = os.path.join(PACKAGE_HOME, 'test.gif')
        fd = open(path, 'rb')
        data = fd.read()
        fd.close()
        self.portal.invokeFactory(type_name='Image', id='test.gif')
        image = self.portal['test.gif']
        image.setImage(data, mimetype='image/gif', filename='test.gif')
        return image

    def enableCDN(self):
        self.cdn_properties.enable_cdn_image = True
        self.cdn_properties.cdn_provider = 'FakeProvider'

    def disableCDN(self):
        self.cdn_properties.enable_cdn_image = False
        self.cdn_properties.cdn_provider = ''

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Member'])

        self.ptool = getToolByName(self.portal, 'portal_properties')
        self.cdn_properties = self.ptool.cdn_properties
        self.image = self.createImage()

    def test_original_behaviour(self):
        self.disableCDN()
        tag = '<img src="http://nohost/plone/test.gif/image" alt="" title="" height="15" width="300" />'
        self.assertEquals(self.image.tag(), tag)

    def test_cdn_behaviour(self):
        self.enableCDN()
        tag = '<img src="http://example.net/plone/test.gif/image" alt="" title="" height="15" width="300" />'
        self.assertEquals(self.image.tag(), tag)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
