from django.contrib import admin
from choices.models import Choice

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display= ["id","question","body","votes"]
    readonly_fields= ["votes"]
    list_filter= ["question"]