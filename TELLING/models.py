from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django_resized import ResizedImageField

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    category_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"

class Story(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    thumbnail = ResizedImageField(size=[500,300], upload_to = 'image',  blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Stories"
