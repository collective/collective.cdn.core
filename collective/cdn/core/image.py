# -*- coding:utf-8 -*-
from cgi import escape
from zope.app.component.hooks import getSite
from Products.Archetypes.Field import ImageField
from collective.cdn.core.utils import image_cdn_enabled, getProvider
        
def base_url(self,instance):
    url = instance.absolute_url()
    if not image_cdn_enabled():
        return url
    site_url = getSite().absolute_url()
    base_url = site_url
    path = url[len(site_url)+1:]
    provider = getProvider()
    return '%s/%s' % (provider.process_url(base_url,path),path)
    
def tag(self, instance, scale=None, height=None, width=None, alt=None,
        css_class=None, title=None, **kwargs):
    """Create a tag including scale
    """
    image = self.getScale(instance, scale=scale)
    if image:
        img_width, img_height = self.getSize(instance, scale=scale)
    else:
        img_height=0
        img_width=0

    if height is None:
        height=img_height
    if width is None:
        width=img_width

    url = self.base_url(instance)
    if scale:
        url+= '/' + self.getScaleName(scale)
    else:
        url+= '/' + self.getName()

    if alt is None:
        alt = instance.Title()
    if title is None:
        title = instance.Title()

    values = {'src' : url,
              'alt' : escape(alt, quote=True),
              'title' : escape(title, quote=True),
              'height' : height,
              'width' : width,
             }

    result = '<img src="%(src)s" alt="%(alt)s" title="%(title)s" '\
             'height="%(height)s" width="%(width)s"' % values

    if css_class is not None:
        result = '%s class="%s"' % (result, css_class)

    for key, value in kwargs.items():
        if value:
            result = '%s %s="%s"' % (result, key, value)

    return '%s />' % result

def patch():
    ''' Patch ImageField with our tag method
    '''
    ImageField.original_tag = ImageField.tag
    ImageField.base_url = base_url
    ImageField.tag = tag