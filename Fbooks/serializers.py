from rest_framework import serializers
# from .models import Fbooks
from .models import Fbooks, Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class FbooksSerializer(serializers.ModelSerializer):
    information = UserSerializer(many=True, read_only=True)
    # User모델에 설정해뒀던 컬럼을 삽입하는 구문. 반드시 해당 컬럼의 related_name을 사용해야 정상적으로 나온다.
    class Meta:
        model = Fbooks
        fields = "__all__"

# 나의 경우엔 django-rest-auth를 사용하여 로그인 기능을 구현했다.
# rest_framework, rest_auth(회원가입 및 로그인), allauth(소셜 로그인), rest_framework_jwt을 통합한 환경이 되겠다. 
# 참고로 rest_auth의 소셜 로그인 기능은 문서가 부실하다.
# 구현 과정에서 깨달은 여러 토픽들을 정리하고자 한다.








