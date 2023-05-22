from django.http import JsonResponse
from rest_framework import serializers
from .models import MultilingualText, Feedback
from rest_framework import generics
from collections import defaultdict


class MultilingualTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultilingualText
        fields = ['key', 'languages', 'content']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
