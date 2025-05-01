from django.contrib import admin
from django.urls import path, include  # ADICIONE o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nomes.urls')),  # ADICIONE esta linha
]
