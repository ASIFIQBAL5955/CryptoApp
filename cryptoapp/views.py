from django.shortcuts import render
from django.http import HttpResponse
# from cryptoapp import models
from .models import Change_password
# Create your views here.

def dashboardscreen(request):
    return render(request, 'Dashboard_screen.html')

def chatscreen_Second(request):
    return render(request, 'chatscreen_second.html')
def chat_screen(request):
    return render(request, 'chat_screen.html')

def refferalscreen(request):
    return render(request, 'ReferralScreen.html')

def unstable(request):
    return HttpResponse("This Html Page is unable to load properly in Server. Please Check Server's Firewall and Forwarding Settings")

def socialaccounts(request):
    return render(request, 'SocialAccounts.html')
def changepassword(request):
    # return HttpResponse('CONTINURE YOUR WORKD')
    return render(request, 'change_password.html')

def change_pswd(request):
    print('saving data')
    Old_Password = request.POST['Old_Password']
    New_Password = request.POST['New_Password']
    Confirm_new_Password = request.POST['Confirm_new_Password']
    print(Old_Password)
    print(New_Password)
    print(New_Password)

    data = Change_password.objects.create(Old_password=Old_Password,New_password=New_Password,Confirm_new_password=New_Password)
    data.save()
    return HttpResponse('Data successfully sent to database')
  

# def chatscreen(request):
#     return render(request, 'index.html')




# def profile_Screen(request):
#     return render(request, 'index.html')


