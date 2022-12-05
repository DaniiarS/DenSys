# Create your views here.
import math
from datetime import datetime, timedelta, date
from django.shortcuts   import Http404
from django.http        import HttpResponse,JsonResponse

from rest_framework import generics
from rest_framework import status

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions    import IsAuthenticated, IsAdminUser
from rest_framework.pagination     import LimitOffsetPagination
from rest_framework.response       import Response

from .models            import *
from patients.models    import Patient
from .serializers       import *

class PatientRequestList(generics.ListAPIView):
    queryset               = Appointment.objects.all()
    serializer_class       = AppointmentSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]
    def get(self, request, iin, format=None):
        patient      = Patient.objects.get(iin=iin)
        appointments = Appointment.objects.filter(patient=patient).order_by('date', 'time')
        service_reqs = ServiceRequest.objects.filter(patient=patient).order_by('date', 'time')
        a            = AppointmentSerializer(appointments, many=True)
        s            = ServiceRequestSerializer(service_reqs, many=True)
        return Response({'appointments': a.data, 'service_requests': s.data})

class AppointmentList(generics.ListAPIView):
    queryset               = Appointment.objects.all()
    serializer_class       = AppointmentSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]

class ServiceRequestList(generics.ListAPIView):
    queryset               = Service.objects.all()
    serializer_class       = ServiceSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]


class RequestService(generics.CreateAPIView):
    def post(self, request, piin, sid, weekat, dateat, time, format=None):
        today       = date.today()
        patient     = Patient.objects.get(iin=piin)
        service     = Service.objects.get(id=sid)
        dateReq     = (today + timedelta(days=-today.weekday()+dateat, weeks=weekat))
        serviceReq  = ServiceRequest(patient=patient, service=service, date=dateReq, time=time)
        status      = ServiceRequestStatus(srid=serviceReq.id)
        serviceReq.save()
        #status.save()
        #serializer = AppointmentSerializer(appointment, partial=True)
        return Response({'message':"ok"})

class MakeAppointment(generics.CreateAPIView):
    def post(self, request, piin, diin, weekat, dateat, time, format=None):
        today       = date.today()
        patient     = Patient.objects.get(iin=piin)
        doctor      = Doctor.objects.get(iin=diin)
        dateReq     = (today + timedelta(days=-today.weekday()+dateat, weeks=weekat))
        appointment = Appointment(patient=patient, doctor=doctor, date=dateReq, time=time)
        status      = AppointmentStatus(aid=appointment.id)
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

def generate_schedule(working_hours, duration, busy):
    # duck typing: busy is either appointments or servicerequests
    a = []
    for w in range(2):
        today  = datetime.now() + timedelta(hours=6)
        monday = (today + timedelta(days=-today.weekday(), weeks=w))
        month  = (today + timedelta(weeks=w)).strftime("%B")
        year   = (today + timedelta(weeks=w)).year
        a.append({'month':month, 'year':year, 'days':[]})
        for d, wh in enumerate(working_hours):
            times = []
            date  = (monday + timedelta(days=d))
            day   = date.day
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
                        m  = m + n * duration
                        h  = hs + math.floor(m/60)
                        m  = m % 60
                    while (h + (m+duration)/60 <= he + me/60):
                        sh =str(h)
                        sm =str(m)
                        if (h < 10):
                            sh = '0'+sh
                        if (m < 10):
                            sm = '0'+sm
                        time = sh+':'+sm
                        if (not busy.filter(time=time).exists()) :
                            times.append(sh+':'+sm)
                        m = m+int(duration)
                        if (m >= 60):
                            h = h+math.floor(m/60)
                            m = m % 60
            a[w]['days'].append({"date":str(day), "times":times})
    return a

class ServiceSchedule(generics.ListAPIView):
    queryset               = Service.objects.all()
    serializer_class       = ServiceSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]

    def get(self, request, sid, format=None):
        service     = Service.objects.get(id=sid)
        serviceReqs = ServiceRequest.objects.filter(service=service)
        response    = generate_schedule(service.working_hours, int(service.duration), serviceReqs)
        return Response({'message': response})

class DoctorSchedule(generics.ListAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]

    def get(self, request, iin, format=None):
        doctor       = Doctor.objects.get(iin=iin)
        appointments = Appointment.objects.filter(doctor=doctor)
        response     = generate_schedule(doctor.working_hours, int(doctor.duration), appointments)
        return Response({'message': response})

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

class ServiceDepartmentList(generics.ListAPIView):
    queryset               = Service.objects.all()
    serializer_class       = ServiceSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]

    def get(self, request, department, limit, offset, format=None):
        print("auth:", request.auth)
        services   = Service.objects.filter(department__iexact=department)
        count      = services.count()
        to_return  = services[offset:offset+limit]
        serializer = ServiceSerializer(to_return, many=True)
        return Response({'services': serializer.data, 'count': count})#JsonResponse(serializer.data, safe=False)


class ServiceList(generics.ListCreateAPIView):
    queryset               = Service.objects.all()
    serializer_class       = ServiceSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAdminUser,]

    def get(self, request, format=None):
        print(request.auth)
        Services = Service.objects.all()
        serializer = ServiceSerializer(Services, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        print(request.auth)
        print(request.data)
        serializer = ServiceSerializer(data=request.data)
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
