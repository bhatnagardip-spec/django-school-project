from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import ItemList, Items, AboutUs, ContactUs, Slider, Testimonial

# Create your views here.
def HomeView(request):
     items = Items.objects.all()
     list = ItemList.objects.all()
     data = AboutUs.objects.all()
     slider = Slider.objects.all()
     testimonial = Testimonial.objects.all()
     contact = ContactUs.objects.all()
     return render(request,'home.html',{'items': items, 'list': list,'data': data,'slider': slider,'testimonial': testimonial,'contact': contact})



def AboutView(request):
     data = AboutUs.objects.all()
     contact = ContactUs.objects.all()
     return render(request,'about.html',{'data': data,'contact': contact})

def ServiceView(request):
     return render(request,'service.html')


def CourseView(request):
     items = Items.objects.all()
     list = ItemList.objects.all()
     contact = ContactUs.objects.all()
     return render(request,'course.html',{'items': items, 'list': list,'contact': contact})

def ContactView(request):
     contact = ContactUs.objects.all()
     return render(request,'contact.html',{'contact': contact})