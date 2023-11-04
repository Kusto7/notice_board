from rest_framework.pagination import PageNumberPagination


class AdsPaginator(PageNumberPagination):
    page_size = 10


class CommentsPaginator(PageNumberPagination):
    page_size = 10
