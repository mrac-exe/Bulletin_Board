from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from users.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django import forms


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories', through='Subscriber')

    def __str__(self):
        return self.name.title()


class Announce(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    # text = RichTextField()
    text = RichTextUploadingField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='AnnounceCategory', related_name='announce', verbose_name='Категория')

    def preview(self):
        return f"{self.text[:124]}..."

    def __str__(self):
        return f'{self.title.title()}'

    def get_absolute_url(self):
        return reverse('announce_detail', args=[str(self.id)])


class AnnounceCategory(models.Model):
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Reply(models.Model):
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE, verbose_name='Объявление')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.text.title()


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




