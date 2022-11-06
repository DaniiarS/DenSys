# Create your views here.
import logging

from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Doctor
from .serializers import DoctorSerializer

@csrf_exempt
def DoctorsView(request):
    logger = logging.getLogger("mylogger")
    logger.info("All Doctors View")
    if request.method == 'GET':
        logger.info("ALL GET")
        items = Doctor.objects.all()
        serializer = DoctorSerializer(items, many =True)
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        logger.info("ALL POST")
        data = JSONParser().parse(request)
        logger.info(data)
        serializer =DoctorSerializer(data = data)
        logger.info(serializer)
        logger.info(serializer.is_valid())

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def DoctorView(request, iin):
    logger = logging.getLogger("mylogger")
    logger.info("One Doctor View")
    try:
        item = Doctor.objects.get(iin = iin)
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
