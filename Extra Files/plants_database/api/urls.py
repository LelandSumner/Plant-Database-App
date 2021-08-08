from django.urls import path

from .views import ListPlant, ListBerry, ListFlower, ListLeaf, ListStem, DetailPlant, DetailBerry, DetailFlower, DetailLeaf, DetailStem

urlpatterns = [
    path('plant/', ListPlant.as_view()),
    path('plant/<str:name>', DetailPlant.as_view()),
    path('berry/', ListBerry.as_view()),
    path('berry/<int:pk>', DetailBerry.as_view()),
    path('flower/', ListFlower.as_view()),
    path('flower/<int:pk>', DetailFlower.as_view()),
    path('leaf/', ListLeaf.as_view()),
    path('leaf/<int:pk>', DetailLeaf.as_view()),
    path('stem/', ListStem.as_view()),
    path('stem/<int:pk>', DetailStem.as_view()),
       
]