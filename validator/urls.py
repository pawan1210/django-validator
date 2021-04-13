from django.urls import path
from .views import FiniteValuesEntityView

urlpatterns = [
    path("finite-values-entity", FiniteValuesEntityView.as_view()),
    # path("/numeric-entity",)
]