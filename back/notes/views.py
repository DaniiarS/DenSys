from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @csrf_exempt
    def ItemsView(request):
        if request.method == 'GET':
            items = Note.objects.all()
            serializer = NoteSerializer(items, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)

            serializer = NoteSerializer(data = data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status =201)
            return JsonResponse(serializer.errors, status = 400)

    @csrf_exempt
    def ItemView(request,nm):
        try:
            item = Note.objects.get(id = nm)
        except Note.DoesNotExist:
            raise Http404('Page Not found')

        if request.method == 'GET':
            serializer = NoteSerializer(item)
            return JsonResponse(serializer.data)

        if request.method == 'PUT':
            data = JSONParser().parse(request)

            logger = logging.getLogger("mylogger")
            logger.info("Whatever to log")

            serializer = NoteSerializer(item,data =data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status =400)

        if request.method == "DELETE":
            item.delete()
            return HttpResponse(status =204)
