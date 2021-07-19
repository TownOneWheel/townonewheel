from os import stat
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from dataclasses import dataclass
from .models import Profile, Relationship
from crud.models import Cat
from boto3.session import Session
from datetime import datetime
from config.settings import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

@dataclass
class SignupDto():
    userid: str
    password: str
    password_check: str
    introduction: str
    name: str
    email: str
    profile_img_url: str

@dataclass
class LoginDto() :
    userid: str
    password: str

@dataclass
class UpdateDto() :
    name: str
    introduction: str
    email: str
    profile_img_url: str
    pk : str

@dataclass
class RelationShipDto():
    user_pk: str
    requester: User

@dataclass
class CatRelationShipDto():
    cat_pk: str
    requester: User

ERROR_MSG = {
    'EXIST_ID': '이미 존재하는 아이디 입니다',
    'NO_EXIST_ID': '존재하지 않는 아이디 입니다',
    'MISSING_INPUT': '항목을 모두 채워주세요',
    'PASSWORD_CHECK': '비밀번호를 확인해주세요',
    'RESIGN_FROM': '탈퇴한 아이디 입니다',
}

class UserService():
    @staticmethod
    def find_by(user_pk):
        return get_object_or_404(User, pk=user_pk)
    @staticmethod
    def signup(dto: SignupDto):
        file = dto.profile_img_url
        if file is None :
            if(not dto.userid or not dto.password or not dto.password_check or not dto.name or not dto.email or not dto.introduction):
                return {'error' : {'state' : True, 'msg' : ERROR_MSG['MISSING_INPUT']}}
            user = User.objects.filter(username=dto.userid, is_active=True)
            if (len(user)>0):
                return {'error' : {'state': True, 'msg':ERROR_MSG['EXIST_ID']}}    
            if User.objects.filter(username=dto.userid, is_active=False):
                return {'error': {'state': True, 'msg':ERROR_MSG['RESIGN_FROM']}}
            if (dto.password != dto.password_check):
                return {'error': {'state': True, 'msg': ERROR_MSG['PASSWORD_CHECK']}}

            user = User.objects.create_user(username=dto.userid, password=dto.password) 
            Profile.objects.create(user=user, name=dto.name, introduction=dto.introduction, email=dto.email, profile_img_url=file)   

            return {'error': {'state': False}, 'user' :user}
        else:
            session = Session(
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                region_name=AWS_S3_REGION_NAME,
            )
            s3 = session.resource('s3')
            now = datetime.now().strftime('%Y%H%M%S')
            s3_url="https://django-cat-project.s3.ap-northeast-2.amazonaws.com/"
            s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
                Key=now+file.name,
                Body=file
            )
            
            if(not dto.userid or not dto.password or not dto.password_check or not dto.name or not dto.email or not dto.introduction):
                return {'error' : {'state' : True, 'msg' : ERROR_MSG['MISSING_INPUT']}}
            user = User.objects.filter(username=dto.userid, is_active=True)
            if (len(user)>0):
                return {'error' : {'state': True, 'msg':ERROR_MSG['EXIST_ID']}}    
            if User.objects.filter(username=dto.userid, is_active=False):
                return {'error': {'state': True, 'msg':ERROR_MSG['RESIGN_FROM']}}
            if (dto.password != dto.password_check):
                return {'error': {'state': True, 'msg': ERROR_MSG['PASSWORD_CHECK']}}

            user = User.objects.create_user(username=dto.userid, password=dto.password) 
            Profile.objects.create(user=user, name=dto.name, introduction=dto.introduction, email=dto.email, profile_img_url=s3_url+now+file.name)   

            return {'error': {'state': False}, 'user' :user}

    @staticmethod
    def login(dto: LoginDto):
        if (not dto.userid or not dto.password):
            return {'error': {'state' : True, 'msg' : ERROR_MSG['MISSING_INPUT']}}
        user = User.objects.filter(username=dto.userid,is_active=True)
        if (len(user) == 0):
            return {'error': {'state': True, 'msg': ERROR_MSG['NO_EXIST_ID']}}
        # if (len(user) > 0 and user.first().password!=dto.password):
        if not check_password(dto.password, user.first().password):
            return {'error': {'state': True, 'msg': ERROR_MSG['PASSWORD_CHECK']}}
                         
        auth_user = authenticate(username=dto.userid, password=dto.password)
        
        return { 'error' : {'state': False}, 'user': auth_user}

    @staticmethod
    def update(dto: UpdateDto):
        if (not dto.name or not dto.introduction or not dto.email):
            return {'error': {'state': True, 'msg': ERROR_MSG['MISSING_INPUT']}}
        
        file = dto.profile_img_url
        print(1, file)
        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME,
        )
        s3 = session.resource('s3')
        now = datetime.now().strftime('%Y%H%M%S')
        s3_url="https://django-cat-project.s3.ap-northeast-2.amazonaws.com/"
        s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key=now+file,
            Body=file
        )

        Profile.objects.filter(pk=dto.pk).update(name=dto.name, introduction=dto.introduction, email=dto.email, profile_img_url = s3_url+now+file)

        return {'error':{'state':False}}

class RelationShipService():
    @staticmethod
    def toggle(dto: RelationShipDto):
        user = User.objects.filter(pk=dto.user_pk).first()
        relationship = Relationship.objects.filter(user=user).first()
        if (relationship is None):
            relationship = Relationship.objects.create(user=user)
        if (dto.requester in relationship.followers.all()):
            relationship.followers.remove(dto.requester)
            return { 'error' : { 'state': False }, 'data' : 'unfollowed' }
        relationship.followers.add(dto.requester)
        return { 'error' : { 'state': False }, 'data' : 'followed' }

class CatRelationShipService():
    @staticmethod
    def toggle(dto: CatRelationShipDto):
        cat = Cat.objects.filter(pk=dto.cat_pk).first()
        relationship = Relationship.objects.filter(user=dto.requester).first()
        if (relationship is None):
            relationship = Relationship.objects.create(user=dto.requester)
        if (cat in relationship.favorite_cat.all()):
            relationship.favorite_cat.remove(cat)
            return { 'error' : { 'state': False } }
        relationship.favorite_cat.add(cat)
        return { 'error' : { 'state': False } }
