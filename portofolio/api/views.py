from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializer import BlogpostSerializer, RepositorySerializer
from .models import Blogpost, Repository

# Create your views here.

class BlogpostAPIView(APIView):

    #Get all blogpost or create a new one

    def get(self, request):
        blogpost = Blogpost.objects.all()
        serializers = BlogpostSerializer(blogpost, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = BlogpostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogpostDetail(APIView):

    #Get a blogpost then you can update or delete

    def get_object(self, pk):
        try:
            return Blogpost.objects.get(pk=pk)
        except Blogpost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        blogpost = self.get_object(pk)
        serializers = BlogpostSerializer(blogpost)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        blogpost = self.get_object(pk)
        serializers = BlogpostSerializer(blogpost, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blogpost = self.get_object(pk)
        blogpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RepositoryAPIView(APIView):

    #Get all repository or create a new one

    def get(self, request, format=None):
        repository = Repository.objects.all()
        serializers = RepositorySerializer(repository, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = RepositorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class RepositoryDetail(APIView):

    #Get a blogpost then you can update or delete

    def get_object(self, pk):
        try:
            return Repository.objects.get(pk=pk)
        except Repository.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        repository = self.get_object(pk)
        serializers = RepositorySerializer(repository)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        repository = self.get_object(pk)
        serializers = RepositorySerializer(repository, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        repository = self.get_object(pk)
        repository.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)