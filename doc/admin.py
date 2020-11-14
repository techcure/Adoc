from django.contrib import admin

# Register your models here.
from .models import Reg
from .models import Person
from .models import Group
from .models import Membership
from .models import *


admin.site.register(Reg)
admin.site.register(Person)
admin.site.register(Group)
