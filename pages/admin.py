from django.contrib import admin
from .models import ContactMessage, Skill

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'message')

@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_on_homepage')