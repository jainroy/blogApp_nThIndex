from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ConditionalPagination(PageNumberPagination):
    page_size = 2

    def paginate_queryset(self, queryset, request, view=None):
        if queryset.count() <= self.page_size:
            return None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)
