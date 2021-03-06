# This is where our intelligence shines
# Pipeline is where we manage user accounts

import urllib2
import json
from simplejson import loads
import urllib
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
import django.contrib.auth as auth
from django.shortcuts import redirect
from social.pipeline.partial import partial
from django.contrib.auth import logout
from django.conf import settings
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage as storage
from django.core.files.base import ContentFile
from django.db.models import Min
from social.apps.django_app.views import _do_login
from social.backends.facebook import FacebookOAuth2
from requests import request, HTTPError
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify
import facebook
import open_facebook
from open_facebook import OpenFacebook
from open_facebook import utils
from open_facebook import api
from django_facebook.utils import get_user_model, mass_get_or_create, \
    cleanup_oauth_url, get_profile_model, parse_signed_request, hash_key, \
    try_get_profile, get_user_attribute

import logging

from StringIO import StringIO
import PIL
from PIL import Image
import urllib2
import random
import json
import os
import re
import sys

from custom.users.models import Profile
from signals import facebook_strategy_used
from signals import googleplus_strategy_used
from signals import twitter_strategy_used
from signals import linkedin_strategy_used

from callbacks import facebook_profile_handler
from callbacks import googleplus_profile_handler


@partial
def check_username(backend, details, user, response, is_new=False,*args,**kwargs):
         try:
              min_id = User.objects.filter(email=user.email).aggregate(id=Min('id'))
              usr_id=int(min_id['id'])
              is_new=False
              usr = User.objects.get(id=usr_id)
              if usr.id < user.id:
                   return {'user':usr}
              else:
                  return {'user':user} 

         except ObjectDoesNotExist:
              min_id = User.objects.filter(username=user.username).aggregate(id=Min('id'))
              usr_id=int(min_id['id'])
              is_new=False
              usr = User.objects.get(id=usr_id)
              if usr.id < user.id:
                  return {'user':usr}

              else:
                  user.username = str(user.id)
                  user.save()
                  return {'user':user}

         except Exception,R:
              if user:
                 return {'user':user}


@partial
def check_duplicate(backend, details, user, response, is_new=False,*args,**kwargs):
         if user:
             return {'user':user}

         if backend.name == 'facebook':
             email = details['email']
             try:
                  min_id = User.objects.filter(email=email).aggregate(id=Min('id'))
                  usr_id=int(min_id['id'])
                  is_new=False
                  usr = User.objects.get(id=usr_id)
                  return {"user":usr}
             except ObjectDoesNotExist:
                  return {"user":None}
             except Exception, R:
                  return {"user":None}

         if backend.name == 'google-oauth2':
             email = details['email']
             try:
                  min_id = User.objects.filter(email=email).aggregate(id=Min('id'))
                  usr_id=int(min_id['id'])
                  is_new=False
                  usr = User.objects.get(id=usr_id)
                  return {"user":usr}
             except ObjectDoesNotExist:
                  return {"user":None}
             except Exception, R:
                  return {"user":None}



