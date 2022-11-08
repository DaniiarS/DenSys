# Create your views here.
from django.shortcuts import render,HttpResponseRedirect,Http404
#from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Doctor
from .serializers import DoctorSerializer, FileSerializer
from rest_framework.views import APIView

class DoctorViewSet(APIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, iin = None, format=None):
        if (iin is None) :
            doctors = Doctor.objects.all()
            serializer = DoctorSerializer(doctors, many=True)
            return JsonResponse(serializer.data, safe=False)
        try:
            doctor = Doctor.objects.get(iin = iin)
        except Doctor.DoesNotExist:
            raise Http404('Not found')
        serializer = DoctorSerializer(doctor)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, iin, format=None):
        try:
            doctor = Doctor.objects.get(iin = iin)
        except Doctor.DoesNotExist:
            raise Http404('Not found')
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

@csrf_exempt
def DoctorsView(request):
    if request.method == 'GET':
        items = Doctor.objects.all()
        serializer = DoctorSerializer(items, many =True)
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        data = MultiPartParser().parse(request)
        serializer =DoctorSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def DoctorView(request, iin):
    try:
        doctor = Doctor.objects.get(iin = iin)
    except Doctor.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = DoctorSerializer(item)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DoctorSerializer(item,data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status =204)
