from django.urls import path
from data_manager import views

app_name = 'data_manager'

urlpatterns = [
    path("", views.login_page, name='index'),
    path("accounts/profile/", views.login_user_with_google, name='accounts/profile/'),
    path("query-builder", views.query_builder, name='query-builder'),
    path("users-list", views.users_list, name='users-list'),
    path("upload-data", views.upload_data, name='upload-data'),
    path("add-user", views.add_user, name='add-user'),
    path("delete-user", views.delete_user, name='delete-user'),
    path('upload/', views.upload_file, name='upload_file'),
    path('api/filter-records/', views.FilterRecordsView.as_view(), name='filter-records'),
]
