from django.urls import path
from Blog.views import *
urlpatterns = [
    path('',index, name = 'home'),
    path('login_user/',login_user, name = 'login'),
    path('register_user/',register_user, name = 'register'),
    path('add_blog/',add_blog, name = 'add_blog'),
    path('blog/<slug:slug>/', blog_detail, name = 'blog_detail'),
    path('blog/<slug:slug>/edit/', update_blog, name = 'blog_update'),
    path('logout', logout_user, name = 'logout'),
    path('mainCat/<id>/',main_category_blogs,name = 'mainCat'),
    path('mainCat/<int:id>/<int:subcategory_id>/', main_category_blogs, name='subcategory_detail'),
]
