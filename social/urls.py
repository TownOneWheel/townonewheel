from django.urls import path

from .views import SignupView, EditView, LoginView, logout, delete

app_name = 'social'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('edit/<pk>', EditView.as_view(), name='edit'),
    path('delete/<int:user_pk>', delete, name='delete'),
]