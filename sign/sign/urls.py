from django.contrib import admin
from django.urls import path
from sign import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.animation_view,name='animation'),
    path('animation/',views.animation_view,name='animation')
]
