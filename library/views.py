from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def index(request):
    title = "Neighbourhood"
    user = Profile.objects.get(user=request.user.id)
    # business = Business.objects.all().filter(hood=user.hood)
    context = {
        "title": title,
        # "business": business
    }
    return render(request, 'index.html', context)


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
            return redirect('/profile/')
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


def search_results(request):
    if 'businesses' in request.GET and request.GET["businesses"]:
        search_term = request.GET.get('businesses')
        # searched_businesses = Business.search_by_name(search_term)
        message = f'{search_term}'

        context = {
            "message": message,
            # "businesses": searched_businesses,
        }
        return render(request, 'search.html', context)
    else:
        message = "Search for a business by its name"
        return render(request, 'search.html', {"message": message})








