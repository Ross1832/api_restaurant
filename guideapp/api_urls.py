from django.urls import path
from .api_view import MultilingualTextList, FeedbackList, CustomObtainAuthToken

urlpatterns = [
    path('multilingual-text/', MultilingualTextList.as_view(), name="multilingual-text-list"),
    path('feedback/', FeedbackList.as_view(), name="feedback-list"),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name="api-token-auth"),
]
