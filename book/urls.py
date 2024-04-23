from django.urls import path
urlpatterns=[
    path('List/',book_list,name='book_list'),
    path('Add/',book_add,name='book_add'),
    path('Update/<str:name>/',book_update,name='book_update'),
    path('Delete/<int:id>/',book_delete,name='book_delete'),
    path('Details/<int:id>/',book_details,name='book_details'),
]