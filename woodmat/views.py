from django.shortcuts import render

from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request,'index.html')


def categories(request):
  return render(request,'categories.html')

def category_detail(request):
  return render(request,'category_detail.html')

def products(request):
  return render(request,'products.html')

def product_detail(request):
  return render(request,'product_detail.html')

def artisan_profile(request):
  return render(request,'artisan_profile.html')


# Login here
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) # Or AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm() # Or AuthenticationForm()
    return render(request, 'login.html', {'form': form})


#  register here 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            #  mail system 
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect("login")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
  
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title':'register here'})
 