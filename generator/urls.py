from django.urls import path
from . import views

#URLConf
urlpatterns = [
    
    # Simple home page
    path(route='', view=views.generatorHome),

    # single person data insertion
    path(route='insertData/', view=views.singleDataInsert),

    # for generating data in bulk
    path(route='bulkDataGenerator/', view=views.bulkDataGenerator),

    # creating the collection in the Typpesense
    path(route='createCollection/', view=views.createCollection),

    # deleting the collection from the Typpesense
    path(route='deleteCollection/', view=views.deleteCollection),

    # for searching the query
    path(route='search/', view=views.searchTypesence),
] 