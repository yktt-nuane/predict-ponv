import pickle

from django.shortcuts import render

from .forms import ModelForm


def predict_model(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            smoking_history = form.cleaned_data['smoking_history']
            history_of_PONV = form.cleaned_data['history_of_PONV']
            anxiety = form.cleaned_data['anxiety']

            # Run new features through ML model
            model_features = [
                [age, gender, smoking_history, history_of_PONV, anxiety]]
            loaded_model = pickle.load(
                open("predict_model/ponv_model.pkl", 'rb'))
            prediction = loaded_model.predict(model_features)[0]

            prediction_dict = [{'name':'It is unlikely to be PONV. Prophylactic administration is not recommended.'},{'name':'It is likely to be PONV. Prophylactic administration is recommended.'}]

            prediction_name = prediction_dict[prediction]['name']


            return render(request, 'ponv/home.html', {'form': form, 'prediction': prediction, 'prediction_name': prediction_name})

    # if a GET (or any other method) we'll create a blank form
    else:        
        form = ModelForm()

    return render(request, 'ponv/home.html', {'form': form})
