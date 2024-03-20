from django.urls import path
from . import views
urlpatterns=[
#            path("",views.index,name="index"),
#            path("html/",views.index2,name="index2"),
#            path("model/",views.index3,name="index3"),
             path("",views.index4,name="index4"),
             path("add/",views.add,name="add"),
             path("add/addrecord/",views.addrecord,name="addrecord"),
             path("delete/<int:id>",views.delete,name="del"),
             path("update/<int:id>",views.update,name="update"),
             path("update/updaterecord/<int:id>",views.updaterecord,name="del")]