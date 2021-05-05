from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import Airticle
from .serializers import AirticleSerializer


@api_view(['GET', 'POST'])
def article_list_create_api_view(request):
    """return and save article api"""

    if request.method == 'GET':
        """Return all airticle data"""
        airticles = Airticle.objects.filter(active=True)
        serializer = AirticleSerializer(airticles, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        """Save posted airticle to the databse"""
        serializer = AirticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
