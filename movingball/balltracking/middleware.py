from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve

class CustomLoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            # import pdb;pdb.set_trace()
            current_url = resolve(request.path_info).url_name
            if current_url != 'login':
                return redirect('http://127.0.0.1:8000/balltracking/login/')
        response = self.get_response(request)
        return response
