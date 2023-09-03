from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tournamentapp.urls')) #os urls da api ficam no 'localhost', logo quando o iniciamos
]
