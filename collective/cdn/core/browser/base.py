# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.PythonScripts.standard import url_quote
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from plone.memoize import ram
from plone.memoize import view
from collective.cdn.core.interfaces import ICDNProvider
from collective.cdn.core.utils import cdn_config, getProvider


class BaseRegistryView(BrowserView):
    """ Information for resource rendering. """

    registry_id = ''
    cdn_enable_prop = ''
    @view.memoize
    def registry(self):
        return getToolByName(aq_inner(self.context), self.registry_id)
    
    @view.memoize
    def skinname(self):
        return aq_inner(self.context).getCurrentSkinName()
    
    @view.memoize
    def cdn_sheet(self):
        return cdn_config()
    
    @property
    def use_cdn(self):
        cdn_sheet = self.cdn_sheet()
        enabled = False
        if cdn_sheet:
            enabled = cdn_sheet.getProperty(self.cdn_enable_prop,False)
        return enabled
    
    @view.memoize        
    def cdn_provider(self):
        provider = getProvider()
        return provider
    
    def process_url(self,base_url,path=''):
        provider = self.cdn_provider()
        if not provider:
            return base_url
        return provider.process_url(base_url, path)
    