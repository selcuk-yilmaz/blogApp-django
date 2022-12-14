from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.
def register(request):
    form = UserCreationForm(request.POST or None)
    # form = UserCreationForm()
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("home")

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)

# def login(request):

#     return redirect('home')
# def logout(request):
#     return redirect('home')
