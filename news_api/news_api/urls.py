
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('news.api.urls')),
    path('job_api/', include('job_news.api.urls')),
]
