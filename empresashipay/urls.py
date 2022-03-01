
from django.contrib import admin
from django.urls import path, include
from saf.views import UsersviewSet, RolesviewSet, ClaimviewSet, ListaPapelUsuarioviewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('TodosUsuarios', UsersviewSet, basename='Usuarios')
router.register('roles', RolesviewSet, basename='roles')
router.register('claims', ClaimviewSet, basename='claims')
router.register('UsuariosFuncao', ListaPapelUsuarioviewSet,
                basename='UsuariosFuncao')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
   


]
