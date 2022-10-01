from datetime import datetime
from django.db import models
from django.contrib.auth.models import *
from ckeditor.fields import RichTextField

def validate_file_Extention(value):
    import os
    from django.core.exceptions import ValidationError
    extention = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not extention.lower() in valid_extensions:
        raise ValidationError('Unsuported file extension')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar', null=False, blank=False, validators=[validate_file_Extention])
    description = models.CharField(max_length=512, null=False, blank=False)
    def __str__(self):
        return self.user.username

class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/article_cover/', null=False, blank=False, validators=[validate_file_Extention])
    content = RichTextField()
    create_at = models.DateField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/category_cover/', null=False, blank=False, validators=[validate_file_Extention])

    def __str__(self):
        return self.title
