from django.contrib import admin


from web.models import Blogs, MarketingFeature, Products, Subscribers, Brand, Feature, Testimonial, Video, Contact


class BrandAdmin(admin.ModelAdmin):
    list_display = ["id","image"]


admin.site.register(Subscribers)


admin.site.register(Brand, BrandAdmin)

admin.site.register(Feature)

admin.site.register(Video)

admin.site.register(Testimonial)

admin.site.register(MarketingFeature)

admin.site.register(Products)

admin.site.register(Blogs)

admin.site.register(Contact)