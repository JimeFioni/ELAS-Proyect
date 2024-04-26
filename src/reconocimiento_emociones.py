import cv2
import os
import pandas as pd

dataPath = "../data/imagenes"

def reconocimiento_emociones(ruta_video, duracion_analisis):
    imagePaths = os.listdir(dataPath)
    emociones_dict = {idx: emocion for idx, emocion in enumerate(imagePaths)}
    
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    face_recognizer.read("../modelos/modeloEigenFaceEmociones2.xml")

    cap = cv2.VideoCapture(ruta_video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duracion_total = frame_count / fps

    if duracion_analisis > duracion_total:
        duracion_analisis = duracion_total

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    df_emociones = []
    personas_detectadas = {}
    contador_personas = 0

    tiempo_final_analisis = duracion_analisis
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

        if frame_time > tiempo_final_analisis:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            persona_id = None
            for coords, pid in personas_detectadas.items():
                cx, cy = coords
                if abs(x - cx) < 100 and abs(y - cy) < 100:
                    persona_id = pid
                    break
            
            if persona_id is None:
                contador_personas += 1
                persona_id = contador_personas
                personas_detectadas[(x, y)] = persona_id

            cv2.putText(frame, str(persona_id), (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro, (48, 48), interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)

            indice_predicho = result[0]
            distancia_prediccion = result[1]

            nombre_predicho = emociones_dict.get(indice_predicho, "Desconocido")
            color = (0, 255, 0) if distancia_prediccion < 5700 else (0, 0, 255)

            cv2.putText(frame, nombre_predicho, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

            df_emociones.append({'Persona': persona_id, 'Emocion': nombre_predicho, 'Tiempo_Inicio': frame_time, 'Tiempo_Fin': frame_time + (1 / fps)})

            print(f'Persona: {persona_id}, Emoción: {nombre_predicho}, Tiempo_Inicio: {frame_time}, Tiempo_Fin: {frame_time + (1 / fps)}')

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    df_emociones = pd.DataFrame(df_emociones)
    df_emociones.to_csv("../data/resultados/emociones_clase1.csv", index=False)

# ruta_video = "../data/pruebas/clase6.mp4"
# duracion_analisis = 300 
# reconocimiento_emociones(ruta_video, duracion_analisis)


