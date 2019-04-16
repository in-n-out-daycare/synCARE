from django.contrib import admin
from core.models import Classroom, Guardian, Child, Visit, Activity


# Register your models here.

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    pass

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    pass

@admin.register(Child)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    pass

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass

