import subprocess
from bill.models import Bill
from bill.permissions import IsOwnerOrReadOnly
from bill.serializers import BillSerializer
from bill.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


# from scripts.convert_image_to_text import convert


class ExampleView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        subprocess.call(
            # ["/usr/bin/open", "-W", "-n", "-a", "/Applications/TextEdit.app"]
            ["idea", "/Users/pedro/ProjectsLink/SalvadorCaetano/projectChatBot/Repositorio/SLCT_18_0365%20-%20Chatbots"]
        )
        return Response({'received data': request.data})


# class Operations(APIView):
#     print("AQUI")
#
#     @classmethod
#     def get_extra_actions(cls):
#         return []
#
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         subprocess.call(
#             ["/usr/bin/open", "-W", "-n", "-a", "/Applications/TextEdit.app"]
#         )
#         return Response({})



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BillCreateObject(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # textImage = convert(serializer.)


class ExportBills(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    @action(detail=False)
    def get_excel_bill(self, request):
        # bills = Bill.objects.get(owner=self.request.user)
        bills = Bill.objects.get(id=1)
        page = self.paginate_queryset(bills)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class BillsByUser(viewsets.ModelViewSet):
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializer
#
#     @action(detail=False)
#     def get_bills_by_user(self, request):
#         bills = Bill.objects.get(owner=request.user.id)
#         page = self.paginate_queryset(bills)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

class BillsByUser(generics.ListAPIView):
    serializer_class = BillSerializer

    def get_queryset(self):
        user = self.request.user
        return Bill.objects.filter(owner=user)

#
# # views.py
#
# class FileUploadView(APIView):
#     parser_classes = (FileUploadParser,)
#
#     def put(self, request, filename, format=None):
#         file_obj = request.data['file']
#         # ...
#         # do some stuff with uploaded file
#         # ...
#         return Response(status=204)
