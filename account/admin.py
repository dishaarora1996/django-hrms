from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
   
    list_display = ('email', 'name', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'name',)
    # readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ['email']

    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'name', 'designation', 'role', 'password1', 'password2'),
    }),
)



# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(Role)