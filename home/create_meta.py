from cgi import print_arguments
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from seller.models import Personal_Info, Occupation_list, Languages, Professional_Info, Language_Levels, Occupation, Skill_list, Skill
from django.core.signing import Signer
import random
import json

def get_random_code():
  num = 0
  count = 8
  rand = ""
  while num < count:
    ran = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    rand += str(ran)
    num += 1

  return rand

def soap(request):
  try:
    fullname = request.POST.get("info[fullname]", None)
    picture = request.POST.get("info[profile_pics]", None)
    description = request.POST.get("info[description]", None)
    url = request.POST.get("info[url]", None)
    occup = request.POST.get("occup", None)
    skill = request.POST.get("skill", None)
    langs = request.POST.get("language", None)
    
    sell = Personal_Info(profile=request.user, full_Name=fullname, profile_Picture=picture, description=description, is_seller=True, seller_mode=True)
    sell.save()

    if url:
      web = Professional_Info(profile=sell, personal_Website=url)
      web.save()
    # print(sell)
    #language = sell.languages_set.all()
    if langs > 0:
      for i in range(int(langs)):
        info_name = request.POST.get(f"info[language][{i}][name]", None)
        info_level = request.POST.get(f"info[language][{i}][level]", None)
        lang_obj = Language_Levels.objects.get(language=info_level)
        lang = Languages(profile=sell, language=info_name, Language_Levels=lang_obj)
        lang.save()
    if skill > 0:
      for i in range(int(skill)):
        skill_name = request.POST.get(f"info[skills][{i}][skill]", None)
        skill_level = request.POST.get(f"info[skills][{i}][level]", None)
        skills = Skill_list.objects.get(skiller=skill_name)
        ins_skill = Skill(profile=sell, skills=skills, level=skill_level)
        ins_skill.save()
    if occup > 0:
      for i in range(int(occup)):
        occupation_name = request.POST.get(f"info[occupation][{i}][occup]", None)
        occupation_from = request.POST.get(f"info[occupation][{i}][fyear]", None)
        occupation_to = request.POST.get(f"info[occupation][{i}][tyear]", None)
        occp_obj = Occupation_list.objects.get(occupations=occupation_name)
        occp = Occupation(profile = sell, occupation= occp_obj, from_year=occupation_from, to_year=occupation_to)
        occp.save()

    return JsonResponse({"status": "success"})
  
  except:
    return JsonResponse({"status": "unknown error"})