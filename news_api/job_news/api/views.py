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


class JobOfferDetailApiVew(APIView):
    """Return and edit Specific Joboffer response"""

    def get_object(self, pk):
        """Return Job offer object"""
        return get_object_or_404(JobOffer, pk=pk)

    def get(self, request, pk):
        """Return Job Detail Response"""
        serializer = JobOfferSerializer(self.get_object(pk), many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """Update Job detail"""
        serializer = JobOfferSerializer(
            self.get_object(pk), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Specific Job Offer"""
        job_offer = self.get_object(pk)
        job_offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
