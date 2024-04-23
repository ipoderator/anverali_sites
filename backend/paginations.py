from rest_framework.pagination import PageNumberPagination

from anverali_sites.settings import PAGE_SIZE


class VacanciescPagination(PageNumberPagination):
    """Пагинация для раздела вакансии."""
    page_size = PAGE_SIZE
    page_size_query_param = 'limit'
