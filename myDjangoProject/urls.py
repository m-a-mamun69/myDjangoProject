from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('basicApp/', include('basicApp.urls')),
    path('admin/', admin.site.urls),
]