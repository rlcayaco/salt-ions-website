"""salt_ions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf import settings 
from django.conf.urls.static import static 

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path, include 
from main_app.views import LandingPageView, CompanyProfileView, contact, landing_page, ProductView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    # path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    # we used template_name inside LogoutView.as_view so Django will not point out to its default 'registration/logout.html'
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    path('company_profile/', CompanyProfileView.as_view(), name='company_profile'),
    path('products/', ProductView.as_view(), name='products'),
    path('contact_us/', contact, name='contact_us'),
    path('project_list/', include('main_app.urls', namespace='projects')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
