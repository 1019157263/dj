from django.contrib import admin

# Register your models here.
from .models import Question,Choice,user
#from .models import Choice

#admin.site.register(Choice)

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(user)