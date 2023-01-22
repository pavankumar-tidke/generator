from django.shortcuts import render, redirect

# Create your views here.

class Dashboard :
    
    # dashboard index page
    def homePage(request) :
        return render(request, 'dashboard.html') 
    
    