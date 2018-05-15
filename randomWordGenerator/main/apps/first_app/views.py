from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'first_app/index.html')

def random(request):
    request.session['word'] = get_random_string(length=14)
    # print(word)
    if 'count' not in request.session:
            request.session['count'] = 1
    else:
        request.session['count'] += 1
    return redirect('/')

def reset(request):
    request.session['count'] = 0
    # print('hellooo')
    return redirect('/')
