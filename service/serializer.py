from rest_framework import serializers
from .models import Skill
from .models import Intent

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id','name','active','created_date')

class IntentSerializer(serializers.ModelSerializer):
    class Meata:
        model = Intent
        fields = ('id','name','handler')
