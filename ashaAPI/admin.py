from django.contrib import admin
from .models import CarouselImage,TeacherCard,TeacherImage,ContactRequest
# Register your models here.
admin.site.register((CarouselImage,TeacherImage,ContactRequest))





@admin.register(TeacherCard)
class DescriptionAdminMCE(admin.ModelAdmin):
    class Media:
        js = ('/static/scripts/TinyMCE.js',)
    list_display = ('sno','name','facultySubject','isInManagement')

    
