from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import ActivitySerializer
from rest_framework.generics import GenericAPIView
from django.db import IntegrityError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class ActivityView(GenericAPIView):
    serializer_class=ActivitySerializer
    id = openapi.Parameter('id', in_=openapi.IN_QUERY, description='Activity ID',type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[id])
    def get(self, request, format=None):
        from Useractivity.models import Activity
        data = Activity.objects.filter(id=request.GET.get('id'))
        if data:
            serializer = ActivitySerializer(data, many = True)
            return Response({'status':status.HTTP_200_OK,'data':serializer.data},
                            status=status.HTTP_200_OK,
                            content_type="application/json"
                            )
        else:
            return Response({'status':status.HTTP_200_OK,'message':'not Found','data':[]},
                            status=status.HTTP_200_OK,
                            content_type="application/json")


    def post(self, request, format=None):
        try:
            serializer = ActivitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':status.HTTP_201_CREATED,'message':'Activity created','data':serializer.data},
                            status=status.HTTP_201_CREATED,
                            content_type="application/json")
            else:
                return Response({'status':status.HTTP_400_BAD_REQUEST,'message':serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST,
                                content_type="application/json")
        except Exception as e:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'empty data or incorrect fields'},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type="application/json")



    def delete(self, request, format=None):
        try:
            from Useractivity.models import Activity
            Activity.objects.filter(id=request.GET.get('id')).delete()
            return Response({'status':status.HTTP_200_OK,'message':'Activity Deleted'},
                                status=status.HTTP_200_OK,
                                content_type="application/json")

        except Exception as e:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':"Exception","data":{}},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type="application/json")

    def put(self, request, format=None):
        try:
            from Useractivity.models import Activity
            Activity.objects.filter(id=request.GET.get('id')).update(**request.data)
            return Response({'status':status.HTTP_200_OK,'message':'Activity Updated'},
                                status=status.HTTP_200_OK,
                                content_type="application/json")
        except IntegrityError:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':"invalid id in the data"},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type="application/json"
                            )
        except Exception as e:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':"Exception"+str(e),"data":{}},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type="application/json")


class ActivityListView(GenericAPIView):
    serializer_class=ActivitySerializer
    items_per_page = openapi.Parameter('items_per_page', in_=openapi.IN_QUERY, description='items per page',type=openapi.TYPE_STRING)
    page_no = openapi.Parameter('page_no', in_=openapi.IN_QUERY, description='page no',type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[items_per_page,page_no])
    def get(self, request, format=None):
        from Useractivity.models import Activity
        if request.GET.get('user_id'):
            data = Activity.objects.filter(user=request.GET.get('user_id'))
        else:
            data = Activity.objects.all().order_by('start_time')
        if data:
            paginator = Paginator(data,request.GET.get('items_per_page'))
            page = request.GET.get('page',request.GET.get('page_no'))
            Activity = paginator.get_page(page)
            serializer = ActivitySerializer(Activity, many = True)
            page_num = int(request.GET.get('page_no'))
            if (page_num<=0)or(page_num>paginator.num_pages):
                return Response({'status':status.HTTP_204_NO_CONTENT,'message':'Empty Records','data':{}},
                                status=status.HTTP_204_NO_CONTENT,
                                content_type="application/json"
                                )
            else:
                return Response({'status':status.HTTP_200_OK,'message':'Found','data':{"Activity_data":serializer.data}},
                                status=status.HTTP_200_OK,
                                content_type="application/json"
                                )
        else:
            return Response({'status':status.HTTP_200_OK,'message':'not Found','data':[]},
                            status=status.HTTP_200_OK,
                            content_type="application/json")