# from django.shortcuts import render, get_object_or_404
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
# from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
# from django.utils.six import BytesIO
# from rest_framework import status
# from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from .custom_functions import get_json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.utils.six import BytesIO
from rest_framework import viewsets


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


# class SnippetList(APIView):

# 	def get(self,request, format=None):
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	def post(self,request, format=None):
# 		data = JSONParser().parse(request.body)
# 		serializer = SnippetSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(status=HTTP_201_CREATED)
# 		return Response(status=HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })










# class SnippetList(generics.ListCreateAPIView):
# 	permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer

# 	def list(self, request):
# 		try:
# 			snippets = Snippet.objects.all()
# 			serializer = SnippetSerializer(snippets, many= True)
# 			json_object = get_json(data=serializer.data)
# 			return JsonResponse(json_object, status=200)
# 		except Snippet.DoesNotExist as e:
# 			json_object	= get_json(error = str(e))
# 			return JsonResponse(json_object, status=404)
# 		# except TypeError as e:
# 		# 	json_object = get_json(error = str(e)+" : Internal Server Error")
# 		# 	return JsonResponse(json_object, status=404)

# 	def post(self, request):
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			try:
# 				serializer.save(owner=request.user)
# 				return JsonResponse(get_json(data=serializer.data, single=True), status=200)
# 			except ValueError as e:
# 				return JsonResponse(get_json(error=str(e)), status=400)
# 		else:
# 			return jsonResponse(get_json(error=serializer.errors), status=404)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer


# class UserList(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
# 	def list(self, request):
# 		try:
# 			users = self.get_queryset()
# 			serializer = UserSerializer(users, many= True, context={'request' : request})
# 			json_object = get_json(data=serializer.data, error=None)
# 			return JsonResponse(json_object, status=200)
# 		except Snippet.DoesNotExist:
# 			json_object	= get_json(data=None, error = "Query does not exist")
# 			return JsonResponse(json_object, status=404)

# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer



class UserViewSets(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer



class SnippetViewSets(viewsets.ModelViewSet):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



