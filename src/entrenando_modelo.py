import cv2
import os
import numpy as np

dataPath = "../data/pruebas/reconocidos"
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

# labels = []
# facesData = []
# label = 0

# for nameDir in peopleList:
#     personPath = dataPath + '/' + nameDir
#     print('Leyendo las imágenes')

#     for fileName in os.listdir(personPath):
#         print('Rostros: ', nameDir + '/' + fileName)
#         labels.append(label)
#         facesData.append(cv2.imread(personPath+'/'+fileName,0))
#         #image = cv2.imread(personPath+'/'+fileName,0)
#         #cv2.imshow('image',image)
#         #cv2.waitKey(10)
#     label = label + 1

# print('labels= ',labels)
# print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))
# print('Número de etiquetas 1: ',np.count_nonzero(np.array(labels)==1))
# # print('Número de etiquetas 2: ',np.count_nonzero(np.array(labels)==2))

# face_recognizer = cv2.face.EigenFaceRecognizer_create()
# # face_recognizer = cv2.face.FisherFaceRecognizer_create()
# # face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# # Entrenando el reconocedor de rostros
# print("Entrenando...")
# face_recognizer.train(facesData, np.array(labels))

# face_recognizer.save('../modelos/modeloLBPHFace.xml')
# print("Modelo almacenado...")


labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = os.path.join(dataPath, nameDir)
    print("Leyendo las imágenes de", nameDir)

    for fileName in os.listdir(personPath):
        print("Rostros:", os.path.join(nameDir, fileName))
        labels.append(label)
        facesData.append(cv2.imread(os.path.join(personPath, fileName), 0))

    label += 1

# Crear el objeto reconocedor de rostros EigenFace
face_recognizer = cv2.face.EigenFaceRecognizer_create()

# Entrenar el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Almacenar el modelo obtenido
face_recognizer.save("../modelos/modeloEigenFace.xml")

print("Modelo almacenado...")
