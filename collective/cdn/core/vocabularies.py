# -*- coding: utf-8 -*-
from zope.app.schema.vocabulary import IVocabularyFactory
from Products.CMFCore.utils import getToolByName
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.component import getMultiAdapter, getUtilitiesFor, getUtility
from zope.interface import implements
from collective.cdn.core.interfaces import ICDNProvider

class ProvidersVocabulary(object):
    """ Return Available Providers
    """
    implements(IVocabularyFactory)
    
    def __call__(self, context):
        ''' 
        '''
        utilities = getUtilitiesFor(ICDNProvider)
        
        vocab = [SimpleTerm(name, name) for (name,instance) in utilities if name.strip()]
        return SimpleVocabulary(vocab)

ProvidersVocabularyFactory = ProvidersVocabulary()