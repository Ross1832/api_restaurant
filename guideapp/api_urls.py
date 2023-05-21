from django.urls import path
from .api_view import MultilingualTextList, FeedbackList, CustomObtainAuthToken, MultilingualTextListCreateView, \
    MultilingualTextRetrieveUpdateDestroyView

urlpatterns = [
    path('feedback/', FeedbackList.as_view(), name="feedback-list"),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name="api-token-auth"),
    path('multilingual/', MultilingualTextListCreateView.as_view()),
    path('multilingual/<int:pk>/', MultilingualTextRetrieveUpdateDestroyView.as_view()),
    path('multilingual-text/', MultilingualTextList.as_view(), name="multilingual-text-list"),
]


