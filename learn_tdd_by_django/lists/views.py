from django.shortcuts import render
from django.http import HttpResponse
# home_page = None


def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    return render(request, 'home.html')
