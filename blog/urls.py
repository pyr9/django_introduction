

from django.urls import path
import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('article', blog.views.article_content),
    path('index', blog.views.get_index_page),
    path('detail/<int:id>', blog.views.get_detail_page)
]