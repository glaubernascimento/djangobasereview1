from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet
from .models import Pessoa, Telefone


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'idade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = ['numero']
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero'].required = False


class TelefoneBaseFormSet(BaseInlineFormSet):
    def save_existing(self, form, instance, commit=True):
        if not form.cleaned_data.get('numero'):
            instance.delete()
            return instance
        return super().save_existing(form, instance, commit=commit)


TelefoneFormSet = inlineformset_factory(
    Pessoa,
    Telefone,
    form=TelefoneForm,
    formset=TelefoneBaseFormSet,
    extra=1,
    can_delete=True,
)
