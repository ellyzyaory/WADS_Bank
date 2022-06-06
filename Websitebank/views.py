from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Websitebank.models import payments, profiles
from .forms import profileregisterform,transactionforms
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
#import mysql.connector
from django.contrib.auth.decorators import login_required
 
# Create your views here.

@login_required(login_url="login/")
def homepage(request):
    if request.user.is_authenticated:
        giver_id = request.user.id
        giver_transactions = payments.objects.filter(sender_id = giver_id)
        context ={
        'trans': giver_transactions   
        #'Payment_id': giver_transactions.payment_id,
        #'Receiver_no': giver_transactions.receiver_no,
        #'amount_tranfer': giver_transactions.amount,
        #'notes_given': giver_transactions.notes

        }
        return render(request,'home.html',context)
    else:
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
def payment(request):
    if request.method == 'POST':
        payforms = transactionforms(request.POST)
        confirm_pin = request.POST.get('pin')
        if payforms.is_valid():
           # if request.user.is_authenticated():
                sender_profile = request.user.profiles
                sender_balance = request.user.profiles.balance
                sender_pin = request.user.profiles.pin
                input_pin = request.POST.get('pin')
                # if sender id matches the input
                if input_pin == sender_pin : 
                    balance = payforms.cleaned_data.get('amount')
                    receiver_no = payforms.cleaned_data.get('receiver_no')
                    receiver_profile = profiles.objects.filter(card_no = receiver_no).first()
                    receiver_amount = receiver_profile.balance
                    new_amount_receiver = receiver_amount + balance
                    new_amount_sender = sender_balance - balance
                    receiver_profile.balance = new_amount_receiver
                    sender_profile.balance = new_amount_sender
                    sender_profile.save()
                    receiver_profile.save()
                    new_transaction = payforms.save(commit = False)
                    # for initialising sender id 
                    if new_transaction.sender_id is NULL or new_transaction.sender_id is None:
                        new_transaction.sender =   request.user 
                    new_transaction.save()
                    return redirect('bank-payments')
                else:
                    messages.add_message("Please input the correct PIN")
                    redirect('bank-payments')
    else:
        payforms = transactionforms()
    
    return render(request,'payments.html',{'forms':payforms} )

@login_required(login_url="login/")
def profile(request):
    # if request.user.is_authenticated:
    #     user_id = request.user.id
    #     image = profileimages.objects.filter(profile_id=user_id)
    #     context ={
    #         'img': image
    #     }
    #     if request.method == 'POST':
            # confirm_image = request.POST.get(image)
            # form = imageform(request.POST, request.FILES)

            # if form.is_valid():
            #     image_save = form.save(commit = False)
            #     if image_save.profile_id is NULL or image_save.profile_id is None:
            #         image_save.profile =   request.user.profiles
            #         image_save.save()
                # return HttpResponse('successfully uploaded')
    #     else:
    #         form = imageform()
    #     return render(request, 'profile.html', {"form": form})
    # else:
    return render(request, 'profile.html')