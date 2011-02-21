# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.PythonScripts.standard import url_quote
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.ResourceRegistries.browser.scripts import ScriptsView as BaseView
from collective.cdn.core.browser.base import BaseRegistryView

class ScriptsView(BaseRegistryView, BaseView):
    """ Information for script rendering. """

    registry_id = 'portal_javascripts'
    cdn_enable_prop = 'enable_cdn_js'

    def scripts(self):
        registry = self.registry()
        registry_url = registry.absolute_url()
        
        scripts = super(ScriptsView,self).scripts()
        result = []
        if not self.use_cdn:
            return scripts
        for scripts in scripts:
            if scripts.has_key('src'):
                src = scripts['src']
                if src.startswith(registry_url):
                    path = src[len(registry_url):]
                    base_url = self.process_url(registry_url,path)
                    scripts['src'] = "%s/%s" % (base_url, path)
            result.append(scripts)
        return result