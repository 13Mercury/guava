from django.http import *
from .forms import Users_Form,AreaForm, FotoForm, PeticionForm, AportacionForm,PhotoForm, InfoForm
from .models import Usuario, Area_Verde, Foto, Aportacion, Peticion, Adopcion
from django.views import View
from django.views.generic import FormView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from datetime import datetime
# Create your views here.


class Signup(View):
    template_name = "modals/signup.html"
    form_class = Users_Form
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        dic = request.session.get('message')
        request.session['message'] = ""
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, "errors" : dic})

    def post(self, request, *args, **kwargs):
        #print("form")
        form = self.form_class(request.POST)
        if form.is_valid():
            #print("if")
            request.session['message'] = ""
            user = form.save()
            a = Usuario()
            a.username = user
            a.nombre = form.cleaned_data["nombre"]
            a.telefono = form.cleaned_data["telefono"]
            a.email = form.cleaned_data["email"]
            a.save()
            return redirect("/")


        #print(form.errors)
        request.session['message'] = form.errors
        messages.add_message(request, messages.INFO, form.errors)
        return redirect("/")

class Info(View):
    template_name = "modals/info.html"
    form_class = InfoForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        dic = request.session.get('message')
        request.session['message'] = ""
        a = Usuario.objects.get(username_id=kwargs["uu"])
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, "errors" : dic, "user":a})

    def post(self, request, *args, **kwargs):
        #print("form")
        form = self.form_class(request.POST)
        if form.is_valid():
            uu = request.POST["next"]
            #print("if")
            request.session['message'] = ""
            a = Usuario.objects.get(username_id=uu)

            a.nombre = form.cleaned_data["nombre"]
            a.descripcion = form.cleaned_data["descripcion"]
            a.direccion = form.cleaned_data["direccion"]
            a.telefono = form.cleaned_data["telefono"]
            a.pagina = form.cleaned_data["pagina"]
            a.email = form.cleaned_data["email"]
            a.save()
            return redirect("/perfil/" + uu )


        #print(form.errors)
        request.session['message'] = form.errors
        messages.add_message(request, messages.INFO, form.errors)
        return redirect("/perfil/" + request.POST["next"])


class Arboles(View):
    template_name = "modals/tree.html"
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        a = Usuario.objects.get(username_id=kwargs["uu"])
        return render(request, self.template_name, {"cc":a})

    def post(self, request, *args, **kwargs):
        uu = request.POST["next"]
        a = Usuario.objects.get(username_id=uu)
        a.arboles = request.POST["arboles"]
        a.save()
        return redirect("/perfil/"+uu)

class Photo(View):
    template_name = "modals/perfilFoto.html"
    form_class = PhotoForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        a = Usuario.objects.get(username_id=kwargs["uu"])
        return render(request, self.template_name, {"cc":a})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        uu = request.POST["next"]
        if form.is_valid():

            a = Usuario.objects.get(username_id=uu)
            a.image = form.cleaned_data["image"]

            a.save()
            return redirect("/perfil/"+uu)

class Login(View):
    template_name = "modals/login.html"
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        dic = request.session.get('message')
        request.session['message'] = ""
        return render(request, self.template_name, { "errors" : dic})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session['user'] = user.pk
                request.session['message'] = ""
                login(request, user)
                return redirect("/")


        request.session['message'] = "Usuario y/o contraseña incorrecto"
        messages.add_message(request, messages.INFO, "Usuario y/o contraseña incorrecto")
        return redirect("/")

class NewArea(View):
    template_name = "modals/newArea.html"
    form_class = AreaForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        dic = request.session['message']
        request.session['message'] = ""
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, "errors" : dic})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            uu = request.POST["next"]
            a = Usuario.objects.get(username_id=uu)
            z = Area_Verde()
            z.nombre = request.POST["nombre"]
            z.ubicacion = request.POST["ubicacion"]
            z.direccion = request.POST["direccion"]
            z.creador = a
            z.encargado = a
            z.enAdopcion = ""
            z.save()
            return redirect("/areas/")

        request.session['message'] = "Nombre del area debe contener solo letras"
        messages.add_message(request, messages.INFO, "Nombre del area debe contener solo letras")
        return redirect("/perfil/" + request.POST["next"])

class NewFoto(View):
    template_name = "modals/newFoto.html"
    form_class = FotoForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        uu = kwargs["uu"]
        aa = kwargs["aa"]
        aa = kwargs["aa"]

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, "u":uu,"a":aa})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        aa = kwargs["aa"]
        if form.is_valid():

            form.save()
            return redirect("/areas/"+aa)


class NewPeticion(View):
    template_name = "modals/newPeticion.html"
    form_class = PeticionForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        uu = kwargs["uu"]
        aa = kwargs["aa"]
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, "u":uu,"a":aa})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            uu = kwargs["uu"]
            aa = kwargs["aa"]

            u = Usuario.objects.get(username_id=uu)
            a = Area_Verde.objects.get(id=aa)

            z = Peticion()
            z.peticion = request.POST["peticion"]
            z.comentario = request.POST["comentario"]
            z.hechaPor = u
            z.paraArea = a
            z.arbolesTotales = 0
            z.save()
            return redirect("/areas/"+aa)

