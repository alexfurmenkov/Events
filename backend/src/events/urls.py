from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/signup/', SignUp.as_view(),
         name='signup'),
    path('users/login/', Login.as_view(),
         name='login'),

    path('posts/', PostHandler.as_view(),
         name='save_post_or_get_all'),
    path('posts/<int:post_id>/', PostByIdHandler.as_view(),
         name='get_post_by_id_or_edit'),
    path('posts/find/', PostsFilteredHandler.as_view(),
         name='get_posts_filtered'),
]
