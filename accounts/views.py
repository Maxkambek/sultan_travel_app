from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import Account, VerifyPhone, AccountDetails
from rest_framework import generics, status, permissions
from rest_framework.views import Response, APIView
from random import randint
from .utils import verify
from .serializers import RegisterSerializer, LoginSerializer, VerifyPhoneSerializer, AccountDetailsSerializer, \
    VerifyPhoneSerializer2, AccountSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        if not phone:
            return Response({'Telefon raqam kemadi tupoymisz?'}, status=404)
        if Account.objects.filter(phone=phone, is_active=True).first():
            return Response({'message': "This number already exist"}, status=status.HTTP_302_FOUND)
        ver = VerifyPhone.objects.filter(phone=phone).first()
        if ver:
            ver.delete()
        code = str(randint(100000, 1000000))
        verify(phone, code)
        VerifyPhone.objects.create(phone=phone, code=code)
        return Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"},
                        status=status.HTTP_200_OK)


class RegisterConfirmAPI(generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = VerifyPhoneSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        code = self.request.data['code']
        if not phone or not code:
            return Response({'message': "Phone or code not exist"}, status=404)
        v = VerifyPhone.objects.filter(phone=phone, code=code).first()
        if not v:
            return Response({'message': "Confirmation code incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
        user = Account.objects.create(
            phone=phone,
            password="12345678"
        )
        user.is_active = True
        user.save()
        token = Token.objects.create(user=user)
        v.delete()
        data = {
            'message': 'User verified',
            'token': str(token.key),
            "user_id": user.id
        }
        return Response(data, status=status.HTTP_201_CREATED)


#
# class CreateUserAPIView(generics.GenericAPIView):
#     queryset = Account.objects.all()
#     serializer_class = VerifyPhoneSerializer2
#
#     def post(self, request, *args, **kwargs):
#         phone = self.request.data['phone']
#         code = self.request.data['code']
#         password = self.request.data['password']
#         v = VerifyPhone.objects.filter(phone=phone, code=code).first()
#         if v:
#             v.delete()
#         else:
#             return Response({'message': "Confirmation code incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
#         user = Account.objects.create(
#             phone=phone,
#             password=password
#         )
#         user.is_active = True
#         user.save()
#         token = Token.objects.create(user=user)
#         data = {
#             'message': 'User verified',
#             'token': str(token.key),
#             "user_id": user.id
#         }
#         return Response(data, status=status.HTTP_201_CREATED)


class LoginAPI(generics.GenericAPIView):
    def get_queryset(self):
        return Account.objects.all()

    def get_serializer_class(self):
        return LoginSerializer

    def post(self, request, *args, **kwargs):
        phone = request.data['phone']
        user = Account.objects.filter(phone=phone).first()
        if not user:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        v = VerifyPhone.objects.filter(phone=phone)
        if v:
            v.delete()
        code = str(randint(100000, 1000000))
        verify(phone, code)
        VerifyPhone.objects.create(phone=phone, code=code)
        return Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"},
                        status=status.HTTP_200_OK)


class LoginConfirmAPI(generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = VerifyPhoneSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        code = self.request.data['code']
        if not phone or not code:
            return Response({'message': "Phone or code not exist"}, status=404)
        v = VerifyPhone.objects.filter(phone=phone, code=code).first()
        if not v:
            return Response({'message': "Confirmation code incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
        user = Account.objects.filter(phone=phone).first()
        token = Token.objects.get(user=user)
        v.delete()
        data = {
            'message': 'User verified',
            'token': str(token.key),
            "user_id": user.id
        }
        return Response(data, status=status.HTTP_201_CREATED)


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({
                "msg": "Logout Success"
            }, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class AccountDetailCreateAPIView(generics.CreateAPIView):
    queryset = AccountDetails.objects.all()
    serializer_class = AccountDetailsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = Account.objects.filter(id=request.user.id).first()
        if user.name:
            pass
        else:
            user.name = self.request.data.get('full_name')
            user.save()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class AccountRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



class AccountDetailListAPIView(generics.ListAPIView):
    queryset = AccountDetails.objects.all()
    serializer_class = AccountDetailsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = AccountDetails.objects.filter(user=self.request.user)
        return queryset
