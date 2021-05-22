from django.shortcuts import render, HttpResponse

# Create your views here.
def testing(request):
    return render(request, 'test.html', {})