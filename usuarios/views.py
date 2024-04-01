from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import userRegisterForm

def novo_usuario(request):
    if request.method == 'POST':
        formulario = userRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O usuario {usuario}, foi criado com sussesso!')
            return redirect('login')
    else:
        formulario = userRegisterForm()

        
    return render(request, 'usuarios/registrar.html', {'formulario': formulario})