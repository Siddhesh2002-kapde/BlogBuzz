from django.contrib import admin
from Blog.models import *
# Register your models here.
admin.site.register(BlogModel)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
