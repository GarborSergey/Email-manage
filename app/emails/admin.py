from django.contrib import admin

from .models import Recipient, Company, Position


admin.site.register(Recipient)
admin.site.register(Company)
admin.site.register(Position)
