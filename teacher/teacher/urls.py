"""teacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tax import views as tax_views
from tax.tax_views import teacherView
urlpatterns = [
    url(r'^success/$', tax_views.success,name = 'success'),
    url(r'^error/$', tax_views.error,name = 'error'),
    url(r'^teacher/add/$',teacherView.AddTeacher.as_view(), name = 'addteacher'),
    url(r'^hello/',tax_views.hello),
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', tax_views.test),

]
