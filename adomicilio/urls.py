"""adomicilio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from myapps.buscar import views 

from django.conf.urls import handler404, handler500
from myapps.home.views import mi_error_404, error_404
 
handler404 = error_404
# handler500 = error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),
    path('', include('myapps.home.urls')),
    path('cuentas/', include('myapps.cuentas.urls')),
    path('categorias/', include('myapps.categorias.urls')),
    path('ofertas/', include('myapps.ofertas.urls')),
    path('contratos/', include('myapps.contratos.urls')),
    path('buscar/', include('myapps.buscar.urls')),
    path('buscar_trabajadores/', include('myapps.trabajadores.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# let's keep this, just in case
# settings.STATIC_URL, document_root=settings.STATIC_ROOT)
