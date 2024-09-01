from django import forms
from cars.models import Brand, Car



    #reescrevendo código acima de forma mais rápida 

class carModelForm(forms.ModelForm): #isso é a mesma coisa de tudo acima, graças ao django
    class Meta:
        model =Car
        fields = '__all__'

    def clean_value(self): # tem que começar com clean para que o django saiba o que é! 
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'valor minimo do carro deve ser maior que R$20.000')
