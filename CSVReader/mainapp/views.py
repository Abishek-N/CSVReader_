import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from mainapp.models import CSVData
# Create your views here.

#To render the index page for the base url
def index(request):
    #read the data from model and store in variable to pass to the index page
    table_data = CSVData.objects.order_by('id')
    my_dict = {'table_data' : table_data}
    return render(request, 'index.html', context=my_dict)

#method to update the values of database using csv file
def update(request):
    my_dict={}
    #redirect if the request is get
    if request.method == "GET":
        return render(request, 'index.html', context=my_dict)
    #store the file
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,"The File uploaded is not a CSV file")
        return render(request, 'index.html', context=my_dict)
    values = csv_file.read().decode('UTF-8')
    #convert the files to string
    string = io.StringIO(values)
    next(string)
    for value in csv.reader(string, delimiter=',', quotechar='|'):
        #update the data into the db
        _,created = CSVData.objects.update_or_create(
            id=int(value[0]),
            firstname=value[1],
            lastname=value[2],
            email=value[3],
            password=value[4],
            profession=value[5]
        )
    table_data = CSVData.objects.order_by('id')
    my_dict = {'table_data': table_data}
    return render(request,'index.html',my_dict)