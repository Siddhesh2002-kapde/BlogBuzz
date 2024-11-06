from django.shortcuts import render,redirect,get_object_or_404
from .form import BlogForm,UpdateForm
from django.conf import settings
from Blog.models import *
from django.contrib import messages

from django.contrib.auth import logout,login, authenticate
# Create your views here.

def index(request):
    mainCat = MainCategory.objects.all() 
    blog = BlogModel.objects.all().order_by('-upload_to')[:5]
    context = {
        'mainCat':mainCat,
        'blogs':blog
    }

    return render(request,'home.html',context)

def main_category_blogs(request, id,subcategory_id=None):
    #main_category variable id wise search karel
    main_category = get_object_or_404(MainCategory, id = id)
    #subcat filter karel main category 
    subCat = SubCategory.objects.filter(main_categories__mainCat = main_category).distinct()
    
    
    if subcategory_id:
        selected_subcategory = get_object_or_404(SubCategory, id=subcategory_id)
        cards = BlogModel.objects.filter(MainCat=main_category, SubCat = selected_subcategory)
    else:
        selected_subcategory = None
        cards = BlogModel.objects.filter(MainCat = main_category)
        search = request.GET.get('search')

        if search:
            cards = cards.filter(title__icontains = search)
        

    context = {
        'main_category': main_category,
        'subCat': subCat,
        'selected_subcategory': selected_subcategory,
        'cards': cards,
        'search':search,


    }
    
    return render(request,'main_category_blogs.html',context)




def add_blog(request):
    if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')  # Adjust the redirect as needed
            else:
                form = BlogForm()

    context = {
        'form': BlogForm
    }
    return render(request, 'add_blog.html',context)

def update_blog(request,slug):
    queryset = get_object_or_404(BlogModel, slug = slug)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance = queryset)

        if form.is_valid():
            form.save()
            return redirect('/',slug=queryset.slug)
        
    else:
        form = BlogForm(instance = queryset)

    context = {
        'form': form,
        'queryset':queryset
    }
    
    return render(request, 'update_blog.html',context)


def blog_detail(request,slug):
    queryset = get_object_or_404(BlogModel,slug = slug)
    data = BlogModel.objects.all()


    context = {
          'queryset':queryset,
          'data':data,
     }
    return render(request, 'each_blog.html',context)




def login_user(request):
    if (request.method == 'POST'):
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        # if username doesn't exists then message to the user.
        user = User.objects.filter(username=username)
        if (not user.exists()):
            messages.error(request, 'Username Does not exists!')
            return redirect('/login_user')
        # cheak  account ahea ka nahi
        userAuth = authenticate(username=username, password=password)
        if (userAuth is None):
            messages.error(request, 'Account does not exists')
            return redirect('/login_user')
        else:
            # acccout assel ther value fit houn user login hoil
            login(request, userAuth)
            return redirect('/')
        
    return render(request,'login_user.html')

def register_user(request):
    if (request.method == 'POST'):
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        userAuth = User.objects.filter(username=username)
        if (userAuth.exists()):
            messages.info(request, 'Username Alraday exists!')
            return redirect('/register_user')

        queryset = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        queryset.set_password(password)
        queryset.save()
        messages.info(request, 'Account Create Successfully!')
        return redirect('/login_user')
    return render(request,'register_user.html')



def logout_user(request):
    logout(request)
    return redirect('/')



    

    
               


