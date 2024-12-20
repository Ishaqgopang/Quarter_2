# -*- coding: utf-8 -*-
"""my chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ti63UxGT_V5oh4oJgbUU1IOz98sOax3z
"""

from google.colab import userdata
userdata.get('GOOGLE_API_KEY')

!pip install -q -U google.generativeai

import google.generativeai as genai

genai.configure(api_key= "AIzaSyBQUxilDPzl_9en_ju2GqEuMJQW7_C_MnQ")

model_name = "gemini-1.5-flash"

model = genai.GenerativeModel(model_name)

response = model.generate_content ("""Objective:
This assignment is designed to deepen your understanding of the parameters used with the OpenAI Chat Completion API. You will explain the purpose and functionality of the following terms or parameters in your own words.

Terms/Parameters to Explain:
Messages
Model
Max Completion Tokens
n
Stream
Temperature
Top_p
Tools""")

print(response.text)