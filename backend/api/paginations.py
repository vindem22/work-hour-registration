from rest_framework.pagination import (
    PageNumberPagination,
    CursorPagination,
    LimitOffsetPagination,
)
from rest_framework.response import Response

class Pagination(object):
    @classmethod
    def number_of_pages(cls, num_of_instances, instances_per_page=12):
        num_of_pages = (
            (num_of_instances // instances_per_page)
            if num_of_instances % instances_per_page == 0
            else (num_of_instances // instances_per_page) + 1
        )
        return num_of_pages

class CustomDefaultPagination(PageNumberPagination, Pagination):
    page_size = 12
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data, *args, **kwargs):
        num_of_instances = self.page.paginator.count
        self.page_size = self.get_page_size(self.request)
        return Response(
            {
                'data': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link(),
                    'page': self.number_of_pages(
                        self.page.paginator.count, self.page_size
                    ),
                    'per_page': self.page_size,
                    'current_page': self.page.number,
                    'total': num_of_instances,
                    'data': data,
                }
            }
        )       