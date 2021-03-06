from django.conf.urls import url
from apps.Formacion_Academica.models import formacion_academica
from apps.Formacion_Academica.views import CreateFormacion_Academica,ListFormacion_Academica,UpdateFormacion_Academica,DeleteFormacion_Academica

urlpatterns = [

    url(r'^CrearFormacion_Academica$',CreateFormacion_Academica.as_view(), name="create_Formacion_Academica"),
   url(r'^ListarFormacion_Academica',ListFormacion_Academica.as_view(queryset=formacion_academica.objects.all().order_by('id')), name="lista_Formacion_Academica"),
   url(r'^UpdateFormacion_Academica/(?P<pk>\d+)/$',UpdateFormacion_Academica.as_view(), name="update_Formacion_Academica"),
   url(r'^DeleteFormacion_Academica/(?P<pk>\d+)/$',DeleteFormacion_Academica.as_view(), name="delete_Formacion_Academica"),

]