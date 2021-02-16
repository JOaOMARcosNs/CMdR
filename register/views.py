from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

import xlwt
from django.http import HttpResponse

from .models import Nationality, About, Homeless, Addiction, Disease
from .forms import HomelessForm

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_list_or_404

# Create your views here.

######################################################### CreateView #########################################################
class NationalityCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admins", u"user"]
    login_url = reverse_lazy('login')
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-nationality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cadastro de nacionalidade"
        context['button'] = "Cadastrar"
        

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid   
 


class AboutCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = About
    fields = ['description','history','sexual_orientation','breed','ethnicity','school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-about')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cadastro das historias/sobre"
        context['button'] = "Cadastrar"
        

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid 

class HomelessCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    form_class = HomelessForm
    model = Homeless
    template_name = 'register/form-homeless.html'
    success_url = reverse_lazy('list-homeless')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cadastro de sem-teto"
        context['button'] = "Cadastrar"
        

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid     
class AddictionCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Addiction
    fields = ['name_addiction', 'type_addiction', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-addiction')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cadastro de vício"
        context['button'] = "Cadastrar"
        

        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid  

class DiseaseCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Disease
    fields = ['name_disease', 'type_disease', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-disease')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cadastro de doença"
        context['button'] = "Cadastrar"
        

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid 

######################################################### UpdateView  #########################################################

class NationalityUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Nationality
    fields = ['city', 'state']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-nationality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar o registro de nacionalidade cadastrada"
        context['button'] = "Salvar"

        return context


class AboutUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = About
    fields = ['description', 'history', 'sexual_orientation', 'breed', 'ethnicity', 'school_level']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-about')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar o registro de história/sobre cadastrada"
        context['button'] = "Salvar"

        return context

class HomelessUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Homeless
    fields = ['frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-homeless')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar o registro do sem-teto cadastrado"
        context['button'] = "Salvar"

        return context

class AddictionUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Addiction
    fields = ['name_addiction', 'type_addiction', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-addiction')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar o registro de vício cadastrado"
        context['button'] = "Salvar"

        return context

class DiseaseUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Disease
    fields = ['name_disease', 'type_disease', 'homeless']
    template_name = 'register/form.html'
    success_url = reverse_lazy('list-disease')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar o registro da doença cadastrada"
        context['button'] = "Salvar"

        return context


######################################################### DeleteView  #########################################################

class NationalityDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = Nationality
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-nationality')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Excluir cadastro de nacionalidade"

        return context

    

class AboutDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = About
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-about')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Excluir cadastro de Historia/sobre"

        return context


class HomelessDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = Homeless
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-homeless')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Deletar cadastro do sem-teto"

        return context

class AddictionDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = Addiction
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-addiction')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Deletar cadastro de vícios"

        return context

class DiseaseDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admins"
    model = Disease
    template_name = 'register/form-excluir.html'
    success_url = reverse_lazy('list-disease')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Deletar cadastro de doença"

        return context


######################################################### ListeView  #########################################################

class NationalityList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Nationality
    template_name =  'register/list/natiomality.html'


class AboutList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = About
    template_name = 'register/list/about.html'


class HomelessList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Homeless
    template_name = 'register/list/homeless.html'

class AddictionList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Addiction
    template_name = 'register/list/addiction.html'

class DiseaseList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"admins", u"user"]
    model = Disease
    template_name = 'register/list/disease.html'

######################################################### export xls Nationality #########################################################

# from .models import Nationality, About, Homeless, Addiction, Disease

def export_nationality_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="nacionalidade.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Nationality Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Cidade', 'Estado']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Nationality.objects.all().values_list('city', 'state')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

######################################################### export xls About #########################################################

def export_about_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="descrição-dos-sem-tetos.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('About Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Descrição', 'História','Orientação sexual','Raça','Etnia','Níveis de escolaridade']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = About.objects.all().values_list('description', 'history','sexual_orientation','breed','ethnicity','school_level')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

######################################################### export xls Homeless #########################################################

def export_homeless_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Sem-teto.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Homeless Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Primeiro nome','Segundo nome','Apelido','Data de nascimento','Gênero','CPF','RG','Órgão expedidor','Altura','Peso','Tipo sanguíneo','Nacionalidade','História/Sobre']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Homeless.objects.all().values_list('frist_name','second_name','nickname','birth_date','gender','cpf','rg','issuing_body','height','weight','blood_type','nationality','about')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

######################################################### export xls Addiction #########################################################

def export_addiction_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Vícios.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Addiction Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nome do vício','Tipo do vício','Sem-teto']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Addiction.objects.all().values_list('name_addiction','type_addiction','homeless')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
######################################################### export xls Disease #########################################################
# name_disease = models.CharField(max_length=90, verbose_name='Nome da doença')
#       type_disease = models.CharField(max_length=90, verbose_name='Tipo da doença')
#       homeless = models.ForeignKey('Homeless', on_delete=models.PROTECT, verbose_name='Sem-teto')
#       user = models.ForeignKey(User, on_delete=models.PROTECT)

def export_disease_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Doenças.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Disease Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nome da doença','Tipo da doença','Sem-teto']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Disease.objects.all().values_list('name_disease','type_disease','homeless')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response