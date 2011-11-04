from django.contrib import admin
from thyroid.models import Reference, Category, Diagnosis

#admin.site.register(Reference)
admin.site.register(Category)
#admin.site.register(Diagnosis)

class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('text', 'category')
    ordering = ('category',)

admin.site.register(Diagnosis, DiagnosisAdmin)

class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

admin.site.register(Reference, ReferenceAdmin)
