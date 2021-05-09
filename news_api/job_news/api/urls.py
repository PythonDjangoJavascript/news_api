from django.urls import path
from . import views


urlpatterns = [
    path('job_offers/', views.JobOfferApiView.as_view(), name='job-list'),
    path('job_offers/<int:pk>/',
         views.JobOfferDetailApiVew.as_view(), name='job-detail'),
]
