from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User




class SnippetSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style','owner')



class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippet = serializers.HyperlinkedRelatedField(many=True, queryset=Snippet.objects.all(), view_name = 'snippet-detail')


	class Meta:
		model = User
		fields = ('id', 'username', 'snippet')
