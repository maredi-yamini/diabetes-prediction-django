from django import forms

class PredictionForm(forms.Form):
    Pregnancies = forms.IntegerField()
    Glucose = forms.IntegerField()
    BloodPressure = forms.IntegerField()
    SkinThickness = forms.IntegerField()
    Insulin = forms.IntegerField()
    BMI = forms.FloatField()
    DiabetesPedigreeFunction = forms.FloatField()
    Age = forms.IntegerField()
