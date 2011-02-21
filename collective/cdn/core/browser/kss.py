# -*- coding: utf-8 -*-
from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.PythonScripts.standard import url_quote
from Products.ResourceRegistries.browser.kss import KSSView as BaseView
from collective.cdn.core.browser.base import BaseRegistryView


class KSSView(BaseRegistryView, BaseView):
    """ Information for kss rendering. """

    registry_id = 'portal_kss'
    cdn_enable_prop = 'enable_cdn_kss'

    def kineticstylesheets(self):
        registry = self.registry()
        registry_url = registry.absolute_url()

        kineticstylesheets = super(KSSView,self).kineticstylesheets()
        result = []
        if not self.use_cdn:
            return kineticstylesheets
        for kss in kineticstylesheets:
            if kss.has_key('src'):
                src = kss['src']
                if src.startswith(registry_url):
                    path = src[len(registry_url):]
                    base_url = self.process_url(registry_url,path)
                    kss['src'] = "%s/%s" % (base_url, path)
            result.append(kss)
        return result