from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import csv
from .models import MyModel
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dishes(request):
    data = MyModel.objects.all()
    params = {'data': data}
    return render(request, 'dishes.html', params)

def search(request):
    query = request.GET['search']
    dataName = MyModel.objects.filter(name__icontains=query)
    dataLocation = MyModel.objects.filter(location__icontains=query)
    data = dataName.union(dataLocation)
    
    params = {'data': data, 'query': query}
    return render(request, 'search.html', params)


def items(request):
    query = request.GET.get('items', None)
    data = MyModel.objects.filter(name__icontains=query)
    params = {'data': data}
    return render(request, 'items.html', params)

# def csv_data(request):
#     data = MyModel.objects.all()
#     params = {'data': data}
#     return render(request, 'dishes.html', params)


### code to import data into model ###

# def csv_to_model(request):
#     with open('static/restaurants_small.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header row if it exists
#         for row in reader:
#             item_dict = json.dumps(row[3])
#             MyModel.objects.create(
#                 # id=row[0],
#                 name=row[1],
#                 location=row[2],
#                 item = item_dict,
#                 # Assign other fields from row as needed
#             )
    
    # print(data)
       
    
