from django.shortcuts import render,redirect
from .forms import UserSignUpForm,LoginForm
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.password_validation import validate_password as validate
from SnapchatCampaigns.sweet_alert_message import SweetAlertMessage
from SnapchatCampaigns.constants import SweetAlertIcons
from django.contrib.auth import authenticate,login as auth_login
# Create your views here.
def login(request):
    context = {
        'title': "Login",
    }
    if 'message' in request.session:
        message = request.session.pop('message', None)
        context['message'] = message
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email,password=password)
            if user:
                auth_login(request,user)
                request.session['message'] = SweetAlertMessage("Hello","Welcome Back!!",SweetAlertIcons.SUCCESS_ICON.value).getAlert()

                return redirect('home-page')
            else:
                request.session['message'] = SweetAlertMessage("Oops!","Either email or password are wrong! please try again ..",SweetAlertIcons.ERROR_ICON.value).getAlert()
        else:
            request.session['message'] = SweetAlertMessage("Oops!","Either email or password are wrong! please try again ..",SweetAlertIcons.ERROR_ICON.value).getAlert()

    return render(request, 'accounts/login.html', context)

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

def validate_password(request):
    password1 = request.GET.get('password1', None)
    data = { 'is_invalid': False, 'error_message':'error'}
    try:
        validate(password1)
    except ValidationError as error:
        data = {
        'is_invalid': True,
         'error_message':error.messages
        }
    return JsonResponse(data)
def register(request):
    is_email_field_has_errors = ""
    is_password1_field_has_errors = False
    is_password2_field_has_errors = False
    email_field_errors = ""
    password1_field_errors = ""
    password2_field_errors = ""
    context = {}
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            request.session['message'] = SweetAlertMessage("Welcome","Glad to have you with us",SweetAlertIcons.SUCCESS_ICON.value).getAlert()
            return redirect('login-page')
        else:
            for x,y in form.errors.get_json_data(escape_html=True).items():
                print(x,y[0]['message'])
                if x == "email":
                    is_email_field_has_errors = "error=true"
                    email_field_errors += y[0]['message']
                elif x == "password1":
                    is_password1_field_has_errors = "error=true"
                    password1_field_errors += y[0]['message']
                elif x == "password2":
                    is_password2_field_has_errors = "error=true"
                    password2_field_errors += y[0]['message']
    context.update({
             'title': "Register",
             'is_email_field_has_errors': is_email_field_has_errors,
             'is_password1_field_has_errors': is_password1_field_has_errors,
             'is_password2_field_has_errors': is_password2_field_has_errors,
             'email_field_errors': email_field_errors,
             'password1_field_errors': password1_field_errors,
             'password2_field_errors': password2_field_errors,
        })

    return render(request, 'accounts/register.html', context)