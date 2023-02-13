from distutils.command.upload import upload
import email
import json

from django.db import models
from django.forms import BooleanField


class Subscribers(models.Model):
    email = models.EmailField()


    def __str__(self):
        return self.email


class Brand(models.Model):
    product = models.ForeignKey("web.products",on_delete=models.CASCADE)
    image = models.FileField(upload_to="brands/")
    white_image = models.FileField(upload_to="brands/",blank=True,null=True)


    def __str__(self):
        return json.dumps(self.pk)


class Feature(models.Model):
    image = models.ImageField(upload_to="features/")
    icon = models.FileField(upload_to="features/")
    icon_background = models.CharField(max_length=256,blank=True,null=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length=256)
    author_designation = models.CharField(max_length=256)
    testimonial_logo = models.FileField(upload_to="features/")


    class Meta:
        db_table = "web_feature"
        ordering = ["-id"]

    def __str__(self):
        return self.title


class Video(models.Model):
    bg_image= models.ImageField(upload_to="video/")
    play_image= models.FileField(upload_to="video/")
    title = models.CharField(max_length=256)
    logo = models.FileField(upload_to="video/")


    class Meta:
        db_table = "web_video"
        ordering = ["-id"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/")
    logo = models.FileField(upload_to="testimonial/",blank=True,null=True)
    description = models.TextField()
    name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    company_name = models.CharField(max_length=256)
    # is_featured = models.BooleanField(default=False)


    class Meta:
        db_table = "web_testimonial"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)


class MarketingFeature(models.Model):
    image = models.FileField(upload_to="marketing/")
    title = models.CharField(max_length=256)
    description = models.TextField()

    class Meta:
        db_table = "web_marketing"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)


class Products(models.Model):
    logo = models.FileField(upload_to="products/")
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    bg_color = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    hero_image = models.ImageField(upload_to="products/")


    class Meta:
        db_table = "web_products"
        ordering = ["id"]

    def __str__(self):
        return str(self.id)


CONTENT_TYPE = (
    ("blog_post", "Blog Post"),
    ("webinar", "Webinar"),
    ("report", "Report"),
)


class Blogs(models.Model):
    image = models.ImageField(upload_to="blogs/")
    title = models.CharField(max_length=256)
    content_type = models.CharField(max_length=256,choices=CONTENT_TYPE)


    class Meta:
        db_table = "web_blogs"
        ordering = ["id"]

    def __str__(self):
        return str(self.id)


COMPANY_SIZE = (
    ("1","1-10"),
    ("2","11-50"),
    ("3","51-200"),
    ("4","201-500"),
)

INDUSTRY = (
    ("1","Agriculture"),
    ("2","Banking & Finance"),
    ("3","Business Services & Software"),
)

JOB_ROLE = (
    ("1","C-Suite"),
    ("2","VP"),
)

COUNTRY = (
    ("US","United States"),
    ("albania","Albania"),
)

class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    company_size = models.CharField(max_length=128,choices=COMPANY_SIZE)
    industry = models.CharField(max_length=128,choices=INDUSTRY)
    job_role = models.CharField(max_length=128,choices=JOB_ROLE)
    country = models.CharField(max_length=128,choices=COUNTRY)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        db_table = "web:contact"
        ordering = ["id"]

    def __str__(self):
        return self.first_name