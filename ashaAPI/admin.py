from django.contrib import admin
from .models import CarouselImage,TeacherCard,ContactRequest,CVSubmission,Subject
# Register your models here.
admin.site.register((CarouselImage,ContactRequest,Subject))



class CVSubmissionAdmin(admin.ModelAdmin):
    list_display = ('sno','name','email')



admin.site.register(CVSubmission,CVSubmissionAdmin)

@admin.register(TeacherCard)
class DescriptionAdminMCE(admin.ModelAdmin):
    list_display = ('sno','name','facultySubject','isInManagement')

    
