from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import Airticle
from .serializers import AirticleSerializer


@api_view(['GET', 'POST'])
def article_list_create_api_view(request):
    """manages all active articel list api view"""

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


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_api_view(request, id):
    """manages single article detail api view"""

    try:
        article = Airticle.objects.get(pk=id)
    except Airticle.DoesNotExist:
        return Response({
            'error': {
                'Code': 404,
                'message': 'Article does not exist'
            }
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        """Return selected article detail"""
        serializer = AirticleSerializer(article, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        """Update articel"""
        serializer = AirticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        """Delete an article from the database"""
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
