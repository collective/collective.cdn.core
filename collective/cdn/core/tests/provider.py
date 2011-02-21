from zope.interface import implements
from collective.cdn.core.interfaces import ICDNProvider

class cdn(object):   
    
    implements(ICDNProvider)
    
    def __init__(self,hostname=[],port=80,path=''):
        ''' Initialize
        '''
        self.hostname = ['example.net',]
        self.port = 80
        self.path = ''
    
    def process_url(self,url,relative_path=''):
        protocol,path = url.split('://')
        path = path.split('/')     
        path[0] = self.hostname[0]
        
        # add path, if supplied
        if self.path:
            path.insert(1,self.path)
        
        # join everything
        path = '/'.join(path)
        url = '%s://%s' % (protocol, path)
        return url