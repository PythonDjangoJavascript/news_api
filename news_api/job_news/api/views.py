from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from job_news.models import JobOffer
from .serializers import JobOfferSerializer


class JobOfferApiView(APIView):
    """Mantain JobOffer Response"""

    def get(self, request):
        """Return Job offer list Response"""
        joboffers = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(joboffers, many=True)

        return Response(serializer.data)

    def post(self, request):
        """Manages post request of job offers"""
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
