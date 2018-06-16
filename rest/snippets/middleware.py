from django.http import HttpResponse

class ResponseInterceptor(object):

	def __init__(self, get_response):
		self.get_response = get_response


	def process_exception(self,request,exception):
		#def process_exception(self,request,exception):
		print('Hello world')
		response = self.get_response(request)
		print(response)

	#def process_response(self,request, response):
		print('Hello world. This is Response')

	
	def process_response(self,request, response):
		print(response.status_code)
		return HttpResponse('Wrong URL', content_type = "text/plain")



	def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

		response = self.get_response(request)
		self.process_response(request,response)

        # Code to be executed for each request/response after
        # the view is called.
		
		

		return response