class NewAportacion(View):
    template_name = "modals/newAportacion.html"
    form_class = AportacionForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        uu = kwargs["uu"]
        aa = kwargs["aa"]
        pp = kwargs["pp"]
        u = Usuario.objects.get(username_id=uu)
        p = Peticion.objects.get(id=pp)
        a = Area_Verde.objects.get(id=aa)
        t = int(p.peticion) - int(p.arbolesTotales)
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, "u":u,"p":p, "a":a, "total":t})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            uu = kwargs["uu"]
            aa = kwargs["aa"]
            pp = kwargs["pp"]

            u = Usuario.objects.get(username_id=uu)
            p = Peticion.objects.get(id=pp)
            a = Area_Verde.objects.get(id=aa)

            z = Aportacion()
            z.aportacion = request.POST["aportacion"]
            z.respondiendoPeticion = p
            z.comentario = request.POST["comentario"]
            z.hechaPor = u
            z.paraArea = a
            z.save()

            u.arboles = u.arboles - int(request.POST["aportacion"])
            u.save()

            p.arbolesTotales = p.arbolesTotales  + int(request.POST["aportacion"])
            if p.arbolesTotales >= p.peticion:
                p.abierta=False;
            p.save()
            return redirect("/areas/"+aa)

@login_required()
def logout_view(request):
    logout(request)
    request.session['user'] = ""
    return redirect("/")

@login_required()
def perfil(request, uu):

    dic = []
    u = ""
    if 'user' in request.session:
        u = request.session['user']

    ux = Usuario.objects.get(username_id=uu)
    u = ""
    if 'user' in request.session:
        u = request.session['user']


    if 'message' in request.session:
        dic = request.session.get('message')

    cc = []
    se = []
    #Todas
    ob = Area_Verde.objects.all()

    #No encargado y Si encargado
    if u != "":
        cc = Area_Verde.objects.raw('SELECT * FROM GuavaApp_area_verde WHERE encargado_id <> %s' % u)
        se = Area_Verde.objects.all().filter(encargado = u)
    context = {
    "otro":"si",
    "user":ux,
    'ob': ob,
    'se': se,
    "errors" : dic
    }
    print(dic)
    return render(request, "perfil.html", context)

def index(request):
    u = ""
    if 'user' in request.session:
        u = request.session['user']

    cc = []
    se = []
    #Todas
    ob = Area_Verde.objects.all()

    #No encargado y Si encargado
    if u != "":
        cc = Area_Verde.objects.raw('SELECT * FROM GuavaApp_area_verde WHERE encargado_id <> %s' % u)
        se = Area_Verde.objects.all().filter(encargado = u)
    context = {
    "otro":"no",
    'ob': ob,
    'se': se,
    }
    return render(request, 'index.html',context)

def areas(request):
    u = ""
    if 'user' in request.session:
        u = request.session['user']

    cc = []
    se = []
    #Todas
    ob = Area_Verde.objects.all()

    #No encargado y Si encargado
    if u != "":
        cc = Area_Verde.objects.raw('SELECT * FROM GuavaApp_area_verde WHERE encargado_id <> %s' % u)
        se = Area_Verde.objects.all().filter(encargado = u)

    #adopcion
    if u != "":
        ad = Area_Verde.objects.raw('SELECT * FROM GuavaApp_area_verde WHERE enAdopcion <> "" AND  encargado_id <> %s' % u)
    else:
        ad = Area_Verde.objects.raw('SELECT * FROM GuavaApp_area_verde WHERE enAdopcion <> "" ')
    #PETICIONES abierta
    pt = Area_Verde.objects.raw('SELECT * FROM GuavaApp_area_verde INNER JOIN GuavaApp_peticion on GuavaApp_peticion.paraArea_id = GuavaApp_area_verde.id  WHERE GuavaApp_peticion.abierta = 1')

    context = {
    'ob': ob,
    'cc': cc,
    'se': se,
    'ad': ad,
    'pt': pt
    }
    return render(request, 'areas.html', context)

def areaSelect(request, uu):
    u = ""
    if 'user' in request.session:
        if request.session['user'] !="":
            u = Usuario.objects.get(username_id=request.session['user'])

    ob = Area_Verde.objects.get(id=uu)
    ft = Foto.objects.all() .filter(areaPertenece=ob)
    ad = Adopcion.objects.all().filter(paraArea=ob)
    pt = Peticion.objects.all().filter(paraArea=ob, abierta=1)
    ap = Aportacion.objects.all().filter(paraArea=ob)

    alls = Area_Verde.objects.all()

    context = {
    "user" : u,
    'ob': ob,
    'all': alls,
    'ft': ft,
    'ad': ad,
    'pt': pt,
    'ap': ap
    }
    return render(request, 'areaSelect.html', context)

def PonerAdopcionView(request, uu, aa):
    u = Usuario.objects.get(username_id=uu)
    ob = Area_Verde.objects.get(id=aa)

    ad = Adopcion()
    ad.creadaPor = u
    ad.adoptadaPor = u
    ad.paraArea = ob
    ad.fechaCreacion = datetime.now()
    print(ad,ad.creadaPor,ad.paraArea,ad.fechaCreacion)
    ad.save()

    ob.enAdopcion = ad.id
    ob.save()

    return redirect("/areas/"+aa)

def QuitarAdopcionView(request, uu, aa):
    u = Usuario.objects.get(username_id=uu)
    ob = Area_Verde.objects.get(id=aa)

    Adopcion.objects.filter(id=ob.enAdopcion).delete()

    ob.enAdopcion = ""
    ob.save()

    return redirect("/areas/"+aa)

def AdoptarView(request, uu, aa):
    u = Usuario.objects.get(username_id=uu)
    ob = Area_Verde.objects.get(id=aa)

    ad = Adopcion.objects.get(id=ob.enAdopcion)
    ad.adoptadaPor = u
    ad.fechaAdopcion = datetime.now()
    ad.save()

    ob.encargado = u
    ob.enAdopcion = ""
    ob.save()

    return redirect("/areas/"+aa)
