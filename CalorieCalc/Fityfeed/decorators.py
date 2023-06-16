from django.http import HttpResponse
from django.shortcuts import redirect


def unauthorized_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
        return wrapper_func

def allowed_users(request,allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(requet,*args,**kwargs):
            group = None
            if request.user.group.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("<h1> You are not allowed ro access this page</h1>")
            return wrapper_func
    return decorator

def admin_only(view_func):
    def warpper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'user':
            return redirect('userPage')
        if group == 'admin':
            return view_func(request,*args,**kwargs)
    return warpper_func