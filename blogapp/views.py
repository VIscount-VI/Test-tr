from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Name
from django.urls import reverse_lazy
# Create your views here.








def Index(request):
    text = request.GET.get('text', 'text',)
    if text and text != '' :
        data = Name.objects.filter(first_name__contains = text).all()[:2]
    else :
        data = None
    return render(request,  'o1.html', {'text'  :  text,  'data' : data})
def Index_2(request):
    text = request.GET.get('text', 'text',)
    if text and text != '' :
        data = Name.objects.filter(last_name__contains = text).all()[:2]
    else :
        data = None
    return render(request,  'o2.html', {'text'  :  text,  'data' : data})
class createlist(CreateView):
    model = Name
    template_name = 'list.html'
    fields = ('first_name', 'last_name')
    success_url = reverse_lazy('save')

def Save(request):
    return render(request, 'save.html',)