from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class ProjectAdmin(TranslationAdmin):
    model = Project


class CityAdmin(TranslationAdmin):
    model = City


class MaterialAdmin(TranslationAdmin):
    model = Material


class CountryAdmin(TranslationAdmin):
    model = Country


class ProfessionAdmin(TranslationAdmin):
    model = Profession


class ScienceAdmin(TranslationAdmin):
    model = Science


admin.site.register(Phone)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Science, ScienceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Person)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Author)
