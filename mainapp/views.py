import datetime
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


def page2(request):
    time1 = datetime.datetime.now() - 1
    time2 = datetime.datetime.now()

    page_data = requests.get(
        f'https://api.covid19api.com/country/south-africa/status/confirmed?from={time1}&to={time2}').json()
    return render(request, 'home.html', {'response': page_data})
