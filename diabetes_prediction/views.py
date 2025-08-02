from django.shortcuts import render
from .forms import PredictionForm
import pickle
import numpy as np
import os
from django.conf import settings

# Load model and scaler using absolute paths
model_path = os.path.join(settings.BASE_DIR, 'rf_model.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'scaler.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

def home(request):
    result = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = [
                form.cleaned_data['Pregnancies'],
                form.cleaned_data['Glucose'],
                form.cleaned_data['BloodPressure'],
                form.cleaned_data['SkinThickness'],
                form.cleaned_data['Insulin'],
                form.cleaned_data['BMI'],
                form.cleaned_data['DiabetesPedigreeFunction'],
                form.cleaned_data['Age']
            ]
            data = np.array(data).reshape(1, -1)
            data_scaled = scaler.transform(data)
            prediction = model.predict(data_scaled)[0]
            result = "Diabetic" if prediction == 1 else "Not Diabetic"
    else:
        form = PredictionForm()
    return render(request, 'home.html', {'form': form, 'result': result})
