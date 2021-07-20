from django.db.models.query import RawQuerySet
from social.models import Relationship
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import generic
from django.views import View
from django.contrib import auth
from django.contrib.auth.models import User

from social.services import UserService, SignupDto, LoginDto, UpdateDto, RelationShipDto, RelationShipService, CatRelationShipService, CatRelationShipDto

from crud.models import Cat, CatImage

class IndexTemplateView(generic.ListView):
    model = Cat
    queryset = Cat.objects.all()
    template_name = 'index.html'


    def get(self, request):
        self.object_list = self.get_queryset()
        context = { 'cats' : self.object_list }
        return render(request, 'index.html', context)

    def post(self, request):
        context = super().get_context_data()
        context['position'] = request.POST['position']
        return render(request, 'index.html', context)

class SignupView(View):
    def get(self, request, *args, **kwargs) :
        return render(request, 'signup.html')

    def post(self, request, *args, **kwargs):
        signup_dto = self._build_signup_dto(request)
        result = UserService.signup(signup_dto)
        
        if(result['error']['state']):
            context = {'error': result['error']}
            return render(request, 'signup.html', context)
        auth.login(request, result['user'])
        return redirect('index')
        
    @staticmethod
    def _build_signup_dto(request) :
        return SignupDto(
            userid=request.POST['userid'],
            profile_img_url=request.FILES.get('image'),
            password=request.POST['password'],
            password_check=request.POST['password_check'],
            introduction=request.POST['introduction'],
            name=request.POST['name'],
            email=request.POST['email'],
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
        update_dto = self._build_update_dto(request)
        result = UserService.update(update_dto)
        if (result['error']['state']):
            context = {'error':result['error']}
            return render(request, 'edit.html', context)
        return redirect('index')
    
    def _build_update_dto(self, request):
        return UpdateDto(
            name=request.POST['name'],
            email=request.POST['email'],
            profile_img_url=request.FILES.get('image'),
            introduction=request.POST['introduction'],
            pk=self.kwargs['pk']
        )
    
def delete(request, user_pk):
    user = User.objects.filter(pk=user_pk)

    user.update(is_active=False)
    auth.logout(request)

    return redirect('index')

class RelationShipView(View):
    def post(self, request, *args, **kwargs):
        relationship_dto = self._build_relationship_dto(request)
        result = RelationShipService.toggle(relationship_dto)

        return redirect('social:detail', kwargs['pk'])
    
    def _build_relationship_dto(self, request):
        return RelationShipDto(
            user_pk=self.kwargs['pk'],
            requester=request.user
        )

class DetailView(generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'detail.html'

class CatRelationShipView(View):
    def post(self, request, *args, **kwargs):
        catrelationship_dto = self._build_catrelationship_dto(request)
        result = CatRelationShipService.toggle(catrelationship_dto)

        return redirect('crud:cat_detail', kwargs['pk'])
    
    def _build_catrelationship_dto(self, request):
        return CatRelationShipDto(
            cat_pk=self.kwargs['pk'],
            requester=request.user
        )

class FavoriteView(generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'favorite.html'

class FollowView(generic.DetailView):
    model = User
    context_object_name= 'user'
    template_name = 'follow.html'

class FollowerView(generic.DeleteView):
    model = User
    context_object_name= 'user'
    template_name = 'follower.html'

