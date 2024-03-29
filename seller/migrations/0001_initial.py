# Generated by Django 4.1.1 on 2022-09-21 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language_Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupations', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_Name', models.CharField(blank=True, max_length=170, null=True)),
                ('profile_Picture', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skiller', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(blank=True, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.personal_info')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.skill_list')),
            ],
        ),
        migrations.CreateModel(
            name='Professional_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_Website', models.URLField(blank=True, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_year', models.IntegerField(blank=True, null=True)),
                ('to_year', models.IntegerField(blank=True, null=True)),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.occupation_list')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='Linked_Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Google', models.URLField(blank=True, null=True)),
                ('Facebook', models.URLField(blank=True, null=True)),
                ('Twitter', models.URLField(blank=True, null=True)),
                ('Github', models.URLField(blank=True, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=70, null=True)),
                ('Language_Levels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.language_levels')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=700, null=True)),
                ('name', models.CharField(blank=True, max_length=700, null=True)),
                ('title', models.CharField(blank=True, max_length=700, null=True)),
                ('major', models.CharField(blank=True, max_length=700, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Certificate', models.CharField(blank=True, max_length=700, null=True)),
                ('certified', models.CharField(blank=True, max_length=700, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='Account_Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_Number', models.IntegerField(blank=True, null=True)),
                ('is_verified', models.BooleanField(blank=True, default=False, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.personal_info')),
            ],
        ),
    ]
