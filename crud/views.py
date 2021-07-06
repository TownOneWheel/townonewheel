from django.shortcuts import redirect, render
from django.views.generic import View, DetailView
from django.db.models import Q
from config.settings import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

import boto3
from boto3.session import Session
from datetime import datetime

from crud.models import Cat, CatImage

    
class AddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add.html')
    
    def post(self, request, *args, **kwargs):
        cat = Cat.objects.create(
            catname=request.POST['catname'],
            friendly=request.POST['friendly'],
            gender=request.POST['gender'],
            color=request.POST['color'],
            neutering=request.POST['neutering'],
            # location=request.POST['location'],
            location_lat=request.POST['location_lat'],
            location_lon=request.POST['location_lon'],
            upload_user=request.user,
            )
        files = request.FILES.getlist('img')
        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME,
        )
        s3 = session.resource('s3')
        now = datetime.now().strftime('%Y%H%M%S')
        s3_url="https://django-cat-project.s3.ap-northeast-2.amazonaws.com/"
        for file in files:
            s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
                Key=now+file.name,
                Body=file
            )
            CatImage.objects.create(
                cat=cat,
                url=s3_url+now+file.name,
            ) 
        return redirect('index')

class CatDetailView(DetailView):
    model = Cat
    context_object_name = 'cat'
    template_name = 'cat_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_lists'] = CatImage.objects.filter(cat=kwargs['object'])
        return context

class EditView(View):
    def get(self, request, *args, **kwargs):
        cat = Cat.objects.filter(pk=kwargs['pk']).first()
        return render(request, 'cat_edit.html', {'cat': cat})
    
    def post(self, request, *args, **kwargs):
        print('--')
        Cat.objects.filter(pk=kwargs['pk']).update(
            catname=request.POST['catname'],
            friendly=request.POST['friendly'],
            gender=request.POST['gender'],
            color=request.POST['color'],
            neutering=request.POST['neutering'],
            location=request.POST['location'],
            upload_user=request.user,
        )
        return redirect('crud:cat_detail', kwargs['pk'])

class SearchView(View):
    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword', '')
        search_cat = {}
        if keyword:
            search_cat = Cat.objects.filter(
                Q(catname__icontains=keyword)
            ).first()
        return render(request, 'search.html', { 'search_cat': search_cat })