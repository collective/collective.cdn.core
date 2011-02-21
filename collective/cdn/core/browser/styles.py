# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.PythonScripts.standard import url_quote
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.ResourceRegistries.browser.styles import StylesView as BaseView
from collective.cdn.core.browser.base import BaseRegistryView

class StylesView(BaseRegistryView,BaseView):
    """ Information for style rendering. """
    
    registry_id = 'portal_css'
    cdn_enable_prop = 'enable_cdn_css'
    
    def styles(self):
        registry = self.registry()
        registry_url = registry.absolute_url()

        styles = super(StylesView,self).styles()
        result = []
        if not self.use_cdn:
            return styles
        for style in styles:
            if style.has_key('src'):
                src = style['src']
                if src.startswith(registry_url):
                    path = src[len(registry_url):]
                    base_url = self.process_url(registry_url,path)
                    style['src'] = "%s/%s" % (base_url, path)
            result.append(style)
        return result