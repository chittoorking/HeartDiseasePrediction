#!/usr/bin/env python
# coding: utf-8

# In[2]:


endpoint = 'http://e4b10aeb-474a-4fc2-b275-846337b3ab00.centralindia.azurecontainer.io/score' #Replace with your endpoint
key = 'zrkbjURc2NK5zIdakgUdNEdRHPBhA4U6' #Replace with your key

import urllib.request
import json
import os

data = {
    "Inputs": {
        "WebServiceInput0":
        [
            {
                    'Id': 188,
                    'age': 23,
                    'sex': 1,
                    'cp': 3,
                    'trestbps': 145,
                    'chol': 234,
                    'fbs': 1,
                    'restecg': 0,
                    'thalach':150,
                    'exang':0,
                    'oldpeak':2.3,
                    'slope':2,
                    'ca':0,
                    'thal':2
            },
        ],
    },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}

req = urllib.request.Request(endpoint, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    json_result = json.loads(result)
    output = json_result["Results"]["WebServiceOutput0"][0]
    print('Patient: {}\nPrediction: {}\nProbability: {:.2f}'.format(output["Id"],
                                                            output["HeartDiseasePrediction"],
                                                            output["Probability"]))
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers to help debug
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))

