from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# a view function is a function that takes a request and return a response . 
# in archtiecture way  , a view is something that user can see but that's not the case here in django it's called template . 

# so let's create our first view or request handler or action or a view in django 
# don't forget a view is a function that takes request and return a response . 


# let's generate a random dynamic value 



def say_hello(request):

    return render(request, 'hello.html', {'name':'BARRY'})


