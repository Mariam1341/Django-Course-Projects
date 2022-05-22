from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('<h1>This is your home</h1>')


def cv(request):
        context = {
            'name': 'Mariam Mohamed',
            'age': 20,
            'education':'Engneering electrical department computer engneering and systems',
            'language': 'Arabic - English - Duetch',
            'job': "Student"

        }
        return render(request, 'proFile/cv.html', context =  context)

def friend_cv(request):
    context = {
        'name': 'Basma Mohamed',
        'age': 20,
        'education': 'Engneering archtic department',
        'language': 'Arabic - English - French',
        'job': "Student"

    }
    return render(request, 'proFile/friend_cv.html', context= context )

def index(request):
    return render(request,'proFile/index.html')