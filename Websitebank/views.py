from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Websitebank.models import account_user, transaction
from .forms import profileregisterform,transactionforms
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
#import mysql.connector
from django.contrib.auth.decorators import login_required
 
# Create your views here.

@login_required(login_url="login/")
def homepage(request):
    return render(request,'home.html')


def login(request):
    '''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
                user = account_user.user_objects.get(username=username,password=password)
                if user is not None:               
                    return render(request, 'home.html', {})
                else:
                    print("Someone tried to login and failed.")
                    print("They used username: {} and password: {}".format(username,password))
     
                    return redirect('/')
        except Exception as identifier:
                
                return redirect('/')
     
    else:
            return render(request, 'base.html')
            '''
   # conn = mysql.connector.connect(host = "localhost", user = "",passwd = "",database = "wads_project")
    return render(request,'login.html')
     

def camerainput(request):
    return HttpResponse("<h1>Input Camera</h1>")

def signup(request):
   if request.method == 'POST': 
        form1 = UserCreationForm(request.POST)
        form2 = profileregisterform(request.POST)
        if form1.is_valid() and form2.is_valid():
            username = form1.cleaned_data.get('username')
            messages.success(request, f'Successfully created an account for {username}')
            new_user = form1.save()
            newdata = form2.save(commit=False)
            if newdata.user_id is NULL or newdata.user_id is None:
                newdata.user =   new_user
            newdata.save()
            return redirect("bank-transactions")
   else:
        form1 = UserCreationForm()
        form2 = profileregisterform()
   context= {'userdata': form1,
                'bankdata':form2 }
   return render(request, 'signup.html',context)

@login_required(login_url="login/")
def payments(request):
    return render(request, 'payments.html')
    # if request.method == 'POST':
    #     payforms = transactionforms(request.POST)
    #     if payforms.is_valid():
            
    #         payforms.save()
    #         return redirect('bank-transactions')
    # else:
    #     payforms = transactionforms()
    # return render(request,'payments.html',{'payforms':payforms})

# @login_required(login_url="login/")
# def logout(request):
    # return redirect('login.html')
    # return render(request, 'logout.html')

@login_required(login_url="login/")
def profile(request):
    return render(request, 'profile.html')