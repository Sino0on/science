from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Material)
class MaterialTranslationOptions(TranslationOptions):
    fields = ('description', 'title')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('description', 'title')


@register(Profession)
class ProfessionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Science)
class ScienceTranslationOptions(TranslationOptions):
    fields = ('title',)
