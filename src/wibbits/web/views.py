from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

import json

from web.models import Brand, Subscribers, Feature, Video, Testimonial, MarketingFeature, Products, Blogs, Contact
from django.http.response import HttpResponse
from web.forms import ContactForm


def index(request):
    Brands = Brand.objects.all()
    Last_Brands = Brand.objects.all()[:4]
    Features = Feature.objects.all()
    Videos = Video.objects.all()[:3]
    Testimonials = Testimonial.objects.all()
    Marketing = MarketingFeature.objects.all()
    Product = Products.objects.all()
    Blog = Blogs.objects.all()
    Contacts = Contact.objects.all() 

    form = ContactForm()
    
    context = {
        "brands": Brands,
         "features" : Features,
         "videos" : Videos,
         "testimonials" : Testimonials,
         "marketing" : Marketing,
         "products" : Product,
         "blogs" : Blog,
         "contacts" : Contacts,
         "form" : form,
         "last_brands" : Last_Brands,
    }
    return render(request,"index.html",context=context)


def subscribers(request):
    email = request.POST.get("email")

    if not Subscribers.objects.filter(email=email).exists():

        Subscribers.objects.create(
            email = email
        )

        response_data = {
            "status": "success",
            "title": "Successfully Registered",
            "message": "You subscribed to our newsletter successfully."
        }

    else:
         response_data = {
            "status": "error",
            "title": "You are already  Registered",
            "message": "You are already a member."
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()

        response_data = {
            "status": "success",
            "title": "Successfully Registered",
            "message": "You subscribed to our newsletter successfully."
        }

    else:
         response_data = {
            "status": "error",
            "title": "You are already  Registered",
            "message": "You are already a member."
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript") 


def product(request,pk):
    product = get_object_or_404(Products.objects.filter(pk=pk))
    
    brands = Brand.objects.filter(product=product) 

    context = {
        "product" : product,
        "brands" : brands
    }
    return render(request,"product.html",context=context)