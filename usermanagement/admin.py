from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from usermanagement.models import CustomUser, WIBAdmin, Agence, Client


class UserModel(UserAdmin):
    ordering = ('email',)


admin.site.register(CustomUser, UserModel)
admin.site.register(WIBAdmin)
admin.site.register(Agence)
admin.site.register(Client)
