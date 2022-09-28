from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class Languages_classAdmin(admin.StackedInline):
    model = Languages
    
class Professional_Info_classAdmin(admin.StackedInline):
    model = Professional_Info

class Occupation_classAdmin(admin.StackedInline):
    model = Occupation

class Skill_classAdmin(admin.StackedInline):
    model = Skill

class Education_classAdmin(admin.StackedInline):
    model = Education

class Certification_classAdmin(admin.StackedInline):
    model = Certification

class Linked_Accounts_classAdmin(admin.StackedInline):
    model = Linked_Accounts

class Account_Security_classAdmin(admin.StackedInline):
    model = Account_Security


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Info', {
            "fields": (
                'full_Name', 'profile_Picture', 'description'
            ),
        }),
    )
    inlines = [Languages_classAdmin, Occupation_classAdmin, Skill_classAdmin, Education_classAdmin, Certification_classAdmin, Professional_Info_classAdmin, Linked_Accounts_classAdmin, Account_Security_classAdmin]

admin.site.register(Personal_Info, ProfileAdmin)
admin.site.register(Language_Levels)
admin.site.register(Occupation_list)
admin.site.register(Skill_list)