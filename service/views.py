from django.shortcuts import render
from .models import Skill, Intent
from .serializer import SkillSerializer, IntentSerializer
from rest_framework import generics
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class IntentViewSet(viewsets.ModelViewSet):
    queryset= Intent.objects.all()
    serializer_class = IntentSerializer

# @api_view
# def api_root(request,format=None):
    # return Response('skills',reverse('skill-list',request=request,format=format))
