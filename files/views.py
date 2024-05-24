from django.conf import settings
from django.shortcuts import render
from .models import subject, pdf
from django.http import HttpResponse
from .decorators import admin_required

# Create your views here.
def home(request):
    sub = subject.objects.all()
    return render(request, 'files/home.html', {'sub':sub})

def main(request, name):
    nme = subject.objects.get(sub_name=name)
    return render(request, 'files/main.html', {'nme':nme, 'pdf':pdf})

@admin_required
def track_user_view(request):
    client_ip = request.client_ip
    user_agent_info = request.user_agent_info

    # Log or save this information as needed
    print(f'Client IP: {client_ip}')
    print(f'User Agent: {user_agent_info}')

    context = {
        'client_ip': client_ip,
        'user_agent_info': user_agent_info,
    }

    return render(request, 'files/your_template.html', context)
