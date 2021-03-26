from django.contrib import admin
from .models import CarouselImage,ContactRequest,CVSubmission,Subject
# Register your models here.
admin.site.register((CarouselImage,Subject))


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name','email','phoneNumber')

class CVSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name','email')


admin.site.register(ContactRequest,ContactRequestAdmin)

admin.site.register(CVSubmission,CVSubmissionAdmin)

# @admin.register(TeacherCard)
# class DescriptionAdminMCE(admin.ModelAdmin):
#     list_display = ('name','facultySubject','isInManagement')
#
#
