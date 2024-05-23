from django.shortcuts import redirect

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return redirect('login')  # Redirect to login page or access denied page
        return view_func(request, *args, **kwargs)
    return _wrapped_view
