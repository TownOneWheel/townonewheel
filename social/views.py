from django.shortcuts import render, redirect
from django.views import generic
from django.views import View
from django.contrib import auth
from django.contrib.auth.models import User

from social.services import UserService, SignupDto, LoginDto, UpdateDto
# Create your views here.

class IndexTemplateView(generic.TemplateView):
    template_name = 'index.html'

class SignupView(View):
    def get(self, request, *args, **kwargs) :
        return render(request, 'signup.html')

    def post(self, request, *args, **kwargs):
        signup_dto = self._build_signup_dto(request.POST)
        result =UserService.signup(signup_dto)

        if(result['error']['state']):
            context = {'error': result['error']}
            return render(request, 'signup.html', context)
        auth.login(request, result['user'])
        return redirect('index')
        
    @staticmethod
    def _build_signup_dto(post_data) :
        return SignupDto(
            userid=post_data['userid'],
            password=post_data['password'],
            password_check=post_data['password_check'],
            introduction=post_data['introduction'],
            name=post_data['name'],
            email=post_data['email'],
        )

class LoginView(View) :
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        login_dto = self._build_login_dto(request.POST)
        result = UserService.login(login_dto)
        if (result['error']['state']):
            context = {'error' : result['error']}
            return render(request, 'login.html', context)
        auth.login(request, result['user'])
        return redirect('index')

    @staticmethod
    def _build_login_dto(post_data):
        return LoginDto(
            userid=post_data['userid'],
            password=post_data['password']
        )

def logout(request) :
    auth.logout(request)
    return redirect('index')

class EditView(View) :
    def get(self, request, *args, **kwargs):
        context = {'user' : UserService.find_by(kwargs['pk'])}
        return render(request, 'edit.html', context)

    def post(self, request, *args, **kwargs):
        update_dto = self._build_update_dto(request.POST)
        result = UserService.update(update_dto)
        if (result['error']['state']):
            context = {'error':result['error']}
            return render(request, 'edit.html', context)
        return redirect('index')
    
    def _build_update_dto(self, post_data):
        return UpdateDto(
            name=post_data['name'],
            email=post_data['email'],
            introduction=post_data['introduction'],
            pk=self.kwargs['pk']
        )
    
def delete(request, user_pk):
    user = User.objects.filter(pk=user_pk)

    user.update(is_active=False)
    auth.logout(request)

    return redirect('index')
