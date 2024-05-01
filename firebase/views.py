from django.shortcuts import render, redirect
import pyrebase
from firebase_admin import auth

Config = {
    'apiKey': "AIzaSyBWy9OCAKP3NR4dFPLfSUzzk-QXLBkdZmY",
    'authDomain': "teste-saudekids.firebaseapp.com",
    'projectId': "teste-saudekids",
    'storageBucket': "teste-saudekids.appspot.com",
    'messagingSenderId': "103564023514",
    'appId': "1:103564023514:web:702908e4968a10ba1a77e3",
    'databaseURL': "postgresql://postgres:admin@localhost:5432/FabricaTeste"
}

firebase = pyrebase.initialize_app(Config)
firebase_auth = firebase.auth()


def Logar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = firebase_auth.sign_in_with_email_and_password(email, password)
            return redirect('home')
        except auth.InvalidPasswordError:
            print("Senha incorreta")
            return render(request, 'Login.html', {'error': 'A senha fornecida está incorreta.'})
        except auth.UserNotFoundError:
            print("Usuário não encontrado")
            return render(request, 'Login.html', {'error': 'O email fornecido não está registrado.'})
        except auth.InternalError:
            print("Erro interno")
            return render(request, 'Login.html', {'error': 'Ocorreu um erro interno. Por favor, tente novamente mais tarde.'})
    elif request.method == 'GET':
        return render(request, 'Login.html')


    
def Cadastrar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = firebase_auth.create_user_with_email_and_password(email, password)
            return redirect('login')
        except auth.EmailAlreadyExistsError:
            return render(request, 'Cadastrar.html', {'error': 'O email fornecido já está em uso.'})
        except auth.InternalError:
            return render(request, 'Cadastrar.html', {'error': 'Ocorreu um erro interno. Por favor, tente novamente mais tarde.'})
    else:
        return render(request, 'Cadastrar.html')
    
def Home(request):
    return render(request, 'Home.html')