from django.shortcuts import render
from django.http import JsonResponse, request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


@api_view(['GET'])
def apiOverview(request):
  
  api_urls = {
    'List of News': '/news-list/',
    'Detail New': '/detail-new/<str:pk>/',
    'Create New': '/news-create/',
    'Update New': '/news-update/<str:pk>/',
    'Delete New': '/news-delete/<str:pk>/',
    'List of Comments': '/news-comments/',
    'Detail Comment': '/detail-comment/<str:pk>',
    'Create Comment': '/comment-create/',
    'Update Comment': '/comment-update/<str:pk>',
    'Delete Comment': '/comment-delete/<str:pk>'

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


@api_view(['GET'])
def commentList(request):
  comment = Comment.objects.all()
  serializer = CommentSerializer(comment, many=True)

  return Response(serializer.data)

@api_view(['POST'])
def commentCreate(request):
  serializer = CommentSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)
