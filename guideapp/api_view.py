from collections import defaultdict

from django.http import JsonResponse
from rest_framework import generics
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from .models import MultilingualText, Feedback
from .serializers import MultilingualTextSerializer, FeedbackSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate


class MultilingualTextList(generics.ListCreateAPIView):
    serializer_class = MultilingualTextSerializer

    def get_queryset(self):
        queryset = MultilingualText.objects.all()
        language = self.request.query_params.get('languages', None)
        if language is not None:
            queryset = queryset.filter(languages=language)
        return queryset


class MultilingualTextListCreateView(generics.ListCreateAPIView):
    queryset = MultilingualText.objects.all()
    serializer_class = MultilingualTextSerializer


class MultilingualTextRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MultilingualText.objects.all()
    serializer_class = MultilingualTextSerializer


class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class CustomObtainAuthToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


def get_translations(request):
    translations = MultilingualText.objects.all()
    serializer = MultilingualTextSerializer(translations, many=True)

    data = defaultdict(lambda: defaultdict(dict))

    for item in serializer.data:
        data[item['languages']]['translation'][item['key']] = item['content']

    return JsonResponse(data)
