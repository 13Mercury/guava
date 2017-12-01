from django.conf.urls import url
from django.contrib.auth.views import LoginView, login
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^areas/$', views.areas, name="areas"),
    url(r'^areas/(?P<uu>\w{0,50})$', views.areaSelect, name="areasSelect"),
    url(r'^areas/aportacion/(?P<uu>\w{0,50})/(?P<aa>\w{0,50})/(?P<pp>\w{0,50})$', views.NewAportacion.as_view(), name='NewAportacion_view'),
    url(r'^areas/peticion/(?P<uu>\w{0,50})/(?P<aa>\w{0,50})$', views.NewPeticion.as_view(), name='NewPeticion_view'),
    url(r'^areas/foto/(?P<uu>\w{0,50})/(?P<aa>\w{0,50})$', views.NewFoto.as_view(), name='NewFoto_view'),
    url(r'^adoptar/(?P<uu>\w{0,50})/(?P<aa>\w{0,50})$', views.AdoptarView, name='Adoptar_view'),
    url(r'^quitar/(?P<uu>\w{0,50})/(?P<aa>\w{0,50})$', views.QuitarAdopcionView, name='QuitarAdopcion_View'),
    url(r'^poner/(?P<uu>\w{0,50})/(?P<aa>\w{0,50})$', views.PonerAdopcionView, name='PonerAdopcion_view'),
    url(r'^register/$', views.Signup.as_view(), name='Signup_view'),
    url(r'^newArea/(?P<uu>\w{0,50})$', views.NewArea.as_view(), name='NewArea_view'),
    url(r'^trees/(?P<uu>\w{0,50})$', views.Arboles.as_view(), name='Arboles_view'),
    url(r'^photo/(?P<uu>\w{0,50})$', views.Photo.as_view(), name='Photo_view'),
    url(r'^info/(?P<uu>\w{0,50})$', views.Info.as_view(), name='Info_view'),
    url(r'^login/$', views.Login.as_view(), name='Login_view'),
    url(r'^logout/$', views.logout_view),
    url(r'^perfil/(?P<uu>\w{0,50})$', views.perfil)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
