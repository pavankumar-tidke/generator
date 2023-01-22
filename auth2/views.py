from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse  
from generator.models import user_master
import json, random, typesense 
from faker import Faker
from datagenerate.globals import GLOBALS
from argon2 import PasswordHasher
ph = PasswordHasher()

GB = GLOBALS()

# Create your views here.

class Auth2 :

    # user login & signup page
    def AuthPage(request) :
        if ('user_details' in request.session) :
            return redirect('dashboard/') 
        return render(request, 'index.html')
    
    @csrf_exempt
    # user Authentication sign up & sign in action
    def AuthenticateUser(request) : 
        # authentication with Typesense
        client = GB.typesenceAuth()  
        
        username = request.POST.get('username')

        if request.POST.get('operation')  == 'signup' : 
            # collecting all data  
            name = request.POST.get('name')    
            email = request.POST.get('email')    
            hash = ph.hash(request.POST.get('password')) 
            gender = GB.randomGender()
            address = GB.randomAddress()
            mobileno = GB.randomMobileNo() 
 
            # searching username from the PostgreSQl DB
            if user_master.objects.filter(username=username).exists() == False :
               
                # insrting single data in Typesense
                client.collections['user_master'].documents.create({
                    'username': username, 
                    'name': name, 
                    'email': email, 
                    'password': hash, 
                    'gender': gender,      
                    'address': address,      
                    'mobileno': mobileno,      
                })
                
                # # inserting the data in our postgresql DB
                user_master(
                    name=name, 
                    username=username, 
                    email=email, 
                    password=hash, 
                    gender=gender, 
                    mobileno=mobileno, address=address).save()
                
                GB.setSession(request, {'name': name, 'username': username, 'email': email})
                
                return HttpResponse(json.dumps({'success': True, 'error': {'errorMsg': None, 'error': False}, 'data': {'redirect': True, 'redirect_url': '/dashboard'}}))
                # return HttpResponse(json.dumps({'successMsg': 'Account Created !', 'errorMsg': None, 'error': False, 'data': data}))
                
            else :
                return HttpResponse(json.dumps({'success': None, 'errorMsg': 'Username Exists !', 'error': True, 'data': None}))
            
        else :  
            # user login logic  
            if user_master.objects.filter(username=username).exists() :
                user = user_master.objects.get(username=username)
                if ph.verify(user.password, request.POST.get('password')) :
                    GB.setSession(request, {'name': user.name, 'username': username, 'email': user.email})
                    return HttpResponse(json.dumps({'success': True, 'errorMsg': None, 'error': False, 'data': {'redirect_url': '/dashboard'}}))                    
                else :
                    return HttpResponse(json.dumps({'success': None, 'errorMsg': 'Invalid Credentials !', 'error': True, 'data': None}))
            else : 
                return HttpResponse(json.dumps({'success': None, 'errorMsg': 'Invalid Credentials !', 'error': True, 'data': None})) 
        

    # logout 
    def logout(request) :
        GB.sessionDestroy(request)
        return redirect('')