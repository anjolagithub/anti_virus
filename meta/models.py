from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Service_Type(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Overview(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    Meta_Title = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE,blank=True, null=True)
    service_type = models.ForeignKey(Service_Type, on_delete=models.CASCADE,blank=True, null=True)
    search_keyword = models.CharField(max_length=700, blank=True, null=True)
    is_project = models.BooleanField(default=False)
    is_request = models.BooleanField(default=False)
    file_update = models.DateTimeField(null=True, blank=True)

class Pricing(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    Price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    sell_price = models.FloatField(blank=True, null=True)

    def save(self, *arg, **kwarg) -> None:
        price = self.Price

        if self.discount:
            price = self.Price * (self.discount/100)
        
        self.sell_price = price

        return super().save(*arg, **kwarg)

class FAQ(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=70, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class Description_FAQ(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.profile

class Requirement(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    requirement = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.profile

class Gallery(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    Picture = models.ImageField(upload_to='project_images/', null=True, blank=True)

    def __str__(self) -> str:
        return self.profile

class Project(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='meta_video/', null=True, blank=True)
    project = models.FileField(upload_to='project/', null=True, blank=True)

    def __str__(self) -> str:
        return self.profile

class Publish(models.Model):
    profile = models.ForeignKey(Overview,on_delete=models.CASCADE, blank=True, null=True)
    progress = models.FloatField(blank=True, null=True)
    can_publish = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)
    publish_date = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.profile

