from django.urls import path
from .views import *

urlpatterns = [
	path('list/',StudentList.as_view()),	
	path('detail/<pk>',StudentDetail.as_view()),
	path('create/',StudentCreate.as_view()),
	path('update/<pk>',StudentUpdate.as_view()),
	path('delete/<pk>',StudentDelete.as_view()),
]
