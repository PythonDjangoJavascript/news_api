from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from news.models import Airticle, Journalist
from .serializers import AirticleSerializer, JournalistSeriazliser


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
def article_detail_api_view(request, pk):
    """manages single article detail api view"""

    try:
        article = Airticle.objects.get(pk=pk)
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


class ArticleListApiView(APIView):
    """Classbased Api view that matian article list"""

    def get(self, request):
        """Mantain get request and return article list"""
        articles = Airticle.objects.filter(active=True)
        serializer = AirticleSerializer(articles, many=True)

        return Response(serializer.data)

    def post(self, request):
        """Mantain post request and add article to the database"""
        serializer = AirticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailApiView(APIView):
    """Classbased Api view mantain article detail response"""

    def get_object(self, pk):
        """Fetch article object from database"""
        return get_object_or_404(Airticle, pk=pk)

    def get(self, request, pk):
        """Fetch article object and return respnse"""
        article = self.get_object(pk)
        serializer = AirticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update article object"""
        article = self.get_object(pk)
        serialzier = AirticleSerializer(article, data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """delete article from database"""
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JournalistApiView(APIView):
    """Mantain Journalist List Response"""

    def get(self, request):
        """Fetch journalist List"""

        journalists = Journalist.objects.all()
        serializer = JournalistSeriazliser(
            journalists,
            many=True,
            context={'request': request}
        )

        return Response(serializer.data)

    def post(self, request):
        """Create new Journalist Object"""

        serializer = JournalistSeriazliser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JournalistDetailApiView(APIView):
    """Mantain Journalist Detail API Response"""

    def get_object(self, id):
        """Return Journalist Jobject"""
        return get_object_or_404(Journalist, pk=id)

    def get(self, request, id):
        """Returnd Journalist Deteail Response"""
        journalist = self.get_object(id)
        serializer = JournalistSeriazliser(journalist, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        """Update Journalist Object"""
        journalist = self.get_object(id)
        serializer = JournalistSeriazliser(journalist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Delete an Journalist Object"""
        journalist = self.get_object(id)
        journalist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
