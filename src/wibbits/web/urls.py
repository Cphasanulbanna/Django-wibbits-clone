from django.urls import path
from web.views import index, subscribers, contact, product


app_name = "web"
urlpatterns = [
    path("",index,name="index"),
    path("subscribers/",subscribers,name="subscribers"),
    path("contact/",contact,name="contact"),
    path("product/<int:pk>/", product, name="product")
]
