"""otter_habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from core import views as habit_views

urlpatterns = [
    path('', habit_views.home, name='home'),
    path('habits/', habit_views.list_habits, name='list_habits'),
    path('habits/add/', habit_views.add_habit, name='add_habit'),
    path('habits/<int:pk>/<int:month>/<int:day>/<int:year>/add_record', habit_views.add_record, name='add_record'),
    path('habits/<int:pk>/add_record', habit_views.add_record, name='add_record'),
    path('habits/<int:pk>/', habit_views.show_habit, name = 'show_habit'),
    path('habits/<int:pk>/edit/', habit_views.edit_habit, name='edit_habit'),
    path('habits/<int:pk>/delete/', habit_views.delete_habit, name='delete_habit'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
