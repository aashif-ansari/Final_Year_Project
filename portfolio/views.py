from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Profile,Post
from django.contrib import messages

# Create your views here.

def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    posts = Post.objects.all()

    return render(request, 'index.html', {'user_profile': user_profile})

def upload(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/feed')
    else:
        return redirect('/')

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email is already used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username is taken by another user')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()

                #log user in and redirect to settings page
                #and  create profile object for the user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request,'password does not matching')
            return redirect('signup')
        
    else:
        return render(request,'signup.html')