from django.conf.urls import url, include
from snippets import views

urlpatterns = [
	url('api_auth/', include('rest_framework.urls')),
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),
]