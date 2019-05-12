
from django.contrib import admin
from django.urls import path, include
import game.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game.views.start, name="start"),
    path('game/', include('game.urls')),
 
  
]
