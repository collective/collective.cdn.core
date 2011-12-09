# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.component import getUtilitiesFor

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from zope.schema.interfaces import IVocabularyFactory

from collective.cdn.core.interfaces import ICDNProvider


class ProvidersVocabulary(object):
    """ Return Available Providers
    """

    implements(IVocabularyFactory)

    def __call__(self, context):
        ''' List available providers registered for ICDNProvider
        '''
        utilities = getUtilitiesFor(ICDNProvider)

        vocab = [SimpleTerm(name, name) for (name, instance) in utilities
                                                             if name.strip()]

        return SimpleVocabulary(vocab)


ProvidersVocabularyFactory = ProvidersVocabulary()
