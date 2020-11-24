from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Reg)
admin.site.register(Fill)
admin.site.register(Publication)
admin.site.register(Article)

