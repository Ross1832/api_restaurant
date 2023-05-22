from django.urls import path
from .api_view import MultilingualTextList, FeedbackList, CustomObtainAuthToken, MultilingualTextListCreateView, \
    MultilingualTextRetrieveUpdateDestroyView
from rest_framework.decorators import api_view
from .api_view import get_translations

urlpatterns = [
    path('feedback/', FeedbackList.as_view(), name="feedback-list"),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name="api-token-auth"),
    path('multilingual/', MultilingualTextListCreateView.as_view()),
    path('multilingual/<int:pk>/', MultilingualTextRetrieveUpdateDestroyView.as_view()),
    path('multilingual-text/', MultilingualTextList.as_view(), name="multilingual-text-list"),
    path('translations/', api_view(['GET'])(get_translations), name='get_translations'),
]

