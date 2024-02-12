from django.contrib import admin
from .models import (Scheduler,personalCV,Education,Work,Skils )

# Register your models here.
admin.site.register(Scheduler)
admin.site.register(personalCV)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Skils)
