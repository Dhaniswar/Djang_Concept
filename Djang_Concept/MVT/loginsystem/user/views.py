from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from user.forms import UserRegisterForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def index(request):
    return render(request, 'user/index.html', {'title':'index'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print("Request data => ", form)
        if form.is_valid():
            form.save()
            username = form.changed_data.get('username')
            email = form.changed_data.get('email')

            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'bkdhaniswar7991@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'})

def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'Account does not exist please sign in ')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'login'})



