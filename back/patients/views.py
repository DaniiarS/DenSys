# Create your views here.
import logging

from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Patient
from .serializers import PatientSerializer

@csrf_exempt
def PatientsView(request):
    logger = logging.getLogger("mylogger")
    logger.info("All Patients View")
    if request.method == 'GET':
        logger.info("ALL GET")
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many =True)
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        logger.info("ALL POST")
        data = JSONParser().parse(request)
        logger.info(data)
        serializer =PatientSerializer(data = data)
        logger.info(serializer)
        logger.info(serializer.is_valid())

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def PatientView(request, iin):
    logger = logging.getLogger("mylogger")
    logger.info("One Patient View")
    try:
        logger.info(f"Patient iin:{iin}")
        patient = Patient.objects.get(iin = iin)
    except Patient.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(patient,data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == "DELETE":
        patient.delete()
        return HttpResponse(status =204)
