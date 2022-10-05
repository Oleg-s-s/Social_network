from django.urls import path
from .views import dashboard, profile_list, profile, post, PostDeleteView, likepost, commentdelete
from users.views import dashboardU

app_name = "network"

urlpatterns = [
    path("", dashboardU),
    path("dashboard/<int:page>/", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name='profile_list'),
    path("profile/<int:pk>/", profile, name="profile"),
    path("comments/<int:post_id>/", post, name="post"),
    path("comments/<int:post_id>/like", likepost, name="like"),
    path("comments/<int:post_id>/<int:comment_id>/", commentdelete, name="delete_comment"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete_post"),
]