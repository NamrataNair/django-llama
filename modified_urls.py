# this the modified URLS.py
# this is to ensure that the URL pattern for gradio is present 

from django.contrib import admin
from django.urls import path
from myapp.views import gradio_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gradio/', gradio_view),
]
