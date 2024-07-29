from  django.urls import path 
from . import views 



# URLConf module or url configuration for this particular application 
# and every application can have its own url configuration and we need to import this into the main configuration url for this project 

urlpatterns = [ 

    path('hello/',views.say_hello)
]