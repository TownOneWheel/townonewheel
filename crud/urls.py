from django.urls import path

from .views import AddView, CatDetailView, CheckedView, EditView, CatDelete, SearchView, CommentView

app_name = 'crud'

urlpatterns = [
    path('add/', AddView.as_view(), name='add'),
    path('cat_detail/<pk>', CatDetailView.as_view(), name='cat_detail'),
    path('cat_edit/<pk>', EditView.as_view(), name='cat_edit'),
    path('cat_delete/<pk>', CatDelete, name='cat_delete'),
    path('search/', SearchView.as_view(), name='search'),
    path('comment/<pk>', CommentView.as_view(),name='comment'),
    path('checked/', CheckedView.as_view(), name='checked'),
]