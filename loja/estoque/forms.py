from django import forms
from .models import Pedido_ordem, Cliente 
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.models import User


class Checar_PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_ordem
        fields=['ordenado_por','endereco_envio','telefone','email', 'pagamento_metodo']
        # widgets = {
        #     'ordenado_por':TextInput(attrs={
        #         'class':'form-control',
        #         'style':'max-width: 300px;',
        #         'placeholder':'ordenado_por'
        #     }),
        #     'endereco_envio':TextInput(attrs={
        #         'class':'form-control',
        #         'style':'max-width: 300px;',
        #         'placeholder':'endereco envio'
        #     }),
        #     'telefone':TextInput(attrs={
        #         'class':'form-control',
        #         'style':'max-width: 300px;',
        #         'placeholder':'telefone'
        #     }),
        #     'email':EmailInput(attrs={
        #         'class':'form-control',
        #         'style':'max-width: 300px;',
        #         'placeholder':'email'
        #     }),
        # }
        

class ClienteRegistrarForm(forms.ModelForm):
    # usuario = forms.CharField(widget=forms.TextInput(attrs={
    #             'class':'form-control',
    #             'style':'max-width: 300px;',
    #             'placeholder':'usuario'
    #         }))
    # senha = forms.CharField(widget=forms.PasswordInput(attrs={
    #             'class':'form-control',
    #             'style':'max-width: 300px;',
    #             'placeholder':'senha'
    #         }))
    # email = forms.CharField(widget=forms.EmailInput(attrs={
    #             'class':'form-control',
    #             'style':'max-width: 300px;',
    #             'placeholder':'email'
    #         }))

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())



    class Meta:
        model = Cliente
        fields=['username','password','email','nome_completo','endereco']
        # widgets = {                             
        #     'nome_completo':TextInput(attrs={
        #         'class':'form-control',
        #         'style':'max-width: 300px;',
        #         'placeholder':'Nome completo'
        #     }),
        #     'endereco':TextInput(attrs={
        #         'class':'form-control',
        #         'style':'max-width: 300px;',
        #         'placeholder':'endereco'
        #     }),
        
        # }
    
    def clean_username(self):
        unome = self.cleaned_data.get('username')
        if User.objects.filter(username=unome).exists():
            raise forms.ValidationError('Este cliente ja existe no banco de dados')
        return unome


class ClienteEntrarForm(forms.Form):   
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

 