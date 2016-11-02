from django.contrib import admin

from shopper_app.models import User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

admin.site.register(User, UserAdmin)
