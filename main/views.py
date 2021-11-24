from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Cars
from .serializer import CarsSerializer
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .filters import UserFilter
from rest_framework import filters


# Create your views here.

class HomeView(viewsets.ModelViewSet):

    #renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    #template_name = "base/home.html"
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_class = UserFilter
    search_fields = ['brand', 'model', 'year', 'color', 'city', 'country', 'price' ]
    ordering = 'brand'

    def create(self, request):
        response = {'message': 'Create function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
"""
    def list(self, request):
        queryset = Cars.objects.all()
        page = self.paginate_queryset(queryset)

        filter = UserFilter(request.GET, queryset=queryset)

        car_brand = Cars.objects.order_by('brand').values('brand').distinct()
        car_model = Cars.objects.order_by('model').values('model').distinct()

        brandFilter = UserFilter(request.GET, queryset=car_brand)
        modelFilter = UserFilter(request.GET, queryset=car_model)

        serializer = self.get_serializer(queryset, many=True)

        return Response({'results':serializer.data,
                         'brandFilter': brandFilter,
                         'modelFilter': modelFilter,
                         'filter': filter,
                         })

"""