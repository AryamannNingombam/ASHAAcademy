from django.contrib import admin
from .models import CarouselImage,TeacherCard,TeacherImage
# Register your models here.
admin.site.register((CarouselImage,TeacherImage))





@admin.register(TeacherCard)
class DescriptionAdminMCE(admin.ModelAdmin):
    class Media:
        js = ('/static/scripts/TinyMCE.js',)
    list_display = ('sno','name','facultySubject','isInManagement')

    
