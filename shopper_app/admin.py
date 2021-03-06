from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token

from shopper_app.models import User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.unregister(Token)
