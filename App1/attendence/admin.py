from django.contrib import admin

# Register your models here.

from .models import *


# Registration of all Models

admin.site.register(Type)
admin.site.register(Faculty)
admin.site.register(LoginAuthKey)
admin.site.register(Publications)
admin.site.register(Workshops)
admin.site.register(FacultyQualification)
admin.site.register(ResearchPaper)
admin.site.register(SessionChair)
admin.site.register(WorkExperience)
admin.site.register(AreaOfSpecialisation)
admin.site.register(AcademicRole)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Fcs)
admin.site.register(Fcss)
admin.site.register(Attendance)
admin.site.register(Tests)
admin.site.register(Test_res)
