from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', 
#     domain=None, secure=None, httponly=False, samesite=None)
def cookie(request):
    print(request.COOKIES)
    resp = HttpResponse('C is for cookie and that is good enough for me...')
    resp.set_cookie('zap', 42) # No epired data = until browser close
    resp.set_cookie('sakaicar', 42, max_age=1000) # seconds until expire
    return resp

def sessfun(request) :
    context = {'zap' : '42' }
    return render(request, 'guess.html', context)

# https://www.youtube.com/watch?v=Ye8mB6VsUHw