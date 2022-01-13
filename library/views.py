from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from django.http import HttpResponse, Http404,HttpResponseRedirect


# Create your views here.
@login_required(login_url='/login')
def index(request):
    title = "Neighbourhood"
    user = Profile.objects.get(user=request.user.id)
    posts = Book.objects.all().order_by("-pk")
    context = {
        "title": title,
        "post": posts
    }
    
    return render(request, 'index.html', context)


def subscription(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            your_address = form.cleaned_data['your_address']
            phone = form.cleaned_data['phone']
            age = form.cleaned_data['age']
            
            recipient = SubscriptionRecipients(name = name,email =email,your_address=your_address, phone=phone, age=age)
            recipient.save()
            send_welcome_email(name,email)
            return redirect('/')
                 
    else:
        form = SubscribeForm()
    return render(request, 'subscribe.html', {"form":form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signUp.html', {"form": form})


@login_required(login_url='/login')
def create_profile(request):

    Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
    return render(request, 'create_profile.html', {"u_form": u_form, "p_form": p_form, })


@login_required(login_url='/login')
def profile(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/login')
def search_results(request):
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get('title')
        searched_book = Book.search_by_title(search_term)
        message = f'{search_term}'

        context = {
            "message": message,
            "searched_book": searched_book,
        }
        return render(request, 'search.html', context)
    else:
        message = "Search for a book by its title"
        return render(request, 'search.html', {"message": message})

@login_required(login_url='/login')
def post_book(request):

    posts = Book.objects.all().order_by("-pk")

    return render(request, 'post.html', {"posts":posts})

@login_required(login_url='/login')
def newbook(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= request.user
            post.save()
            return redirect('post_book')

    else:
        form = PostForm()
    return render(request, 'postnewbook.html' ,{'form': form})


@login_required(login_url='/login')
def library(request):

    books = Book.objects.all().order_by("-pk")

    return render(request, 'library.html', {"books":books})

@login_required(login_url='/login')  
def service(request):
    title = "service"
    user = Profile.objects.get(user=request.user.id)
    context = {
        "title": title,
    }
    return render(request, 'about.html', context)







