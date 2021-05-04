from django.shortcuts import render
import requests
import json


def home(request):
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)

    return render(request, 'crypto_app/home.html', {'api': api})
