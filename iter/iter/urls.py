"""iter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)

from user_authentication import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userauth/', include('user_authentication.urls')),
    path('hotel_vendor/', include('hotel_vendor.urls')),
    path('bus_vendor/', include('bus_vendor.urls')),

#    path('hotelbooking/',include('hotel_booking.urls')),
#    path('busbooking/',include('bus_booking.urls')),
#    path('tripplanner/', include('trip_planner.urls')),
    path('signup/',views.signup,name="signup"),
    path('login/',views.user_login,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user_authentication/home.html'),name='logout'),
    path('reset-password/', PasswordResetView.as_view(template_name='user_authentication/password_reset_form.html',
                                                        email_template_name="user_authentication/reset_password_email.html",
                                                        success_url="done/"), name="password_reset"),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='user_authentication/password_reset_done.html'),
        name="password_reset_done"),
    path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
        PasswordResetConfirmView.as_view(template_name="user_authentication/password_reset_confirm.html"),
        name="password_reset_confirm"),
    path(r'reset-password/complete/',
        PasswordResetCompleteView.as_view(template_name="user_authentication/password_reset_complete.html"),
        name="password_reset_complete"),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
