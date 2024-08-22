from django.contrib import admin
from .models import Group, Event, Message


admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Message)
