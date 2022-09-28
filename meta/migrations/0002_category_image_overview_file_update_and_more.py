# Generated by Django 4.1.1 on 2022-09-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
        migrations.AddField(
            model_name='overview',
            name='file_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='overview',
            name='is_project',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overview',
            name='is_request',
            field=models.BooleanField(default=False),
        ),
    ]