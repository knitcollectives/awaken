from django.contrib import admin
from django.db import models
from blog.models import Post, Category, Byline, Contact, Service
from tinymce.widgets import TinyMCE


# Register your models here.
class PostAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["title", "created_on"]}),
        ("Content", {'fields': ["body"]}),
        ("Category", {'fields': ["categories"]}),
        ("Byline", {"fields": ["author"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }



class CategoryAdmin(admin.ModelAdmin):
    pass


class BylineAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


class ServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Byline, BylineAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Service, ServiceAdmin)
