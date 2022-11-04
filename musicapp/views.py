from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics


# Create your views here.
#Using viewsets
# class ArtisteViewSet(viewsets.ModelViewSet):
#     queryset = Artiste.objects.all()
#     serializer_class = ArtisteSerializer


# class SongViewSet(viewsets.ModelViewSet):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer

#     def patch(self, request, pk, *args, **kwargs):
#         song_object = Song.objects.get(id=pk)
#         data = request.data

#         song_object.title = data.get['title']
#         song_object.date_realeased = data.get['date_realeased']


class ArtisteList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArtisteDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, id=pk)

    

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, id=pk)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, id=pk)


class SongList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SongDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, id=pk)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, id=pk)

    def patch(self, request, pk, *args, **kwargs):
        return self.partial_update(request, id=pk)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, id=pk)

class LyricList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LyricDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer


    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, id=pk)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, id=pk)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, id=pk)