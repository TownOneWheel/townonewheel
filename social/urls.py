from django.urls import path

from .views import SignupView, DetailView, EditView, LoginView, RelationShipView, logout, delete

app_name = 'social'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('edit/<pk>', EditView.as_view(), name='edit'),
    path('delete/<int:user_pk>', delete, name='delete'),
    path('relationship/<int:pk>', RelationShipView.as_view(), name='relationship'),
    path('detail/<pk>', DetailView.as_view(), name='detail'),

]