"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path("admin/", admin.site.urls)]

urlpatterns += [path("catalog/", include("catalog.urls"))]

urlpatterns += [path("", RedirectView.as_view(url="/catalog/"))]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# NEW 5
# The following automatically includes the following URL routes:
#
#   accounts/ login/ [name='login']
#   accounts/ logout/ [name='logout']
#   accounts/ password_change/ [name='password_change']
#   accounts/ password_change/done/ [name='password_change_done']
#   accounts/ password_reset/ [name='password_reset']
#   accounts/ password_reset/done/ [name='password_reset_done']
#   accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
#   accounts/ reset/done/ [name='password_reset_complete']
#
# They also expect you to provide a number of templates that the
# authentication framework expects. These are:
#
#   registration/login.html
#   registration/logged_out.html
#   registration/password_reset_form.html
#   registration/password_reset_done.html
#   registration/password_reset_email.html
#   registration/password_reset_confirm.html
#   registration/password_reset_complete.html
#
#
urlpatterns += [path("accounts/", include("django.contrib.auth.urls"))]
