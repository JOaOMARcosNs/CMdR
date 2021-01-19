from django.contrib import admin
from register.models import Nationality, About
# Register your models here.

class Show_about(admin.ModelAdmin):
    list_display = ('id','description','history', 'sexual_orientation', 'breed', 'school_level')
    list_filter = ('id', 'description', 'breed', 'school_level')

class Show_nationality(admin.ModelAdmin):
    list_display = ('city', 'state')
    list_filter = ('city', 'state')



admin.site.register(Nationality, Show_nationality)
admin.site.register(About, Show_about)