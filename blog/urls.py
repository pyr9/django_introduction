

from django.urls import path
import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world)
]