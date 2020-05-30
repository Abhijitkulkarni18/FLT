from django.conf.urls import url
from django.urls import path,re_path
from .userview import UserView,UserListView
from .activityview import ActivityView,ActivityListView

urlpatterns = [
    path(r'user/',UserView.as_view(),name='UserView'),
    path(r'userlist/',UserListView.as_view(),name='UserListView'),
    path(r'activity/',ActivityView.as_view(),name='ActivityView'),
    path(r'activitylist/',ActivityListView.as_view(),name='ActivityListView'),
]