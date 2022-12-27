from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboardscreen(request):
    return render(request, 'Dashboard_screen.html')

def chatscreen_Second(request):
    return render(request, 'chatscreen_second.html')

def refferalscreen(request):
    return render(request, 'ReferralScreen.html')

def unstable(request):
    return HttpResponse("This Html Page is unable to load properly in Server. Please Check Server's Firewall and Forwarding Settings")

def socialaccounts(request):
    return render(request, 'SocialAccounts.html')
# def changepassword(request):
#     return HttpResponse('CONTINURE YOUR WORKD')
# def chatscreen(request):
#     return render(request, 'index.html')




# def profile_Screen(request):
#     return render(request, 'index.html')


