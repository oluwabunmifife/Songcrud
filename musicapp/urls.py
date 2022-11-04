from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtisteList, ArtisteDetail, SongList, SongDetail, LyricList, LyricDetail

#Using router
# router = DefaultRouter()
# router.register('artistes', ArtisteViewSet, basename='artistes')
# router.register('songs', SongViewSet, basename='songs')

urlpatterns = [
    #Using router
    # path('', include(router.urls)),

    #Using viewsets
    # path('', ArtisteViewSet.as_view({'get': 'list'})),
    # path('artistes/<int:pk>/', ArtisteViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    # path('songs/<int:pk>/', SongViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    
    #Using mixins
    path('artistes/', ArtisteList.as_view()),
    path('artistes/<int:pk>/', ArtisteDetail.as_view()),
    path('songs/', SongList.as_view()),
    path('songs/<int:pk>/', SongDetail.as_view()),
    path('lyrics/', LyricList.as_view()),
    path('lyrics/<int:pk>/', LyricDetail.as_view()),
]
