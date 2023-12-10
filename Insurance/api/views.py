from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
import joblib

import pandas as pd
import os
from .serializers import InsuranceSerializer
import sklearn
print(sklearn.__version__)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
#get the path to the pickled model file
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','Model','InsuranceCostPredictor.pkl')

# load the pickled model
model = joblib.load(model_path)


@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        # deserialize the input data from the request
        serializer = InsuranceSerializer(data=request.data)
        if serializer.is_valid():
            # convert input data to input format for the model
          
            input_data = tuple(serializer.validated_data.values())
            input_data_as_numpy_array = np.asarray(input_data)
            
            new_data_encoded_array = input_data_as_numpy_array.reshape(1,-1)

            
            new_predictions = model.predict(new_data_encoded_array)    
          
            

            # return the prediction as a JSON response
            return Response(new_predictions)
        else:
            # Handle the case where the serializer is not valid
            return Response(serializer.errors, status=400)
    else:
        # Handle the case where the request method is not POST
        return Response({"error": "Invalid request method"}, status=405)
###password :vnrvjiet
###pip install django-cors-headers numpy joblib scikit-learn pandas