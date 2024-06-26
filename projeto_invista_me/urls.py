from django.contrib import admin
from django.urls import path
from invista_me import views
from usuarios import views as usuarios_vw
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('conta', usuarios_vw.novo_usuario, name= 'novo_usuario'),
    path('login', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name= 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name= 'logout'),
    path('', views.investimento, name= 'investimento'),
    path('novo_investimento', views.criar, 
        name= 'novo_investimento'),
    path('novo_investimento/<int:id_investimento>', views.editar, 
        name= 'editar'),
    path('excluir/<int:id_investimento>', views.excluir, 
        name= 'excluir'),
    path('<int:id_investimento>', views.detalhes, 
    name= 'detalhes'),
]
