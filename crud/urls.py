from django.urls import path

from .views import AddView, CatDetailView, EditView, SearchView

app_name = 'crud'

urlpatterns = [
    path('add/', AddView.as_view(), name='add'),
    path('cat_detail/<pk>', CatDetailView.as_view(), name='cat_detail'),
    path('cat_edit/<pk>', EditView.as_view(), name='cat_edit'),
    path('search/', SearchView.as_view(), name='search'),
]