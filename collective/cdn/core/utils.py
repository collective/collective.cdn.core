# -*- coding:utf-8 -*-
from zope.component import queryUtility
from zope.component import getUtility
from collective.cdn.core.interfaces import ICDNProvider
from Products.CMFCore.interfaces import IPropertiesTool


def cdn_config():
    ''' Return CDN Configuration '''
    ptool = queryUtility(IPropertiesTool)
    if ptool is None:
        return None
    props = getattr(ptool, 'cdn_properties', None)
    return props


def image_cdn_enabled():
    ''' Is Image CDN also available? '''
    config = cdn_config()
    return config and config.getProperty('enable_cdn_image', False)


def getProvider():
    ''' Return the activated provider '''
    config = cdn_config()
    provider_name = config.getProperty('cdn_provider', 'CoralCDN')
    p_hostname = config.getProperty('cdn_hostname', '')
    p_port = config.getProperty('cdn_port', 80)
    p_path = config.getProperty('cdn_path', '')
    provider = getUtility(ICDNProvider, provider_name)(hostname=p_hostname,
                                                       port=p_port,
                                                       path=p_path)
    return provider
