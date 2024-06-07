from django.urls import path
from .views import DestinationCreate, DestinationList,DestinationUpdate, DestinationDestroy, DestinationRetrieve

urlpatterns = [
    path('destinations/', DestinationList.as_view(), name='destination-list'),
    path('destinations/create/', DestinationCreate.as_view(), name='destination-create'),
    path('destinations/<int:pk>/', DestinationRetrieve.as_view(), name='destination-retrieve'),
    path('destinations/<int:pk>/update/', DestinationUpdate.as_view(), name='destination-update'),
    path('destinations/<int:pk>/delete/', DestinationDestroy.as_view(), name='destination-delete'),
    path('list/', DestinationList.as_view(), name='destination-list'),
    path('create/', DestinationCreate.as_view(), name='destination-create'),
    path('<int:pk>/', DestinationRetrieve.as_view(), name='destination-retrieve'),
    path('<int:pk>/update/', DestinationUpdate.as_view(), name='destination-update'),
    path('<int:pk>/delete/', DestinationDestroy.as_view(), name='destination-delete'),

]