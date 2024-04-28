from django.shortcuts import render

def home(request):
    return render(request,'SnapchatCampaigns/base.html')
# oauth2 for snapchat
# https://accounts.snapchat.com/accounts/oauth2/auth?client_id=221d959d-1dc6-4740-8e0e-2675ced3b530&redirect_uri=https://web-production-831b6.up.railway.app/&response_type=code&scope=snapchat-marketing-api
