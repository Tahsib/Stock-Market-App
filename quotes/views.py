from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock
from .forms import StockForm
import requests
import json
import os

API_KEY = os.getenv("API_KEY")

# Create your views here.
def home(request):
   

    if request.method == 'POST':

        ticker = request.POST['ticker'].upper()
        api_request = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=" + ticker + "&apikey=" + API_KEY )
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api':api})

    else:
        return render(request, 'home.html', {'ticker':'Enter a ticker symbol'})

def add_stock(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST["ticker"]=request.POST["ticker"].upper()
        form = StockForm(request.POST or none)
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been Added"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output=[]
        for ticker_item in ticker:
            api_request = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=" + str(ticker_item) + "&apikey=" + API_KEY )
            try:
                api = json.loads(api_request.content)
                if 'Symbol' in api:
                    output.append(api)
            except Exception as e:
                api = "Error..."
        for item in output:
            print(item)
            print()
        print()
        return render(request, 'add_stock.html',{'ticker':ticker,'output':output})
    
def about(request):
    return render(request, 'about.html', {})

def delete(request,stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request,("Stock has been deleted!"))
    return redirect(delete_stock)

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html',{'ticker':ticker})
