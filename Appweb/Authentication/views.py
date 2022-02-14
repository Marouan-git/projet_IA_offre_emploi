from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

# Authentication




def login(request):
    if 'username'  in request.session:
        return redirect('index')
    else:    
        if request.method == 'POST':
            username = request.POST.get("username", "default value")
            userpassword = request.POST.get("userpassword", "default value")
            user = auth.authenticate(username=username, password=userpassword)

            if user is not None:
                request.session['username'] = username
                auth.login(request, user)                
                return redirect("/")
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('login')
        else:
            return render(request, 'Authentication/login.html')


def register(request):
    if 'username'  in request.session:
        return redirect('index')
    else:    
        if request.method == 'POST':
            email = request.POST['useremail']
            username = request.POST['username']
            userpassword = request.POST['userpassword']
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already Exists')
                return redirect('register')
            else:
                send_mail(
                    'Welcome To Minible',
                    'Congratulations  for your membership.',
                    settings.EMAIL_HOST_USER,
                    [email, 'test@test.com', 'demo@demo.com'],
                    fail_silently=False,
                )
                user = User.objects.create_user(
                    email=email, username=username, password=userpassword)
                user.save()
                return redirect('login')
        else:
            return render(request, 'Authentication/register.html')


def recoverpassword(request):
    if request.method == "POST":
        email = request.POST.get("email","default value")
        if User.objects.filter(email=email).exists():
            password_reset_form = PasswordResetForm(request.POST)
            if password_reset_form.is_valid():
                data = password_reset_form.cleaned_data['email']
                associated_users = User.objects.filter(Q(email=data))
                if associated_users.exists():
                    for user in associated_users:
                        subject = "Password Reset Requested"
                        email_template_name = "Authentication/email.txt"
                        c = {
                            "email": user.email,
                            'domain': '127.0.0.1:8000',
                            'site_name': 'Website',
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "user": user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                        }
                        email = render_to_string(email_template_name, c)
                        try:
                            send_mail(subject, email, 'admin@example.com',
                                    [user.email], fail_silently=False)
                        except BadHeaderError:
                            messages.info(request,"Email Doesn't Exists ")  
                            return redirect('recoverpassword')
                        return redirect("password_reset_done")
            password_reset_form = PasswordResetForm()
            return render(request=request, template_name="Authentication/recoverpassword.html", context={"password_reset_form": password_reset_form})
        else:
            if email == "":
                messages.info(request, 'Please Enter Your Email')
                return redirect('recoverpassword')
            else:
                messages.info(request, "Email doesn't  exist")
                return redirect('recoverpassword')
    else:
        return render(request, 'Authentication/recoverpassword.html')


def lockscreen(request):    
    if 'username'  not in request.session:
        return redirect('login')
    else:    
        if request.method == 'POST':
            userpassword = request.POST.get("userpassword", "default value")
            user = auth.authenticate( password=userpassword)

            if user is not None:
                auth.login(request, user)                
                return redirect("/")
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('login')
        else:
            return render(request, 'Authentication/lockscreen.html')
    
   
def logout(request):
    auth.logout(request)
    return render(request, 'Authentication/logout.html')
