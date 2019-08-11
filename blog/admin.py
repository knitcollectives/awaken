from django.contrib import admin
from blog.models import Post, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["title", "created_on"]}),
        ("Content", {'fields': ["body"]}),
        ("Category", {'fields': ["categories"]})
    ]

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
