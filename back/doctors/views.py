# Create your views here.
import math
from datetime import datetime, timedelta
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
        today  = datetime.date.today()
        patient = Patient.objects.get(iin=piin)
        doctor  = Doctor.objects.get(iin=diin)
        date = (today + timedelta(days=-today.weekday()+dateat, weeks=weekat))
        appointment = Appointment(patient=patient, doctor=doctor, date=date, time=time)
        status = AppointmentStatus(aid=appointment.id)
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
        doctor    = Doctor.objects.get(iin=iin)
        response = self.generate_schedule(doctor)
        return Response({'message': response})

    def generate_schedule(self, doctor):
        a = []
        working_hours = doctor.working_hours
        duration      = int(doctor.duration)
        appointments = Appointment.objects.filter(doctor=doctor)
        for w in range(2):
            today  = datetime.now() + timedelta(hours=6)
            monday = (today + timedelta(days=-today.weekday(), weeks=w))
            month  = (today + timedelta(weeks=w)).strftime("%B")
            year   = (today + timedelta(weeks=w)).year
            a.append({'month':month, 'year':year, 'days':[]})
            for d, wh in enumerate(working_hours):
                times = []
                date = (monday + timedelta(days=d))
                day  = date.day
                print(date, ">=", today, ":", date>=today)
                if (date >= today) :
                    for time in wh:
                        # 00:00 - 11:00
                        # 0123456789012
                        hs = int(time[0:2])
                        ms = int(time[3:5])
                        he = int(time[8:10])
                        me = int(time[11:13])
                        h  = hs
                        m  = ms
                        if (date==today
                        and (h < today.hour or (h == today.hour and m < today.minute))):
                            dt = (today.hour + today.minute/60) - (hs + ms/60)
                            n  = math.ceil(dt/(duration/60))
                            m = m + n * duration
                            h = hs + math.floor(m/60)
                            m = m % 60
                        while (h + (m+duration)/60 <= he + me/60):
                            sh =str(h)
                            sm =str(m)
                            if (h < 10):
                                sh = '0'+sh
                            if (m < 10):
                                sm = '0'+sm
                            time = sh+':'+sm
                            if (not appointments.filter(time=time).exists()) :
                                times.append(sh+':'+sm)
                            m = m+int(duration)
                            if (m >= 60):
                                h = h+math.floor(m/60)
                                m = m % 60
                a[w]['days'].append({"date":str(day), "times":times})
        return a

class DoctorList(generics.ListCreateAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAdminUser,]

    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
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
