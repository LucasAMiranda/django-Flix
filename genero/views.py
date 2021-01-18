from django.shortcuts import render
from . import forms
from . import models


# Create your views here.

def cadastro(request):
    print("insert")
    print(request.method);
    form = forms.GeneroForm()
    if request.method == 'POST':
        form = forms.GeneroForm(request.POST)
        if form.is_valid():
            print("Saving")
            form.save(commit=True)
        else:
            print("ERROR")
    genero_list = models.Genero.objects.order_by('descricao')
    data_dict = {'form':form , 'genero_records': genero_list}

    return render(request, 'genero/genero.html', data_dict)