from django.urls import path
from . import views

#URLConf
urlpatterns = [
    
    # User login / signup page route
    path(route='', view=views.Auth2.AuthPage),

    # User Autentication route
    path(route='authenticateUser/', view=views.Auth2.AuthenticateUser)
    
]