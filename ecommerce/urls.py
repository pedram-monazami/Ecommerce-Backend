"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

# The urls of the main app.

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('landing.urls')),
                  path('api/order/', include('order.urls')),
                  path('api/product/', include('product.urls')),
                  path('api/customer/', include('customer.urls')),
                  path('login', TokenObtainPairView.as_view(), name='login'),
                  path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
                  path('logout', TokenBlacklistView.as_view(), name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
