from django.urls import path
from . import views


urlpatterns = [
    path('', views.allblogs, name="allblogs"),
    path('<int:blog_id>', views.detail, name='detail'),
]


# import blog.views
#
# urlpatterns = [
#     path('', blog.views.allblogs, name="allblogs"),
# ]


