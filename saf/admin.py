from re import search
from django.contrib import admin
from saf.models import Users, Roles, Claims


class AdminUsers(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 5


class AdminClaims(admin.ModelAdmin):
    list_display = ('id', 'descricao')


class AdminRoles(admin.ModelAdmin):
    list_display = ('id', 'description')


admin.site.register(Users, AdminUsers)
admin.site.register(Roles, AdminRoles)
admin.site.register(Claims, AdminClaims)
