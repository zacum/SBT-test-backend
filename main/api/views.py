from rest_framework import viewsets, status
from .serializer import UniModelSerializer, DegModelSerializer, MdataModelSerializer
from main.models import University, Degree, Mdata
from django.http.response import JsonResponse


class UniViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniModelSerializer


class DegViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegModelSerializer


class MdataViewSet(viewsets.ModelViewSet):
    queryset = Mdata.objects.all()
    serializer_class = MdataModelSerializer


def getMetadata(request, pk):
    try:
        mdata = Mdata.objects.get(tokenid=pk)
        if request.method == "GET":
            mdata_serializer = MdataModelSerializer(mdata)
            return JsonResponse(mdata_serializer.data)
    except Mdata.DoesNotExist:
        return JsonResponse(
            {"message": "The Metadata does not exist"}, status=status.HTTP_404_NOT_FOUND
        )
