from django.shortcuts import render
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def Artistes(request):
    if request.method == 'GET':
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtisteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def artistes_listing(request, pk):
    try:
        artistes = Artiste.objects.get(pk=pk)
    except artistes.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = ArtisteSerializer(artistes)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArtisteSerializer(artistes, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        artistes.delete()
        return Response(status=204)



@api_view(['GET', 'POST'])
def Songs(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def songs_listing(request, pk):
    try:
        songs = Song.objects.get(pk=pk)
    except songs.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = SongSerializer(songs)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(songs, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        songs.delete()
        return Response(status=204)