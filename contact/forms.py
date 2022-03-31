from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=50, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'}
    ))
    # TextInput le quita la validación a EmailField, debe ser EmailInput
    email = forms.EmailField(label='Email', max_length=50, required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu correo'}
    ))
    message = forms.CharField(label='Mensaje', max_length=300, required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Cuéntanos tus dudas.'}
    )) # No TextField