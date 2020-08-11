from django.shortcuts import render
from django.http import JsonResponse, request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post


@api_view(['GET'])
def apiOverview(request):
  
  api_urls = {
    'List': '/news-list/',
    'Detail New': '/detail-new',
    'Create': '/news-create/',
    'Update': '/news-update/<str:pk>/',
    'Delete': '/news-delete/<str:pk>/',

  }

  return Response(api_urls)

@api_view(['GET'])
def newList(request):
  posts = Post.objects.all()
  serializer = PostSerializer(posts, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def newDetail(request, pk):
  posts = Post.objects.get(id=pk)
  serializer = PostSerializer(posts, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def newCreate(request):
  serializer = PostSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['POST'])
def newUpdate(request, pk):
  post = Post.objects.get(id=pk)
  serializer = PostSerializer(instance=post, data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def newDelete(request, pk):
  post = Post.objects.get(id=pk)
  post.delete()

  return Response("New successfully delete")