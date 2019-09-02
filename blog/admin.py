from django.contrib import admin
from blog.models import Post, Category
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["title", "created_on"]}),
        ("Content", {'fields': ["body"]}),
        ("Category", {'fields': ["categories"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }



class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
