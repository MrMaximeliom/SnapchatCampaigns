from django.shortcuts import render
from SnapchatCampaigns.constants import SweetAlertIcons
from SnapchatCampaigns.sweet_alert_message import SweetAlertMessage
from django.contrib import messages

def home(request):
    context = {
        'title':"Home",
    }
    if 'message' in request.session:
        message = request.session.pop('message', None)
        context['message'] = message

    return render(request,'home/home.html',context)
# oauth2 for snapchat
# https://accounts.snapchat.com/accounts/oauth2/auth?client_id=221d959d-1dc6-4740-8e0e-2675ced3b530&redirect_uri=https://web-production-831b6.up.railway.app/&response_type=code&scope=snapchat-marketing-api
