from django.urls import path

from backend.views import (
    UserRegistrationCreateView,
    CustomerProfileRetrieveView,
    PerformerProfileRetrieveView,
    SearchVacanciesListView
)

urlpatterns = [
    path('registration/',
         UserRegistrationCreateView.as_view(),
         name='registration'
         ),
    path('customer_profile/<slug:slug>/',
         CustomerProfileRetrieveView.as_view(),
         name='customer_profile'
         ),
    path('performer_pofile/<slug:slug>/',
         PerformerProfileRetrieveView.as_view(),
         name='performer_pofile'
         ),
    path('search_vacancies/',
         SearchVacanciesListView.as_view(),
         name='search_vacancy'
         ),
]
