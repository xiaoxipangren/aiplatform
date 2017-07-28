from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Regex)
admin.site.register(Vocab)
admin.site.register(Intent)
admin.site.register(Skill)
admin.site.register(App)

