from rest_framework.views import APIView
from utils import results
from .serializers import UserSerializer
class Login(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return results.failure(None, '1002', '参数无效')
        username = serializer.data['username']
        password = serializer.data['password']
        if username is None or username == '' or password is None or password == '':
            return results.failure(None, '1001', '账号密码不能为空')
        if username == 'jack' and password == '123456':
            return results.success(None, message='登录成功')
        return results.failure(None, '1002', '登录失败')
