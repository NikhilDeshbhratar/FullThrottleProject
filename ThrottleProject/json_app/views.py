from rest_framework import viewsets
from .models import Members
from .serializer import JsonDataSerializer
from django.http import JsonResponse
from rest_framework.exceptions import ParseError
from .service import populate_data,format_json
import json

# Create your views here.
class JsonViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = JsonDataSerializer

    def list(self,request):
        Members.objects.filter().delete()
        populate_data()
        queryset = Members.objects.filter()
        serializer = JsonDataSerializer(queryset,many=True)
        formatted_data = list(map(format_json,list(json.loads(json.dumps(serializer.data)))))
        return JsonResponse({
            "ok":True,
            "members":formatted_data
        })