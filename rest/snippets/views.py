from django.shortcuts import render, get_object_or_404
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.utils.six import BytesIO
from rest_framework import status
from rest_framework import APIView



# Create your views here.

# @api_view(['GET', 'POST'])
# def snippet_list(request):
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request.body)
# 		serializer = SnippetSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		print("error # 1")
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_details(request, pk):
# 	#retrieve the snippet using primary key
# 	try:
# 		snippet = Snippet.objects.get(pk=pk)
# 	except:
# 		print("error # 2")
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		print (request.body);
# 		stream = BytesIO(request.body)
# 		data = JSONParser().parse(stream)
# 		serializer = SnippetSerializer(snippet, data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		print("Error # 3")
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return Response(status=HTTP_204_NO_CONTENT)





###########.   Will create view classes


class SnippetList(APIView):

	def get(request):
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return Response(serializer.data)

	def post(request):







