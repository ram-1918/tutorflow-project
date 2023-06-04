from django.urls import path, re_path
from .views import ListUsersAPI, GetUserAPI, LoginAPI, AnonymousLoginAPI, CreatePost, UpdatePost, ListAnswersAPI, GetAnswersAPI, ListAnswersAPI_RO
from .views import ListFavoritesAPI, GetFavoritesAPI, ListFavoritesAPI_RO, GetFavoritesAPI_RO, FeedbackAPI, LikesAPI, GetLikesAPI, FeedbackDeleteAPI


urlpatterns = [
    path("user/", ListUsersAPI.as_view()),
    path("user/<int:pk>", GetUserAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("anon-login/", AnonymousLoginAPI.as_view()),

    path("", CreatePost.as_view(), name="create-post"),
    path("tutor-list/", CreatePost.as_view()),
    path("tutor-list/<int:pk>", UpdatePost.as_view()),

    path('answers/', ListAnswersAPI.as_view()),
    path("answer/<int:pk>", GetAnswersAPI.as_view()),
    path("answers-ro/", ListAnswersAPI_RO.as_view()),

    path("likes/", LikesAPI.as_view()),
    path("likes/<int:pk>", GetLikesAPI.as_view()),

    path("favorites/", ListFavoritesAPI.as_view()),
    path("favorites/<int:pk>", GetFavoritesAPI.as_view()),
    path("favorites_ro/", ListFavoritesAPI_RO.as_view()),
    path("favorites_ro/<int:pk>", GetFavoritesAPI_RO.as_view()),

    path("feedbacks/", FeedbackAPI),
    path("feedbacks/<int:pk>", FeedbackDeleteAPI.as_view()),

]
