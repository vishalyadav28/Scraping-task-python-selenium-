import json
from .models import *
import urllib.request
from drf_yasg import openapi
from django.db.models import Q
from rest_framework import viewsets
import scrap_data.constants as constants
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication


search_key = openapi.Parameter('search_key', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING)

class TICViewset(viewsets.ViewSet):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    permission_classes     = [IsAuthenticated]
    parser_classes         = (MultiPartParser,)
    
    # data get api 
    @swagger_auto_schema(
        manual_parameters=[search_key],tags=['company_search']
        )
    @action(methods=['GET' ], detail=False)
    def companysearch(self,request):
        try:

            search_key = request.GET.get('search_key')
            search_data = DataStore.objects.filter(Q(company_name__iexact = search_key) | Q(plan_id__exact = search_key))
            if search_data.exists():
                data = search_data.values()
                get_url= urllib.request.urlopen(data[0].get('report_data'))
                
                return Response(
                    constants.data((json.load(get_url))['reporting_structure'])
                    )
                # return Response(
                #     constants.data()
                #     )
            else:
                return Response(
                    constants.failed("Data doesn't exists")
                    )

        except Exception as error:

            return Response(
                constants.error(str(error))
            )

        
