from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout



def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('login')
    context = {"form": form}
    return render(request, "users/register.html", context)

# Create your views here.
def login_view(request):
    # future -> ?next=/articles/create/
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "users/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "users/logout.html", {})

def edit_users(request):
    form = UserChangeForm(request.POST or None)

    return render(request, "users/edit_user.html", {'form': form})

"""def index(request):
    return render(request, 'users/login.html')

class BBLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = 'addfilm'"""