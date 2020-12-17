from rest_framework import serializers
# from .models import Fbooks
from .models import Fbooks, Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class FbooksSerializer(serializers.ModelSerializer):
    fbooks_FRK = UserSerializer(many=True, read_only=True)
    # User모델에 설정해뒀던 컬럼을 삽입하는 구문. 반드시 해당 컬럼의 related_name을 사용해야 정상적으로 나온다.
    class Meta:
        model = Fbooks
        fields = "__all__"










