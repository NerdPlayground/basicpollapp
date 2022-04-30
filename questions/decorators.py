from django.http import HttpResponse

def is_manager(func):
    def inner(*args,**kwargs):
        request= args[0] or kwargs["request"]
        if not request.user.is_manager:
            return HttpResponse("Warning: You are not allowed to view this page.")
        return func(*args,**kwargs)
    return inner