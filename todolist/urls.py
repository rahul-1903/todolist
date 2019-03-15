from django.contrib import admin
from django.urls import path, include
from todos import views

urlpatterns = [
    path('', include('todos.urls')),
    path('todos/', include('todos.urls')),
    path('admin/', admin.site.urls),
]
