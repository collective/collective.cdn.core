# -*- coding: utf-8 -*-
from zope.interface import Interface

class ICDNLayer(Interface):
    """ Marker interface that defines a Zope 3 browser layer
    """

class IScriptsView(Interface):

    def scripts():
        """ Returns a list of dicts with information for scripts rendering. """


class IStylesView(Interface):

    def styles():
        """ Returns a list of dicts with information for style rendering. """

class IKSSView(Interface):

    def kineticstylesheets():
        """ Returns a list of dicts with information for kss rendering. """