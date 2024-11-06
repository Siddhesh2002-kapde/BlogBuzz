from django.db import models
from froala_editor.fields import FroalaField
from Blog.helpers import generate_slug
from django.contrib.auth.models import User
# Create your models here.

class MainCategory(models.Model):
    mainCat = models.CharField(max_length=500)
    image = models.ImageField(upload_to='main_cat',default=True)
    

    def __str__(self):
        return self.mainCat


class SubCategory(models.Model):
    main_categories = models.ManyToManyField(MainCategory, through='BlogModel',related_name='subcategories')
    subCat = models.CharField( max_length=500)


# rm -rf Blog/migrations
    def __str__(self):
        return self.subCat
    
class BlogModel(models.Model):
    MainCat = models.ForeignKey(MainCategory, on_delete=models.CASCADE, null=True, blank=True,default=True)
    SubCat = models.ForeignKey(SubCategory, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    pre_content = models.TextField(null= True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,default=True)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null = True, blank= True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)

