from django.utils.deprecation import MiddlewareMixin


class TestMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        print('1111每次请求前，都会调用执行')

        name = request.COOKIES.get('username')
        if name:
            print('111没有用户信息')
        else:
            print('111有用户信息')

    def process_response(self, request, response):
        print('111每次响应前，都会调用')

        return response


class TestMiddleWare2(MiddlewareMixin):

    def process_request(self, request):
        print('222每次请求前，都会调用执行')

        name = request.COOKIES.get('username')
        if name:
            print('22没有用户信息')
        else:
            print('22有用户信息')

    def process_response(self, request, response):
        print('22每次响应前，都会调用')

        return response