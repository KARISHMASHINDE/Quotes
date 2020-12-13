from django.urls import path
from Myapp import views

urlpatterns = [
    path('quotes/', views.QuoteList.as_view()),
    path('quote/<int:pk>/', views.QuoteEdit.as_view()),
]