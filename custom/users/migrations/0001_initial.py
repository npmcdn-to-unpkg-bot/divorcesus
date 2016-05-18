# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 03:20
from __future__ import unicode_literals

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
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('subtitle', models.CharField(blank=True, max_length=150)),
                ('body', models.CharField(blank=True, max_length=1500)),
                ('avatar', models.ImageField(upload_to='avatars')),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=250, null=True)),
                ('address2', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('postal_zip', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=140, null=True)),
                ('section_one', models.CharField(blank=True, max_length=500, null=True)),
                ('section_two', models.CharField(blank=True, max_length=500, null=True)),
                ('section_three', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Advantage',
                'verbose_name_plural': 'Advantage',
            },
        ),
        migrations.CreateModel(
            name='AdvantageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=140, null=True)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
                ('advantage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Advantage')),
            ],
            options={
                'verbose_name': 'Advantage Link',
                'verbose_name_plural': 'Advantage Links',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('time_contacted', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('message', models.CharField(blank=True, max_length=450, null=True)),
            ],
            options={
                'verbose_name': 'User Contact',
                'verbose_name_plural': 'User Contacts',
            },
        ),
        migrations.CreateModel(
            name='FacebookProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(blank=True, null=True)),
                ('facebook_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('access_token', models.TextField(blank=True, help_text='Facebook token for offline access', null=True)),
                ('facebook_name', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_profile_url', models.TextField(blank=True, null=True)),
                ('website_url', models.TextField(blank=True, null=True)),
                ('blog_url', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True)),
                ('raw_data', models.TextField(blank=True, null=True)),
                ('facebook_open_graph', models.NullBooleanField(help_text='Determines if this user want to share via open graph')),
                ('new_token_required', models.BooleanField(default=False, help_text='Set to true if the access token is outdated or lacks permissions')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/facebook_profiles/%Y/%m/%d')),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='users.Profile')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='facebook_user', to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(blank=True, max_length=140)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(blank=True, max_length=140)),
                ('last_name', models.CharField(blank=True, max_length=140)),
                ('time_created', models.DateField(blank=True, null=True, verbose_name='Time Created')),
                ('profile_picture', models.CharField(blank=True, max_length=250)),
                ('is_new', models.BooleanField(default=True)),
                ('is_cleared', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-time_created'],
                'verbose_name': 'Facebook Profile',
                'verbose_name_plural': 'Facebook Profiles',
            },
        ),
        migrations.CreateModel(
            name='GooglePlusProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_id', models.CharField(blank=True, max_length=140)),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='users.Profile')),
                ('username', models.CharField(blank=True, max_length=140)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=140)),
                ('last_name', models.CharField(blank=True, max_length=140)),
                ('time_created', models.DateField(blank=True, null=True, verbose_name='Time Created')),
                ('profile_image_path', models.CharField(blank=True, max_length=200, null=True)),
                ('activation_key', models.CharField(blank=True, max_length=140)),
                ('is_new', models.BooleanField(default=True)),
                ('is_cleared', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Google Plus Profile',
                'verbose_name_plural': 'Google Plus Profiles',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MileStone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=140, null=True)),
                ('year', models.CharField(blank=True, max_length=140, null=True)),
                ('body', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Milestone',
                'verbose_name_plural': 'Milestones',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('username', models.CharField(blank=True, max_length=250, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('profile_image_path', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('is_new', models.NullBooleanField(default=True)),
                ('is_avatar_processed', models.BooleanField(default=False)),
                ('is_avatar_transfered', models.BooleanField(default=False)),
                ('is_signature_customized', models.BooleanField(default=False)),
                ('is_online', models.BooleanField(default=False)),
                ('is_cleared', models.BooleanField(default=False)),
                ('is_facebook_signup_used', models.BooleanField(default=False)),
                ('is_google_signup_used', models.BooleanField(default=False)),
                ('is_twitter_signup_used', models.BooleanField(default=False)),
                ('is_linkedin_signup_used', models.BooleanField(default=False)),
                ('is_username_customized', models.BooleanField(default=False)),
                ('is_user_avatar', models.BooleanField(default=False)),
                ('is_google_avatar', models.BooleanField(default=False)),
                ('is_facebook_avatar', models.BooleanField(default=False)),
                ('is_twitter_avatar', models.BooleanField(default=False)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Address')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='SocialFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=250, null=True)),
                ('full_name', models.CharField(blank=True, max_length=250, null=True)),
                ('first_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('date_connected', models.DateField(blank=True, null=True, verbose_name='Date Connected')),
                ('profile_picture', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Social Friend',
                'verbose_name_plural': 'Social Friends',
            },
        ),
        migrations.CreateModel(
            name='SocialMedium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(blank=True, max_length=20, null=True)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Social Medium',
                'verbose_name_plural': 'Social Mediums',
            },
        ),
        migrations.CreateModel(
            name='StateProvince',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('abbreviation', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'State or Province',
                'verbose_name_plural': 'States or Provinces',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='dv_user', to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(blank=True, max_length=140)),
                ('is_partner', models.NullBooleanField(default=False)),
                ('is_associate', models.NullBooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=140)),
                ('last_name', models.CharField(blank=True, max_length=140)),
                ('title', models.CharField(blank=True, max_length=140)),
                ('bio', models.CharField(blank=True, max_length=1500)),
                ('avatar', models.ImageField(upload_to='avatars')),
            ],
            options={
                'verbose_name': 'Team Members',
                'verbose_name_plural': 'Team Members',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(blank=True, max_length=250, null=True)),
                ('date_used', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'verbose_name': 'User Activation',
                'verbose_name_plural': 'User Activations',
            },
        ),
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('remote_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('session_key', models.CharField(blank=True, max_length=200, null=True)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField(blank=True, null=True, verbose_name='Time Logged Out')),
                ('time_online_hours', models.IntegerField(blank=True, default=0, null=True)),
                ('time_online_minutes', models.IntegerField(blank=True, default=0, null=True)),
                ('time_online_seconds', models.IntegerField(blank=True, default=0, null=True)),
                ('time_online_total', models.CharField(blank=True, max_length=200, null=True)),
                ('time_online_delta', models.FloatField(blank=True, default=0, null=True)),
                ('date_visited', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
            },
        ),
        migrations.AddField(
            model_name='googleplusprofile',
            name='friends',
            field=models.ManyToManyField(to='users.SocialFriend'),
        ),
        migrations.AddField(
            model_name='address',
            name='state_province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.StateProvince'),
        ),
    ]
