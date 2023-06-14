from django.contrib import admin
from .models import Person, Group, Membership

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'group', 'date_joined', 'invite_reason']
