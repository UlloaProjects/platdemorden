from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, DetailView, ListView

from toy_app import forms
from toy_app.forms import UploadFilesForm
from toy_app.models import User, ProductDemand, Product, PronosticoSES
from django.contrib.auth.decorators import login_required
import csv


def index(request):
    return render(request, 'toy_app/project_app/index.html')


class Register(View):
    form_class = forms.SignUpForm
    template = 'registration/signup.html'

    def get(self, request):
        # mostrar formulario de registro
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request):
        # procesar formulario de registro
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.save()

            return render(request, 'toy_app/project_app/index.html')
        else:
            print('error')
            print(form.errors)
            return render(request, self.template, {'form': form})


def Inputfiles(request):
    form = UploadFilesForm(request.POST, request.FILES, instance=request.user)
    if request.method == "POST":

        if form.is_valid():
            form.save()

            return redirect('index')
        else:
            form = UploadFilesForm()

        return render(request, 'registration/File_Upload.html', {'form': form})
    else:
        return render(request, 'registration/File_Upload.html', {'form': form})


class UserUpdateView(UpdateView):
    fields = ("file_one", "file_two")
    model = User


class UserDetailView(DetailView):
    model = User
    template_name = 'toy_app/project_app/User_detail_view.html'


@login_required
def proc_dem_file(request):
    demfile = request.user.file_one.path
    with open(demfile, newline='') as f:

        reader = csv.reader(f, delimiter=';', skipinitialspace=True, strict=True)
        firstline = True
        for row in reader:
            if firstline:
                firstline = False
            else:
                material = row[1]
                oficina = row[0]
                txt_breve = row[2]
                product, created = Product.objects.get_or_create(material=material, owner=request.user,
                                                                 oficina=oficina,
                                                                 texto_breve_material=txt_breve)
                date_string = row[3]
                print(date_string)
                date = datetime.strptime(date_string, '%d/%m/%Y')
                mes_string = row[4]
                anno_string = row[5]
                demand_string = row[6]
                demand = int(demand_string)
                mes = int(mes_string)
                anno = int(anno_string)
                ProductDemand.objects.get_or_create(
                    product=product,
                    date=date,
                    mes=mes,
                    anno=anno,
                    demand=demand)

    return render(request, 'toy_app/project_app/index.html')


def funcion_demandas(request):
    print("inicio demanda")
    p = Product.objects.filter(owner=request.user)
    ses = 0
    print(len(p))


    for product in p:
        all_demands = []
        for item in product.demands.all().order_by('date'):
            all_demands.append(item)

        # END FOR product demands
        print("meterial de turno")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~  " + product.material + "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        mes = 1
        var = len(all_demands)
        n = 1
        demanda_mensual = all_demands[0].demand
        demanda_anual = all_demands[0].demand
        while n < var:
            print("valor de n es:")
            print(n)
            print(all_demands[n - 1].date)
            mes_ini = all_demands[n - 1].mes
            year_ini = all_demands[n - 1].anno
            mes_post = all_demands[n].mes
            year_post = all_demands[n].anno
            my_demand = all_demands[n].demand
            demanda_anual += my_demand
            if mes_ini == mes_post and year_ini == year_post:
                demanda_mensual = demanda_mensual + my_demand
                print(demanda_mensual)
            else:
                print("no entro al if")
                print(demanda_mensual)
                forecast, created = PronosticoSES.objects.get_or_create(owner=product)
                forecast.monthly_demand.append(1,demanda_mensual)
                demanda_mensual = 0

            n += 1

        print(demanda_anual)
    return render(request, 'toy_app/project_app/User_detail_view.html')


def metodo_ses(request):
    p = Product.objects.filter(owner=request.user)
    flag = True
    forecast = 0
    n = 1

    for i in p:
        lista = PronosticoSES.objects.filter(owner=i)
        for f in lista.monthly_demand:
            print("hola")
            if len(f) == 12:
                if flag:
                    forecast = f[0]
                    flag = False
                else:
                    forecast = forecast * 0.9 * (f[n - 1] - forecast)
                    n += 1
        i.demanda_ses = forecast




class ProductView(ListView):
    context_object_name = "productos"
    model = Product
