# Create your views here.
import math
import datetime
from django.shortcuts import Http404
from django.http import HttpResponse,JsonResponse

from rest_framework import generics
from rest_framework import status

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions    import IsAuthenticated, IsAdminUser
from rest_framework.pagination     import LimitOffsetPagination
from rest_framework.response       import Response

from .models import *
from patients.models import Patient
from .serializers import *

class AppointmentList(generics.ListAPIView):
    queryset               = Appointment.objects.all()
    serializer_class       = AppointmentSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]

class MakeAppointment(generics.CreateAPIView):

    def post(self, request, piin, diin, weekat, dateat, time, format=None):
        print("piin:  ", piin)
        print("diin:  ", diin)
        print("weekat:", weekat)
        print("dateat:", dateat)
        print("time:  ", time)
        today  = datetime.date.today()
        patient = Patient.objects.get(iin=piin)
        doctor  = Doctor.objects.get(iin=diin)
        date = (today + datetime.timedelta(days=-today.weekday()+dateat, weeks=weekat))
        appointment = Appointment(patient=patient, doctor=doctor, date=date, time=time)
        appointment.save()
        #serializer = AppointmentSerializer(appointment, partial=True)
        return Response({'message':"ok"})

class DoctorIINList(generics.ListAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]

    def get(self, request, specialization, limit, offset, format=None):
        print("auth:", request.auth)
        print("spec:", specialization)
        doctors    = Doctor.objects.filter(specialization__iexact=specialization).values('iin')
        count      = doctors.count()
        to_return  = doctors[offset:offset+limit]
        serializer = DoctorIINSerializer(to_return, many=True)
        return Response({'doctors': serializer.data, 'count': count})#JsonResponse(serializer.data, safe=False)

class DoctorSchedule(generics.ListAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]

    def get(self, request, iin, format=None):
        print("auth:", request.auth)
        print("iin:",  iin)
        doctor    = Doctor.objects.get(iin=iin)
        appointments = Appointment.objects.filter(doctor=doctor)
        response = self.generate_schedule(doctor.working_hours, doctor.duration)
        return Response({'message': response})

    def generate_schedule(self, working_hours, duration):
        a = []
        for w in range(2):
            today  = datetime.date.today()
            monday = (today + datetime.timedelta(days=-today.weekday(), weeks=w))
            a.append([])
            for d, wh in enumerate(working_hours):
                times = []
                day = (monday + datetime.timedelta(days=d)).day
                for time in wh:
                    # 00:00 - 11:00
                    # 0123456789012
                    hs = int(time[0:2])
                    ms = int(time[3:5])
                    he = int(time[8:10])
                    me = int(time[11:13])
                    while (hs + ms/60 < he + me/60):
                        shs =str(hs)
                        sms =str(ms)
                        if (hs < 10):
                            shs = '0'+shs
                        if (ms < 10):
                            sms = '0'+sms
                        times.append(shs+':'+sms)
                        ms = ms+int(duration)
                        if (ms >= 60):
                            hs = hs+math.floor(ms/60)
                            ms = ms % 60
                a[w].append({"date":str(day), "times":times})
        return a

class DoctorList(generics.ListCreateAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAdminUser,]

    def get(self, request, format=None):
        print(request.auth)
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        print(request.auth)
        print(request.data)
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorR(generics.RetrieveAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated,]
    def get(self, request, pk, format=None):
        print(request.auth)
        try:
            doctor = Doctor.objects.get(iin = pk)
        except Doctor.DoesNotExist:
            raise Http404('Not found')
        serializer = DoctorSerializer(doctor)
        return JsonResponse(serializer.data, safe=False)

class DoctorU(generics.UpdateAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAdminUser,]
    def put(self, request, pk, format=None):
        try:
            doctor = Doctor.objects.get(iin = pk)
        except Doctor.DoesNotExist:
            raise Http404('Not found')
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
