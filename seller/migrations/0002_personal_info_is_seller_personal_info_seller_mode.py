# Generated by Django 4.1.1 on 2022-09-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_info',
            name='is_seller',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='seller_mode',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]