import cv2
import os

dataPath = "../data/pruebas/reconocidos"
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

# #face_recognizer = cv2.face.EigenFaceRecognizer_create()
# #face_recognizer = cv2.face.FisherFaceRecognizer_create()
# face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# # Leyendo el modelo
# #face_recognizer.read('modeloEigenFace.xml')
# #face_recognizer.read('modeloFisherFace.xml')
# face_recognizer.read('../modelos/modeloLBPHFace.xml')

# #cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cap = cv2.VideoCapture("../data/pruebas/nat.mp4")

# faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

# while True:
#     ret,frame = cap.read()
#     if ret == False: break
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     auxFrame = gray.copy()

#     faces = faceClassif.detectMultiScale(gray,1.3,5)

#     for (x,y,w,h) in faces:
#         rostro = auxFrame[y:y+h,x:x+w]
#         rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
#         result = face_recognizer.predict(rostro)

#         cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-5),1,1.3,(0,255,0),1,cv2.LINE_AA)
#         cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

#         '''
#         # EigenFaces
#         if result[1] < 5700:
#             cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
#             cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
#         else:
#             cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
#             cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
#         # FisherFace
#         if result[1] < 500:
#             cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
#             cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
#         else:
#             cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
#             cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
#         # LBPHFace
#         if result[1] < 70:
#             cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
#             cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
#         else:
#             cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
#             cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
#         '''

#         # LBPHFace
#         if result[1] < 70:
#             cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
#             cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
#         else:
#             cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
#             cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            
#     cv2.imshow('frame',frame)
#     k = cv2.waitKey(1)
#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()


face_recognizer = cv2.face.EigenFaceRecognizer_create()

# Leyendo el modelo
face_recognizer.read("../modelos/modeloEigenFace.xml")

# Abriendo el video
cap = cv2.VideoCapture("../data/pruebas/muchas_personas.mp4")

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        # cv2.putText(frame, "{}".format(imagePaths[result[0]]), (x, y-5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # if result[1]<5700:
        #     cv2.putText(frame, "{}".format(result), (x, y-20), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # else:
        #     cv2.putText(frame, "Desconocido", (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Dentro del bucle for donde realizas la predicción
        indice_predicho = result[0]
        distancia_prediccion = result[1]

        # Verificamos si la distancia de la predicción es menor que un umbral
        if distancia_prediccion < 5700:
            nombre_predicho = imagePaths[indice_predicho]
            cv2.putText(frame, nombre_predicho, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Desconocido", (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()