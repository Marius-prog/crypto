from django.shortcuts import render

<<<<<<< HEAD

def home(request):
    # crypto prices
    price_request = requests.get(
        'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD')
    price = json.loads(price_request.content)

    # crypto news
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)

    return render(request, 'crypto_app/home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':

        quote = request.POST['quote']

        # fix all cases
        quote = quote.upper()

        crypto_request = requests.get(
            'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + quote + '&tsyms=USD')
        crypto = json.loads(crypto_request.content)

        url_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
        url = json.loads(url_request.content)

        return render(request, 'crypto_app/prices.html', {'quote': quote, 'crypto': crypto, 'url': url})

    else:
        notfound = 'Enter the crypto currency symbol into the form above..'
        return render(request, 'crypto_app/prices.html', {'notfound': notfound})
=======
# Create your views here.
>>>>>>> 120c0f35f9684e16bee3133719dcdacd961b4f9b
