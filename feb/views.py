from django.shortcuts import render

# Create your views here.
def Feb(request):
    return render(request, 'feb.html')