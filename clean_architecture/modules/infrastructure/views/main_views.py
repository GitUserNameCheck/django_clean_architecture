from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from clean_architecture.modules.infrastructure.forms import RegisterUserForm, LoginForm

# @login_required(login_url='login')
def homepage(request):
    return render(request, 'index.html')

def register(request):

    form  = RegisterUserForm() #формирование формы

    if request.method == 'POST': #проверка на то, что метод POST

        form = RegisterUserForm(request.POST) # получение объекта RegisterUserForm после ввода данных

        if form.is_valid(): # проверка корректности ввода

            form.save() # сохранение объекта в бд

            return redirect('login') # перенаправление на маршрут 'login

    context = {'registerform' : form} # сохранение введенных данных для повторного открытия веб-страницы

    return render(request, 'register.html', context)


def login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username') #получение данных из запроса
            password = request.POST.get('password')
            user = authenticate(request, username=username, password = password) #проверка пользовательских данных для входа
            if user is not None:
                auth.login(request, user) #создание новой сессии
                return redirect('personalCabin')
            
    context = {'loginform' : form}
    return render(request, 'login.html', context)


# @login_required(login_url='login')
def personalCabin(request):
    return render(request, 'personalCabin.html')


# @login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('homepage')