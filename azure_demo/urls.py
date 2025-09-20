from django.contrib import admin
from django.urls import path
from home.views import upload_file

urlpatterns = [
path('admin/', admin.site.urls),
path('', upload_file),
]