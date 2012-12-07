from zope.schema.interfaces import IVocabularyFactory
from zope import interface
from zope import component
from collective.socialicons.icons import ICONS
from plone.registry.interfaces import IRegistry
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from plone.i18n.normalizer.base import baseNormalize


class RegistryVocabulary(object):
    """vocabulary to use with plone.app.registry"""
    interface.implements(IVocabularyFactory)

    def __init__(self, key):
        self.key = key

    def __call__(self, context):
        icons = []
        if self.key in ICONS:
            icons = ICONS[self.key]
        registry = component.queryUtility(IRegistry)
        if registry is None:
            return icons
        icons += registry.get('collective.socialicons.%s' % self.key, [])
        terms = [SimpleTerm(baseNormalize(icon),
                            baseNormalize(icon),
                            icon) for icon in icons]
        return SimpleVocabulary(terms)


FacebookIcons = RegistryVocabulary('facebook')
TwitterIcons = RegistryVocabulary('twitter')
GooglePlusIcons = RegistryVocabulary('googleplus')
YoutubeIcons = RegistryVocabulary('youtube')
LinkedinIcons = RegistryVocabulary('linkedin')
RSSIcons = RegistryVocabulary('rss')
