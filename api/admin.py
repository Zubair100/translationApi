from django.contrib import admin

from .models import Animal

from .models import ProtectionStatus

admin.site.register(Animal)
admin.site.register(ProtectionStatus)

# Register your models here.
