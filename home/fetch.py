from cgi import print_arguments
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from seller.models import Language_Levels, Occupation_list, Skill_list
from django.core.signing import Signer
import random

def get_random_code():
  num = 0
  count = 8
  rand = ""
  while num < count:
    ran = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    rand += str(ran)
    num += 1

  return rand

def search_f(request):
  paraml = request.GET.get("skill", None)
  paramo = request.GET.get("skill", None)
  params = request.GET.get("skill", None)
  if paraml:
    level = Language_Levels.objects.get(language=paraml)
    datas = level.name
    return JsonResponse({"result": datas})
  elif paramo:
    level = Occupation_list.objects.get(occupations=paramo)
    datas = level.name
    return JsonResponse({"result": datas})
  elif params:
    level = Skill_list.objects.get(skiller=params)
    datas = level.name
    return JsonResponse({"result": datas})
  else:
    return JsonResponse({"result": ""})