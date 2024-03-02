# adds a X-Frame-Options header to all responses with a value of DENY. We've defined an __init__ method that accepts a get_response parameter and an __call__ method that adds the header to the response
class XFrameOptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        response['X-Frame-Options'] = 'DENY'
        return response