from django.shortcuts import render

# Create your views here.


from django.views.generic.base import View
from django.http import HttpResponse
import json
from rest_framework.response import Response
from  rest_framework.views import APIView


from .models import CRISPR_DATABASE
from .serializers import CRISPRSerializer


class CRISPRView(APIView):
    def get(self,request,format = None):
        # json_list = []
        # CRISPRs = CRISPR_DATABASE.objects.all()
        #
        # for CRISPR_info in CRISPRs:
        #     json_dict = {}
        #     json_dict['CRISPR'] = CRISPR_info.CRISPR
        #     json_dict['CRISPR_name'] = CRISPR_info.CRISPR_name
        #     json_dict['PI'] = CRISPR_info.PI
        #     json_dict['CRISPR_type'] = CRISPR_info.CRISPR_type
        #     json_dict['PAM'] = CRISPR_info.PAM
        #     json_list.append(json_list)
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        CRISPRs = CRISPR_DATABASE.objects.all()
        CRISPR_serializer = CRISPRSerializer(CRISPRs,many=True)

        return Response(CRISPR_serializer.data)



