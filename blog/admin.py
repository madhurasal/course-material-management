from django.contrib import admin
from .models import Category, Post




#for configuration of category model
class categoryadmin(admin.ModelAdmin):
    list_display = ('cat_id', 'img_tag', 'title', 'add_date',)
    search_fields = ('title',)


#for configuration of post model
class postadmin(admin.ModelAdmin):
    list_display = ('post_id', 'title', 'cat', 'post_date',)
    list_filter = ('cat',)
    list_per_page = 10

# Register your models here.
admin.site.register(Category, categoryadmin)
admin.site.register(Post, postadmin)