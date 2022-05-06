from django.contrib import admin
from .models import *

admin.site.register(category)
admin.site.register(product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(orderitem)
admin.site.register(Profile)



