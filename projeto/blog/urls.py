from django.urls import path

from projeto.blog.views.post_views import PostView

urlpatterns = [
    path('', PostView.as_view(), name='home')
]