@partial
def consolidate_profiles(backend, details, user, response, is_new=False,*args,**kwargs):

    min_id = User.objects.filter(email=user.email).aggregate(id=Min('id'))
    usr_id=min_id['id']
    usr = User.objects.get(id=usr_id)
    

    if backend.name == 'linkedin':
        skip_user = False

        try:
            try:
                 min_id = User.objects.filter(email=user.email).aggregate(id=Min('id'))
                 usr_id=int(min_id['id'])
                 is_new=False
                 usr = User.objects.get(id=usr_id)

            except ObjectDoesNotExist:
                 min_id = User.objects.filter(username=user.username).aggregate(id=Min('id'))
                 usr_id=int(min_id['id'])
                 is_new=False
                 usr = User.objects.get(id=usr_id)
            except Exception,R:
                 usr = user

            if usr.id < user.id:
                is_new = False
                try:
                    user.profilesummary.delete()
                except Exception, R:
                    pass
                try:
                    user.profile.delete()
                except Exception, R:
                    pass
                try:
                    user.delete()
                except Exception, R:
                     pass

                return {'user':usr}
            else:
                is_new = True
                usr = user


        except ObjectDoesNotExist:
            usr = user
            skip_user = False

        try:
             profile=Profile.objects.get(id=usr.id)
        except ObjectDoesNotExist:
             profile = Profile.objects.create(id=usr.id,username=usr.username,is_new=True,email=usr.email,first_name=usr.first_name,last_name=usr.last_name,user=usr)

        if profile.is_user_avatar==False:
            avatar_url = response.get('pictureUrls', {}).get('values', [None])[0]
            if not avatar_url:
               avatar_url = response.get('pictureUrl')

            profile.profile_image_path=avatar_url
            profile.save()




    elif backend.name == 'twitter':
        skip_user = False

        try:
            try:
                 min_id = User.objects.filter(email=user.email).aggregate(id=Min('id'))
                 usr_id=int(min_id['id'])
                 is_new=False
                 usr = User.objects.get(id=usr_id)

            except ObjectDoesNotExist:
                 min_id = User.objects.filter(username=user.username).aggregate(id=Min('id'))
                 usr_id=int(min_id['id'])
                 is_new=False
                 usr = User.objects.get(id=usr_id)
            except Exception,R:
                 usr = user

            if usr.id < user.id:
                is_new = False
                try:
                    user.profilesummary.delete()
                except Exception, R:
                    pass
                try:
                    user.profile.delete()
                except Exception, R:
                    pass
                try:
                    user.delete()
                except Exception, R:
                     pass

                return {'user':usr}
            else:
                is_new = True
                usr = user


        except ObjectDoesNotExist:
            usr = user
            skip_user = False
        except Exception, R:
            usr = user
            skip_user = False

        try:
             profile=Profile.objects.get(id=usr.id)
        except ObjectDoesNotExist:
             profile = Profile.objects.create(id=usr.id,username=usr.username,is_new=True,email=usr.email,first_name=usr.first_name,last_name=usr.last_name,user=usr)



        if profile.is_user_avatar==False:            

            avatar_url = response.get('profile_image_url', '').replace('_normal', '')
            profile.profile_image_path=avatar_url
            profile.save()


    elif backend.name == 'google-oauth2':

        skip_user = False

        try:
            try:
                 min_id = User.objects.filter(email=user.email).aggregate(id=Min('id'))
                 usr_id=int(min_id['id'])
                 is_new=False
                 usr = User.objects.get(id=usr_id)

            except ObjectDoesNotExist:
                 min_id = User.objects.filter(username=user.username).aggregate(id=Min('id'))
                 usr_id=int(min_id['id'])
                 is_new=False
                 usr = User.objects.get(id=usr_id)
            except Exception,R:
                 usr = user

            if usr.id < user.id:
                is_new = False
                try:
                    user.profilesummary.delete()
                except Exception, R:
                    pass
                try:
                    user.profile.delete()
                except Exception, R:
                    pass
                try:
                    user.delete()
                except Exception, R:
                     pass

                return {'user':usr}
            else:
                is_new = True
                usr = user


        except ObjectDoesNotExist:
            usr = user
            skip_user = False
        except Exception, R:
            usr = user
            skip_user = False

        try:
             profile=Profile.objects.get(id=usr.id)
        except ObjectDoesNotExist:
             profile = Profile.objects.create(id=usr.id,username=usr.username,is_new=True,email=usr.email,first_name=usr.first_name,last_name=usr.last_name,user=usr)


        if profile.is_user_avatar==False:

                 profile_picture_url=str(response['image'].get('url'))[:-2] # Read the original google avatar

                 profile_picture_url=profile_picture_url+'200' # provide the size

                 input_file = StringIO(urllib2.urlopen(profile_picture_url).read()) # read the file into buffer
                 image = Image.open(input_file)   # Create an image
                 output = StringIO()
                 format = 'PNG' # or 'JPEG' or whatever you want
                 image.save(output, format)   # Format image
                 contents = output.getvalue() # Get the size
                 size = len(contents) # The default avatar has size 4712 so we know we have to replace it


                 if size <= 5000: # Verify size and replace if smaller than 5000
                       profile_picture = settings.PROFILE_IMAGE_PATH
                       is_google_avatar = False
                 else:
                       profile_picture = profile_picture_url
                       is_google_avatar = True

                 output.close() # Close the buffer
                 profile.is_google_avatar=True 
                 profile.profile_image_path=profile_picture_url #Save the avatar in profile url
                 profile.save()
         
        if profile.is_new:
                 profile_picture_url=str(response['image'].get('url'))[:-2] # Read the original google avatar

                 profile_picture_url=profile_picture_url+'200' # provide the size

                 input_file = StringIO(urllib2.urlopen(profile_picture_url).read()) # read the file into buffer
                 image = Image.open(input_file)   # Create an image
                 output = StringIO()
                 format = 'PNG' # or 'JPEG' or whatever you want
                 image.save(output, format)   # Format image
                 contents = output.getvalue() # Get the size
                 size = len(contents) # The default avatar has size 4712 so we know we have to replace it


                 if size <= 5000: # Verify size and replace if smaller than 5000
                       profile_picture = settings.PROFILE_IMAGE_PATH
                       is_google_avatar = False
                 else:
                       profile_picture = profile_picture_url
                       is_google_avatar = True

                 if not profile_picture:
                    profile_picture = settings.PROFILE_IMAGE_PATH

                 profile.profile_image_path=profile_picture

                
                 usr.username = usr.username.lower()
                 profile.username = usr.username.lower()
                 profile.save()
                 profile.save()
        else:
            profile_picture =  profile.profile_image_path


        if profile.is_new:
                     is_new = True
        else:
                     is_new = False

        googleplus_strategy_used.send(sender=usr, instance = usr,
                                            is_new=is_new, email=usr.email,
                                            profile_picture=profile_picture, kwargs=None)


        return {'user': usr}



    elif backend.name == 'facebook':

        skip_user = False

        try:
            try:
                 min_id = User.objects.filter(email=user.email).aggregate(id=Min('id'))
                 usr_id=int(min_id['id'])
                 is_new=False
                 usr = User.objects.get(id=usr_id)

            except ObjectDoesNotExist:
                 min_id = User.objects.filter(username=user.username).aggregate(id=Min('id'))
                 usr_id=int(min_id['id'])
                 is_new=False
                 usr = User.objects.get(id=usr_id)
            except Exception,R:
                 usr = user

            if usr.id < user.id:
                is_new = False
                try:
                    user.profile.delete()
                except Exception, R:
                    pass
                try:
                    user.profile.delete()
                except Exception, R:
                    pass
                try:
                    user.delete()
                except Exception, R:
                     pass

                return {'user':usr}
            else:
                usr = user


        except ObjectDoesNotExist:
            usr = user
            skip_user = False
        except Exception, R:
            usr = user
            skip_user = False

        try:
             profile=Profile.objects.get(id=usr.id)
        except ObjectDoesNotExist:
             is_new=True
             profile = Profile.objects.create(id=usr.id,username=usr.username,is_new=True,email=usr.email,first_name=usr.first_name,last_name=usr.last_name,user=usr)



        if profile.is_user_avatar==False:
            if profile.is_google_avatar==False:
                 profile_picture_url= "http://graph.facebook.com/%s/picture?type=large"%response['id'] # Read the original google avatar


                 input_file = StringIO(urllib2.urlopen(profile_picture_url).read()) # read the file into buffer
                 image = Image.open(input_file)   # Create an image
                 output = StringIO()
                 format = 'PNG' # or 'JPEG' or whatever you want
                 image.save(output, format)   # Format image
                 contents = output.getvalue() # Get the size
                 size = len(contents) # The default avatar has size 4712 so we know we have to replace it


                 if size <= 6000: # Verify size and replace if smaller than 5000
                       profile_picture = settings.PROFILE_IMAGE_PATH
                       is_facebook_avatar = False
                 else:
                       profile_picture = profile_picture_url
                       is_facebook_avatar = True

                 output.close() # Close the buffer
                 profile.is_facebook_avatar=True
                 profile.profile_image_path=profile_picture_url #Save the avatar in profile url
                 profile.save()

                 
        if profile.is_new:
                     is_new = True
        else:
                     is_new = False


        facebook_strategy_used.send(sender=usr, instance = usr,
                                          new_id=user.id,
                                          is_new=is_new,
                                          email=usr.email,
                                          facebook_id=response['id'],
                                          request=request,
                                          kwargs=None)
        return {'user':usr}



googleplus_strategy_used.connect(googleplus_profile_handler)
facebook_strategy_used.connect(facebook_profile_handler)
