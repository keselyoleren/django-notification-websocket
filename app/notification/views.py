from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from notification.models import Notifications
# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return HttpResponse("success")
    return render(request, 'index.html')

def notification(request):
    notif = Notifications.objects.all()
    context = {
        'notif':notif
    }

    return render(request, 'notification.html', context)
