# Create your views here.
import math
from datetime         import datetime, timedelta, date
from django.shortcuts import Http404
from django.http      import HttpResponse,JsonResponse
from django.db.models import Count
from django.db.models import Q
from django.db.models.functions import Lower

from rest_framework import generics
from rest_framework import status

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions    import IsAuthenticated, IsAdminUser
from rest_framework.pagination     import LimitOffsetPagination
from rest_framework.response       import Response

from .models            import *
from patients.models    import Patient
from .serializers       import *

class PatientHistoryList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]

    def get(self, request, iin, format=None):
        patient      = Patient.objects.get(iin=iin)
        appointments = AppointmentStatus.objects.filter( aid__patient=patient ).order_by(Lower('when_made').desc())
        services     = ServiceRequestStatus.objects.filter(srid__patient=patient).order_by(Lower('when_made').desc())
        p            = PatientSerializer(patient)
        a            = AppointmentStatusSerializer(appointments, many=True)
        s            = ServiceRequestStatusSerializer(services,  many=True)
        return Response({'patient':p.data, 'appointments':a.data, 'services':s.data})

class DoctorPatientList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]

    def get(self, request, format=None):
        doctor      = Doctor.objects.get(iin=request.user.iin)
        patients    = Appointment.objects.raw(f'SELECT id, DA.patient_id, COUNT() AS pcount FROM doctors_appointment AS DA WHERE DA.doctor_id=\'{doctor}\' GROUP BY DA.patient_id')
        print(f'SELECT id, DA.patient_id, COUNT() AS pcount FROM doctors_appointment AS DA WHERE DA.doctor_id=\'{doctor}\' GROUP BY DA.patient_id')
        result      = DoctorPatientSerializer(patients, many=True)
        print(result.data)
        return Response(result.data)

class DoctorAppointmentList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]

    def get(self, request, format=None):
        doctor       = Doctor.objects.get(iin=request.user.iin)
        appointments = Appointment.objects.filter(doctor=doctor).order_by('date', 'time')
        a            = AppointmentSerializer(appointments, many=True)
        return Response(a.data)

class PatientRequestList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAuthenticated,]
    def get(self, request, iin, format=None):
        try:
            patient      = Patient.objects.get(iin=iin)
        except Patient.DoesNotExist:
            appointments = Appointment.objects.filter(status=0).order_by('date', 'time')
            service_reqs = ServiceRequest.objects.filter(status=0).order_by('date', 'time')
            a            = AppointmentSerializer(appointments, many=True)
            s            = ServiceRequestSerializer(service_reqs, many=True)
            return Response({'appointments': a.data, 'service_requests': s.data})
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
        serviceReq.save()
        status      = ServiceRequestStatus(srid=serviceReq)
        status.save()
        #serializer = AppointmentSerializer(appointment, partial=True)
        return Response({'message':"ok"})

class MakeAppointment(generics.CreateAPIView):

    def post(self, request, piin, diin, weekat, dateat, time, format=None):
        today       = date.today()
        patient     = Patient.objects.get(iin=piin)
        doctor      = Doctor.objects.get(iin=diin)
        dateReq     = (today + timedelta(days=-today.weekday()+dateat, weeks=weekat))
        appointment = Appointment(patient=patient, doctor=doctor, date=dateReq, time=time)
        appointment.save()
        status      = AppointmentStatus(aid=appointment)
        status.save()
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
                        if (not busy.filter(Q(time=time), Q(status=0) | Q(status=1) | Q(status=2)).exists()) :
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

class ServiceRequestRU(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated,]

    def put(self, request, srid, format=None):
        try:
            service_request = ServiceRequest.objects.get(id=srid)
        except ServiceRequest.DoesNotExist:
            raise Http404('Not found')

        serializer = ServiceRequestUpdateStatusSerializer(service_request, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            service_request = ServiceRequest.objects.get(id = srid)
            astatus     = ServiceRequestStatus(srid=service_request, status=service_request.status)
            astatus.save()
            history     = ServiceRequestStatus.objects.filter(srid=service_request).order_by(Lower('when_made').desc())
            a = ServiceRequestSerializer(service_request)
            h = ServiceRequestStatusSerializer(history, many=True)
            print(history)
            return JsonResponse({'service_request': a.data, 'history': h.data}, safe=False)

        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, srid, format=None):
        try:
            service_request = ServiceRequest.objects.get(id = srid)
            history     = ServiceRequestStatus.objects.filter(srid=service_request).order_by(Lower('when_made').desc())
            print(history)
        except ServiceRequest.DoesNotExist:
            raise Http404('Not found')
        s = ServiceRequestSerializer(service_request)
        h = ServiceRequestStatusSerializer(history, many=True)
        print(h.data)
        return JsonResponse({'service_request': s.data, 'history': h.data}, safe=False)

class AppointmentRU(generics.RetrieveUpdateAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated,]

    def put(self, request, aid, format=None):
        try:
            appointment = Appointment.objects.get(id = aid)
        except Appointment.DoesNotExist:
            raise Http404('Not found')

        serializer = AppointmentUpdateStatusSerializer(appointment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            appointment = Appointment.objects.get(id = aid)
            astatus     = AppointmentStatus(aid=appointment, status=appointment.status)
            astatus.save()
            history     = AppointmentStatus.objects.filter(aid=appointment).order_by(Lower('when_made').desc())
            a = AppointmentSerializer(appointment)
            h = AppointmentStatusSerializer(history, many=True)
            print(history)
            return JsonResponse({'appointment': a.data, 'history': h.data}, safe=False)

        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, aid, format=None):
        try:
            appointment = Appointment.objects.get(id = aid)
            history     = AppointmentStatus.objects.filter(aid=appointment).order_by(Lower('when_made').desc())
            print(history)
        except Appointment.DoesNotExist:
            raise Http404('Not found')
        a = AppointmentSerializer(appointment)
        h = AppointmentStatusSerializer(history, many=True)
        print(h.data)
        return JsonResponse({'appointment': a.data, 'history': h.data}, safe=False)

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

class ServiceR(generics.RetrieveAPIView):
    queryset               = Service.objects.all()
    serializer_class       = ServiceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated,]
    def get(self, request, pk, format=None):
        try:
            service = Service.objects.get(id = pk)
        except Service.DoesNotExist:
            raise Http404('Not found')
        serializer = ServiceSerializer(service)
        return JsonResponse(serializer.data, safe=False)

class ServiceU(generics.RetrieveAPIView):
    queryset               = Service.objects.all()
    serializer_class       = ServiceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAdminUser,]
    def put(self, request, pk, format=None):
        try:
            service = Service.objects.get(id = pk)
        except Service.DoesNotExist:
            raise Http404('Not found')
        serializer = ServiceSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
