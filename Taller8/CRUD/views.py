from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from .forms import PersonaForm
from django.views.generic import ListView, DetailView

# Create your views here.

class IndexView(ListView):
    template_name = 'CRUD/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Persona.objects.all()

class ContactDetailView(DetailView):
    model = Persona
    template_name = 'CRUD/contact-detail.html'

# CRUD.

def create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = PersonaForm()

    return render(request,'CRUD/create.html',{'form': form})

def edit(request, pk, template_name='CRUD/edit.html'):
    persona = get_object_or_404(Persona, pk=pk)
    form = PersonaForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='CRUD/confirm_delete.html'):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method=='POST':
        Persona.delete()
        return redirect('index')
    return render(request, template_name, {'object':persona})