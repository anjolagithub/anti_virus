from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

class Pricing_classAdmin(admin.StackedInline):
    model = Pricing

class Description_FAQ_classAdmin(admin.StackedInline):
    model = Description_FAQ

class FAQ_classAdmin(admin.StackedInline):
    model = FAQ

class Requirement_classAdmin(admin.StackedInline):
    model = Requirement

class Gallery_classAdmin(admin.StackedInline):
    model = Gallery

class Project_classAdmin(admin.StackedInline):
    model = Project

class Publish_classAdmin(admin.StackedInline):
    model = Publish


class OverviewAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'Meta_Title', 'category', 'sub_category', 'service_type', 'search_keyword'
            ),
        }),
    )
    inlines = [Pricing_classAdmin, Description_FAQ_classAdmin, FAQ_classAdmin, Requirement_classAdmin, Gallery_classAdmin, Project_classAdmin, Publish_classAdmin]

admin.site.register(Overview, OverviewAdmin)

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Service_Type)
