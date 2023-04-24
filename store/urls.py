from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.ItemListCreateAPIView.as_view()),
    path('manufacturer/', views.ManufacturerListCreateAPIView.as_view()),
    path('category/', views.category_list_create_api_view),
]