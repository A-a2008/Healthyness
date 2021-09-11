from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Yoga)

# Site names

admin.site.site_title = "Healthyness"
admin.site.site_header = "Healthyness Administration"
admin.site.index_title = "Healthyness Administration"
