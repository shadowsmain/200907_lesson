import
import requests

print(random.random())

response = requests.get('https://yan.ru')
print(response)
print(response.content)


# faces_marks = face_recognition.face_encodings()



#dependencies:
#requests
#pillow
#numpy


#pip freeze+ 3 библиотеки