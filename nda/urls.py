from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

import conference_registration.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', conference_registration.views.index, name='home'),
    path('registration/', include('conference_registration.urls')),
    path('login', conference_registration.views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("__debug__/", include("debug_toolbar.urls")),
]
