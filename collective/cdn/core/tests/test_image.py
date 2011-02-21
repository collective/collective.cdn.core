import unittest

import os
from Globals import InitializeClass, package_home

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc

from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

from Products.PloneTestCase.PloneTestCase import FunctionalTestCase
from Products.Five.testbrowser import Browser

from Products.CMFCore.utils import getToolByName

import collective.cdn.core
import collective.cdn.core.tests

PACKAGE_HOME = package_home(globals())

@onsetup
def setup_product():
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml',
                     collective.cdn.core)
    zcml.load_config('testing.zcml',
                     collective.cdn.core.tests)
    fiveconfigure.debug_mode = False
    ztc.installPackage('collective.cdn.core')

setup_product()
ptc.setupPloneSite(products=['collective.cdn.core',])

class TestImageCDN(ptc.PloneTestCase):
    
    def createImage(self):
        path = os.path.join(PACKAGE_HOME, 'test.gif')
        fd = open(path, 'rb')
        data = fd.read()
        fd.close()
        self.portal.invokeFactory(type_name='Image',id='test.gif')
        image = self.portal['test.gif']
        image.setImage(data,mimetype='image/gif', filename='test.gif')
        return image
    
    def enableCDN(self):
        self.cdn_properties.enable_cdn_image = True
        self.cdn_properties.cdn_provider = 'FakeProvider'

    def disableCDN(self):
        self.cdn_properties.enable_cdn_image = False
        self.cdn_properties.cdn_provider = ''
    
    def afterSetUp(self):
        super(TestImageCDN, self).afterSetUp()
                
        self.browser = Browser()
        
        self.setRoles(['Manager', 'Member'])
        
        self.ptool = getToolByName(self.portal, 'portal_properties')
        self.cdn_properties = self.ptool.cdn_properties
        self.image = self.createImage()
        
    def test_original_behaviour(self):
        self.disableCDN()
        tag = '<img src="http://nohost/plone/test.gif/image" alt="" title="" height="15" width="300" />'
        self.failUnlessEqual(self.image.tag(),tag)
        
    def test_cdn_behaviour(self):
        self.enableCDN()
        tag = '<img src="http://example.net/plone/test.gif/image" alt="" title="" height="15" width="300" />'
        self.failUnlessEqual(self.image.tag(),tag)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestImageCDN))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
