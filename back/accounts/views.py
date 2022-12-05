from rest_framework.authtoken.views  import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response         import Response

from doctors.models                  import Doctor
from patients.models                 import Patient

class UserObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.errors)
        user           = serializer.validated_data['user']
        print(user.iin)
        token, created = Token.objects.get_or_create(user=user)
        if (user.is_superuser) :
            return Response({'token': token.key, 'who': 'admin', 'user_iin': user.iin})
        try:
            doctor = Doctor.objects.get(iin = user.iin)
            return Response({'token': token.key, 'who': 'doctor', 'user_iin': user.iin})
        except Doctor.DoesNotExist:
            try:
                patient = Patient.objects.get(iin = user.iin)
                return Response({'token': token.key, 'who': 'patient', 'user_iin': user.iin})
            except Patient.DoesNotExist:
                return Response({'token': token.key})


obtain_auth_token = UserObtainAuthToken.as_view()
