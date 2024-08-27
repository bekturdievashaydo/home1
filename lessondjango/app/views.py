from django.shortcuts import HttpResponse
from django.shortcuts import render
# Create your views here.
def Homepage(requests):
    # return HttpResponse('bu bosh sahifa')
    return render(requests, template_name="home.html")