from rest_framework import generics
from .models import MultilingualText, Feedback
from .serializers import MultilingualTextSerializer, FeedbackSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class MultilingualTextList(generics.ListCreateAPIView):
    queryset = MultilingualText
    serializer_class = MultilingualTextSerializer


class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['data'])
        user = token.user
        return Response({'token': token.key, 'user_id': user.pk, 'email': user.email})


