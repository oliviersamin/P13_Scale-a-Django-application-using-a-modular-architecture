from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'oc_lettings_site'



urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', views.trigger_error),
]
