# -*- coding: utf-8 -*-
from zope.i18nmessageid import MessageFactory as BaseMessageFactory

from collective.cdn.core import image

MessageFactory = BaseMessageFactory('collective.cdn.core')

image.patch()
