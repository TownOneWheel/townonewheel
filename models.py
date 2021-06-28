class Cat(models.Model):
    COLOR_CHOICES = [
        ('BL', 'Black'),
        ('YL', 'Cheese'),
        ('WH', 'White'),
        ('3C', 'Three Colors'),
    ]
    SEX_CHOICES = [
        ('N/A', 'N/A'),
        ('M', 'Male'),
        ('F', 'Female'),
    ]    
    name = models.CharField(max_length=8)
    owner = models.ForeignKey(Profile, related_name='mycats', null=True, blank=True)
    carer = models.ManyToMany(Profile, related_name='myastraycats', null=True, blank=True)
    TNR = models.BooleanField(default=False)
    color = models.CharField(choices=COLOR_CHOICES, null=True, blank=True)    
    sex = models.CharField(choices=SEX_CHOICES, default='N/A')
    age = models.IntegerField(default=1)
    friendliness = models.IntegerField(null=True, blank=True)
    location = models.TextField()
    profile_img_url = models.TextField()
    created_at = models.TextField()
    updated_at = models.TextField()
    is_deleted = models.BooleanField(default=True)


class Profile(models.Model):
    name = models.CharField(max_length=8)
    profile_img_url = models.TextField()
    introduction = models.TextField()
    created_at = models.TextField()
    updated_at = models.TextField()
    is_deleted = models.BooleanField(default=True)

class Relationship(models.Model):
    profile = models.OneToOneField(Profile, related_name='myrelationship')
    favorite_cats = models.ManyToMany(Cat, related_name='relationship')
    followers = models.ManyToMany(Profile, related_name='relationship')

class Notification(models.Model):
    created_at = 
    read = models.BooleanField(default=False)
    

class Comment(models.Model):
    writer = models.Foreignkey(Profile, related_name='mycomments')
    cat = models.ForeignKey(Cat, related_name='comments')
    liked_bys = models.ManyToMany(Profile, related_name='likedcomments')
    created_at = models.TextField()
    is_deleted= models.BooleanField(default=False)
