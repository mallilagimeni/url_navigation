from django.shortcuts import render

# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')

def hitman(request):
    return render(request,'hitman.html')