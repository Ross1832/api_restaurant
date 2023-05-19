from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("guideapp.urls")),
    path('', include('guideapp.api_urls')),
]
