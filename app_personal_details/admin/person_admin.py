from django.contrib import admin
from ..models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'middle_name', 'maiden_name', 'marital_status', 'dob', 'gender', 'occupation', 'qualification', 'person_type', 'deceased']
    search_fields = ['first_name', 'last_name']
    fieldsets = (
        (None, {
            "fields": (
                'last_name', 'first_name',
                'middle_name', 'maiden_name',
                'marital_status', 'dob', 'gender',
                'occupation', 'qualification', 'person_type',
                'deceased'
            ),
        }),
    )


admin.site.register(Person, PersonAdmin)