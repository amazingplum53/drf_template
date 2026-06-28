"""
URL configuration for django_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, FileResponse

urlpatterns = [
    path('health/', lambda request: HttpResponse(status=204)),
]

if settings.STATIC_URL == "/static/":
    urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )

def frontend(request):
    return FileResponse(
        open(settings.BASE_DIR / "static" / "index.html", "rb"),
        content_type="text/html",
    )

frontend_routes = [
    path("auth/signup/", frontend),
]

urlpatterns.append(path("", include(frontend_routes)))