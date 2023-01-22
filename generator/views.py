from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user_master
from django.views.decorators.csrf import csrf_exempt
import json, random, typesense 
from faker import Faker
fake = Faker('en_US') 

'''Create your views below here.'''


# Below function will perform the Authentication with the Typesense server, 
# coz everytime you perform the operation with Typesense the autehntication is required.  
def authTypesence():
    client = typesense.Client({
        'nodes': [{
            'host': 'localhost',  # For Typesense Cloud use xxx.a1.typesense.net
            'port': '8108',       # For Typesense Cloud use port no. 443
            'protocol': 'http'    # For Typesense Cloud use https
        }],
        'api_key': 'xyz',
        'connection_timeout_seconds': 2
    })
    return client

# This function will just render the home page. i.e. index.html  
def generatorHome(request):  
    return render(request, 'generator.html')

# To create the collection in the Typesence
def createCollection(request):
    # authentication with Typesense
    client = authTypesence() 
    
    # sehema will match with your database table
    client.collections.create({
        'name': 'user_master',  # name is your database table name
        'fields': [
            {
            'name'  :  'name',
            'type'  :  'string'
            },
            {
            'name'  :  'username',
            'type'  :  'string'
            },
            {
            'name'  :  'password',
            'type'  :  'string'
            },
            {
            'name'  :  'gender',
            'type'  :  'string'
            },
            {
            'name'  :  'address',
            'type'  :  'string', 
            },
            {
            'name'  :  'mobileno',
            'type'  :  'string', 
            },
        ], 
    }) 
    
    # return message
    return HttpResponse('creatd')

# To delete the collection in the Typesence
def deleteCollection(request):
    # authentication with Typesense
    client = authTypesence()
    
    # deleting single collection from Typesence
    client.collections['user_master'].delete()

    # return message
    return HttpResponse('deleted')
    
# Search from the Typesense
@csrf_exempt
def searchTypesence(request):
    # authentication with Typesense
    client = authTypesence()
    
    # here we are getting the search parameters which we want to search
    search_parameters = {
        'q'         : request.GET.get('q'),
        'query_by'  : 'name',                   # query_by is the entity by which yo are searching, it can be changed with yuor column name.
        'per_page' : 100                        # if you are implimenting the pagination then per_page value is useful
    }
    
    # searching from the Typesense
    data = client.collections['user_master'].documents.search(search_parameters)

    # return the 'data' as a response which get by searching from the Typesense
    return HttpResponse(json.dumps(data))
    
# If you have to insert the data in bulk then this function will call 
def bulkDataGenerator(request):   
    # authentication with Typesense
    client = authTypesence()
    
    # CAUTION: while generating BE AWARE that, 
    # this operation will take time depends on how many no_of_rows you want to insert
    no_of_rows = request.POST['no_of_rows_to_generate']
    
    for i in range(int(no_of_rows)):  
        # generating all random data 
        rand_name = fake.name()
        rand_city = fake.address()
        rand_gender = random.choice(['M', 'F'])
        rand_number = random.randint(1000000000, 9999999999)
        
        # adding in the Typesense collection
        client.collections['user_master'].documents.create({
            'name': rand_name[0:10],
            'gender': rand_gender,
            'address': rand_city[0:10],
            'mobileno': str(rand_number),
        })
        
        # inserting the data in our postgresql DB
        user = user_master(name=rand_name[0:10], gender=rand_gender, mobileno=rand_number, address=rand_city[0:15])
        user.save()

    return HttpResponse('/generator')

# for single data insertion 
@csrf_exempt
def singleDataInsert(request): 
    # authentication with Typesense
    client = authTypesence()
    
    # collection all data 
    name = request.POST['name']
    gender = request.POST['gender']
    address = request.POST['addr']
    mobileno = request.POST['mobno']
     
    # insrting single data in Typesense
    client.collections['user_master'].documents.create({
        'name': name,
        'gender': gender,
        'address': address,
        'mobileno': mobileno,
    })
    
    # inserting the data in our postgresql DB
    user = user_master(name=name, gender=gender, mobileno=mobileno, address=address)
    user.save()
  
    return redirect('/generator')