from django.contrib import admin
from register.models import Nationality, About, Homeless, Addiction, Disease
# Register your models here.

class Show_about(admin.ModelAdmin):
    list_display = ('id','description','history', 'sexual_orientation', 'breed', 'school_level')
    list_filter = ('id', 'description', 'breed', 'school_level')

class Show_nationality(admin.ModelAdmin):
    list_display = ('city', 'state')
    list_filter = ('city', 'state')

class Show_homeless(admin.ModelAdmin):
    list_display = ('id', 'frist_name', 'second_name', 'cpf', 'rg')
    list_filter = ('id', 'frist_name', 'second_name', 'cpf', 'rg')

class Show_addiction(admin.ModelAdmin):
    list_display = ('id', 'name_addiction', 'type_addiction')
    list_filter = ('id', 'name_addiction', 'type_addiction')

class Show_Disease(admin.ModelAdmin):
    list_display = ('id', 'name_disease', 'type_disease')
    list_filter = ('id',  'name_disease', 'type_disease')


admin.site.register(Nationality, Show_nationality)
admin.site.register(About, Show_about)
admin.site.register(Homeless, Show_homeless)
admin.site.register(Addiction, Show_addiction)
admin.site.register(Disease, Show_Disease)