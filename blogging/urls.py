from django.urls import path
from blogging.views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path(
        "posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"
    ),  # TODO: May need to change to posts/<int:pk>/, will need to test
]
