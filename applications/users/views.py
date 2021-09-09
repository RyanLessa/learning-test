from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views import View


@login_required
def protected_template(request):
    return render(request, 'authenticated.html')


def logout_user(request):
    logout(request)
    form = AuthenticationForm()
    return render(request, 'authentication.html', {'form': form})


class Authenticate(View):

    def get(self, request):
        return render(request,
                      'authentication.html',
                      {'form': AuthenticationForm()})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

        return render(request, 'authentication.html')
