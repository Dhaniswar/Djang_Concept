# def p_middleware(get_response):
#     print("One time initialization")

#     def p_function(self, request):
#         print("This is execute before view")
#         response = get_response(request)
#         print("This is After View")
#         return response
    
#     return p_middleware
import time
import json

class Pmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization")

    def __call__(self, request):
        print("This execute before view")
        print("Request =>", request.method, request.get_full_path())
        start_time = time.time()
        response = self.get_response(request)
        if request.method == 'POST':
            print("Request Body =>", (request.body))

        response = self.get_response(request)
        end_time = time.time()
        print("Status Code =>", response.status_code)
        print("Time taken =>", end_time - start_time)
        print("This execute After view")
        return response

