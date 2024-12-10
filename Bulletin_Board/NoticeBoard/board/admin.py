from django.contrib import admin
from .models import Author, Category, Announce, AnnounceCategory, Reply

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Announce)
admin.site.register(AnnounceCategory)
admin.site.register(Reply)


# Register your models here.
