# -*- coding: latin-1 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from .models import Facultad


class FormularioFacultad(forms.ModelForm):
    class Meta:
        model= Facultad
        fields = ['codigo','nombre']
        widgets={
            'codigo':forms.TextInput(attrs={'class':'form-control','placeholder':'digite codigo'}),
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'digite nombre'}),

        }



