from rest_framework import serializers
from .models import MultilingualText, Feedback


class MultilingualTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultilingualText
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
