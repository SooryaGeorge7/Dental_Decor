
from django.shortcuts import render

# Create your views here.
def view_shoppingbag(request):
    
    return render(request, 'shoppingbag/shoppingbag.html')