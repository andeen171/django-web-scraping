from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
import requests


class Drogasil(APIView):
    api_address = 'https://api-gateway-prod.drogasil.com.br/search/v2/store/DROGASIL/channel/SITE/product/search/live'

    def get(self, request):
        term = request.GET.get('term')
        if not term:
            return Response({'message': 'Please provide a valid term'}, status=400)
        uri = self.api_address + '?term=' + term + '&sort_by=relevance:desc'
        limit = request.GET.get('limit')
        if limit:
            uri += '&limit=' + limit
        req = requests.get(uri)
        if req.status_code == 200:
            data = ProductSerializer(req.json()['results']['products'], many=True).data
            return Response(data)
        else:
            return Response({'message': 'error'}, status=req.status_code)
