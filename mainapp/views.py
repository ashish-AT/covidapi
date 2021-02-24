from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import HttpResponseRedirect


# Create your views here.


def home(request):
    response = requests.get('https://api.covid19api.com/summary').json()
    # return HttpResponse(response)
    # print(response['Countries'])
    return render(request, 'home.html', {'response': response})
