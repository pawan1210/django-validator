from django.urls import path
from .views import FiniteValuesEntityView, NumericEntityView

urlpatterns = [
    path("finite-values-entity", FiniteValuesEntityView.as_view()),
    path("numeric-entity", NumericEntityView.as_view()),
]