# -*- coding=utf-8 -*-
from zope.interface import Interface

class ICDNProvider(Interface):
    '''A CDN Provider
    '''
    
    def process_url(url, relative_path=''):
        ''' process a url
        '''