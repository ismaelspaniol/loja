from django.urls import path
from .views import *


app_name = 'estoque'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('todos-produtos/', TodosProdutosView.as_view(), name='todosProdutos'),
    path('produto/<slug:slug>/', ProdutoDetalheView.as_view(), name='produtoDetalhe'),
    path('addcarro-<int:prod_id>/', AddCarroView.as_view(), name='addcarro'),
    path('meu-carro/', MeuCarroView.as_view(), name='meucarro'),
    path('manipular-carro/<int:cp_id>/', ManipularView.as_view(), name='manipularcarro'),
    path('limpar-carro/', LimparCarroView.as_view(), name='limparcarro'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]