from django.contrib import admin

# Register your models here.
from openHands.models import Post, CustomerReview

admin.site.register(Post)
admin.site.register(CustomerReview)