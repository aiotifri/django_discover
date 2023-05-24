
from django.contrib import admin
from django.urls import path, include

from home.views import index, generate_blague

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("home.urls")),

]
