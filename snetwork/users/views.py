from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt


def dashboardU(request):
    if request.user.is_authenticated:
        return redirect("dashboard/1")
    else:
        return render(request, "network/dashboardU.html")

@csrf_exempt
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

    if form.is_valid():
        new_user = form.save()
        login(request, new_user)
        return redirect("/")

    context = {'form': form}
    return render(request, 'registration/register.html', context)