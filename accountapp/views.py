from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #log the user in
            return redirect('articles:home')
    else:
        form = UserCreationForm()
        print(request.path)
    return render(request,'accounts/signup.html', context={'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            user = form.get_user()
            login(request, user)

            # this next is an input in the html but we get the value from the request.get.next
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("articles:home")

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("accounts:login")
