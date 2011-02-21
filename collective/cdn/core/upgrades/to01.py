# -*- coding: utf-8 -*-
from zope import component
import logging
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup import interfaces as gsinterfaces
from Products.GenericSetup.upgrade import listUpgradeSteps

from Products.ZCatalog.ProgressHandler import ZLogHandler

def upgrade0to1(context):
    ''' Upgrade to version 1.0
    '''
    setup = getToolByName(context, 'portal_setup')
    catalog = getToolByName(context,'portal_catalog')
    portal_properties = getToolByName(context,'portal_properties')
    
    # Do Stuff
    