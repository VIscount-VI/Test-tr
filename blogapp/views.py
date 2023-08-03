from django.shortcuts import render
from django.http import HttpResponse
from .models import Name
# Create your views here.








def Index(request):
    text = request.GET.get('text', 'text',)
    if text and text != '' :
        data = Name.objects.filter(first_name__contains = text).all()[:2]
    else :
        data = None
    return render(request,  'o1.html', {'text'  :  text,  'data' : data})