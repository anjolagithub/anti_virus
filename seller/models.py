from django.db import models
from django.contrib.auth.models import User

class Personal_Info(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    full_Name = models.CharField(max_length=170, blank=True, null=True)
    profile_Picture = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    is_seller = models.BooleanField(default=False, null=True, blank=True)
    seller_mode = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self) -> str:
        return self.profile.username

class Language_Levels(models.Model):
    language = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.language

class Languages(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    language = models.CharField(max_length=70, null=True, blank=True)
    Language_Levels = models.ForeignKey(Language_Levels, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.language

class Occupation_list(models.Model):
    occupations = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.occupations

class Occupation(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    occupation = models.ForeignKey(Occupation_list, on_delete=models.CASCADE)
    from_year = models.IntegerField(null=True, blank=True)
    to_year = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.occupation

class Skill_list(models.Model):
    skiller = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.skiller

class Skill(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    skills = models.ForeignKey(Skill_list, on_delete=models.CASCADE)
    level = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.skills

class Education(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=700, null=True, blank=True)
    name = models.CharField(max_length=700, null=True, blank=True)
    title = models.CharField(max_length=700, null=True, blank=True)
    major = models.CharField(max_length=700, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.major

class Certification(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    Certificate = models.CharField(max_length=700, null=True, blank=True)
    certified = models.CharField(max_length=700, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.Certificate

class Professional_Info(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    personal_Website = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.profile.username

class Linked_Accounts(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    Google = models.URLField(blank=True, null=True)
    Facebook = models.URLField(blank=True, null=True)
    Twitter = models.URLField(blank=True, null=True)
    Github = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.profile.username

class Account_Security(models.Model):
    profile = models.ForeignKey(Personal_Info, on_delete=models.CASCADE, blank=True, null=True)
    phone_Number = models.IntegerField(blank=True, null=True)
    is_verified = models.BooleanField(blank=True, null=True, default=False)
    code = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.profile.username
