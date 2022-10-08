from django.urls import path
from relationships import views

urlpatterns = [
	path("send_jsons",views.send_jsons,name="send_jsons"),
	path("send_json/<int:id>",views.send_json,name="send_json"),
	path("logout",views.logout_request,name="logout"),
	path("login",views.login_request,name="login"),

	path('list', views.list_table, name='list_table'),
	path('add', views.add_table, name='add_table'),
	path('update/<int:id>', views.update_table, name='update_table'),
	path('delete/<int:id>', views.delete_table, name='delete_table'),
	
	path('list_mark/<int:id>', views.list_mark, name='list_mark'),
	path('add_marks', views.add_marktable, name='add_marktable'),
	path('update_marks/<int:id>', views.update_marktable, name='update_marktable'),
	path('delete_marks/<int:id>', views.delete_marktable, name='delete_marktable'),
	
	#path('add_marks', views.add_marks, name='add_marks'),
    #path('add_students', views.add_students, name='add_students'),
    #path('add_persons', views.add_persons, name='add_persons'),
    #path('add_aadhars', views.add_aadhars, name='add_aadhars'),
]
