from django.utils import timezone
from ipware import get_client_ip
from user_agents import parse
import pytz
from .models import UserTracking

class UserTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip, is_routable = get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        user_agent_info = parse(user_agent)

        if client_ip:
            device_info = f"{user_agent_info.browser.family} {user_agent_info.browser.version_string} on {user_agent_info.os.family} {user_agent_info.os.version_string}"
            ist = pytz.timezone('Asia/Kolkata')
            current_time = timezone.now().astimezone(ist)

            if request.user.is_authenticated:
                UserTracking.objects.create(
                    user=request.user,
                    ip_address=client_ip,
                    device=device_info,
                    timestamp=current_time
                )
            else:
                UserTracking.objects.create(
                    ip_address=client_ip,
                    device=device_info,
                    timestamp=current_time
                )

        response = self.get_response(request)
        return response
