from django.shortcuts import redirect, render
from django.views.generic import View, DetailView
from django.db.models import Q
from config.settings import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

import boto3
from boto3.session import Session
from datetime import datetime
import glob, os

from crud.models import Cat, CatImage, Comment



    
class AddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cat_add.html')
    
    def post(self, request, *args, **kwargs):
        catname=request.POST['catname']
        friendly=request.POST['friendly']
        gender=request.POST['gender']
        color=request.POST['color']
        neutering=request.POST['neutering']
        location_lat=request.POST['location_lat']
        location_lon=request.POST['location_lon']
        upload_user=request.user
        image = request.FILES.getlist('img')
        cat_locations = '{0:0.3f}'.format(float(location_lat)) + '{0:0.3f}'.format(float(location_lon))
        path =  './crud/cat_location/*'
        location_file_lists = glob.glob(path)
        location_file_names = []
        for location_file_list in location_file_lists:
            file_path = os.path.splitext(location_file_list)[0]
            location_file_names.append(file_path.split('/')[-1])
        if not catname or not friendly:
            content = {'state': True, 'error': '빈 항목이 있습니다. 모두 채워주세요!'}
            return render(request, 'cat_add.html', content)
        # if not type(friendly) == int:
        #     content = {'state': True, 'error': '개냥이 지수는 숫자만 입력 가능합니다!'}
        #     return render(request, 'cat_add.html', content)
        if cat_locations in location_file_names:
            with open('./crud/cat_location/{}.txt'.format(cat_locations), 'r') as f:
                cat_list = f.readlines()
            cat_pk_list = cat_list[0].split(',')[:-1]
            cat_lists = []
            for cat_pk in cat_pk_list:
                cat = Cat.objects.filter(pk=int(cat_pk)).first()
                cat_lists.append(cat)
            return render(request, 'overlap.html', {
                'cat_lists': cat_lists,
                'catname': catname,
                'friendly': friendly,
                'gender': gender,
                'color': color,
                'neutering': neutering,
                'location_lat': location_lat,
                'location_lon': location_lon,
                'upload_user': upload_user,
                'image': image,
            })
        cat = Cat.objects.create(
            catname=catname,
            friendly=friendly,
            gender=gender,
            color=color,
            neutering=neutering,
            location_lat=location_lat,
            location_lon=location_lon,
            upload_user=upload_user,
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
        with open('./crud/cat_location/{}.txt'.format(cat_locations), 'a') as f:
            f.write(str(cat.pk))
            f.write(',')
        return redirect('index')

class CheckedView(View):
    def get(self, request, *args, **kwargs):
        return redirect('index')

    def post(self, request, *args, **kwargs):
        catname=request.POST['catname']
        friendly=request.POST['friendly']
        gender=request.POST['gender']
        color=request.POST['color']
        neutering=request.POST['neutering']
        location_lat=request.POST['location_lat']
        location_lon=request.POST['location_lon']
        upload_user=request.user
        cat_locations = '{0:0.3f}'.format(float(location_lat)) + '{0:0.3f}'.format(float(location_lon))
        cat = Cat.objects.create(
            catname=catname,
            friendly=friendly,
            gender=gender,
            color=color,
            neutering=neutering,
            location_lat=location_lat,
            location_lon=location_lon,
            upload_user=upload_user,
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
        with open('./crud/cat_location/{}.txt'.format(cat_locations), 'a') as f:
            f.write(str(cat.pk))
            f.write(',')
        return redirect('index')

class CatDetailView(DetailView):
    model = Cat
    context_object_name = 'cat'
    template_name = 'cat_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['cat'] = Cat.objects.filter(cat=kwargs['object'])
        context['image_lists'] = CatImage.objects.filter(cat=kwargs['object'])
        context['comments'] = Comment.objects.filter(cat=kwargs['object'])
        return context

class EditView(View):
    def get(self, request, *args, **kwargs):
        cat = Cat.objects.filter(pk=kwargs['pk']).first()
        return render(request, 'cat_edit.html', {'cat': cat})
    
    def post(self, request, *args, **kwargs):
        Cat.objects.filter(pk=kwargs['pk']).update(
            catname=request.POST['catname'],
            friendly=request.POST['friendly'],
            gender=request.POST['gender'],
            color=request.POST['color'],
            neutering=request.POST['neutering'],
            location_lat=request.POST['location_lat'],
            location_lon=request.POST['location_lon'],
            upload_user=request.user,
        )
        return redirect('crud:cat_detail', kwargs['pk'])

def CatDelete(request, pk):
    cat = Cat.objects.filter(pk=pk)
    cat.update(catname='deleted_cat', is_deleted=True, location_lat=0, location_lon=0)
    return redirect('index')

class SearchView(View):
    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword', '')
        search_cats = {}
        if keyword:
            search_cats = Cat.objects.filter(
                Q(catname__icontains=keyword)
            )
        return render(request, 'search.html', { 'search_cats': search_cats })

class CommentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cat_detail.html')

    def post(self, request, *args, **kwargs):
        cat = Cat.objects.filter(pk=kwargs['pk']).first()
        user = request.user
        Comment.objects.create(
            cat=cat,
            user=user,
            content=request.POST['content'],
        )
        return redirect('crud:cat_detail', kwargs['pk'])




    
