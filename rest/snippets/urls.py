from django.conf.urls import url, include
from snippets import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='My API')



snippet_list = views.SnippetViewSets.as_view({
	'get' : 'list',
	'post' : 'create'
	})

snippet_detail = views.SnippetViewSets.as_view({
	'get' : 'list',
	'put' : 'update',
	'patch' : 'partial_update',
	'delete' : 'destroy'
	})

user_list = views.UserViewSets.as_view({
	'get' : 'list'
	})

user_detail = views.UserViewSets.as_view({
	'get' : 'list'
	})





urlpatterns = [
	url(r'^$', views.api_root),
	url(r'^schema/$', schema_view),
	url('api_auth/', include('rest_framework.urls')),
	url(r'^users/$', user_list, name="user-list"),
	url(r'^users/(?P<pk>[0-9]+)$', user_detail, name="user-detail"),
    url(r'^snippets/$', snippet_list, name="snippet-list"),
    url(r'^snippets/(?P<pk>[0-9]+)$', snippet_detail, name="snippet-detail"),
]