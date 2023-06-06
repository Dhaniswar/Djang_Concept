class Request:
    def send(*args):
        print('Sent', args)



# Request.send()
# print(Request.send)
# print(type(Request.send))

http_request = Request()
# print(http_request.send)

# print(type(Request.send) is type(http_request.send))
# print(type(http_request.send))  # <class 'method'>
# print(type(Request.send))  # <class 'function'>

# Request.send()
# print(hex(id(http_request)))
# http_request.send()
http_request.send()
Request.send(http_request)