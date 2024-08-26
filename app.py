import face_recognition
import cv2
import numpy as np
from time import sleep

RED = "\033[1;31m"
CYAN = "\033[1;96m"
GREEN = "\033[1;92m"

# Captura de vídeo
videoCapture = cv2.VideoCapture(0)

# Carregar uma imagem de exemplo e aprender a reconhecê-la
userImage = face_recognition.load_image_file("rosto.jpg")
UserFaceEncoding = face_recognition.face_encodings(userImage)

if len(UserFaceEncoding) > 0:
    UserFaceEncoding = UserFaceEncoding[0]
else:
    print("Erro: Não foi possível encontrar a face em 'rosto.jpg'.")
    exit()

knowFaceEncodings = [UserFaceEncoding]
knownFaceNames = ["Daniel"]

faceLocations = []
faceEncodings = []
faceNames = []
processThisFrame = True

while True:
    ret, frame = videoCapture.read()

    if not ret:
        print("Erro ao capturar o frame da câmera.")
        break

    # Reduz o tamanho do frame para acelerar o processamento
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if processThisFrame:
        # Localiza os rostos no frame atual
        faceLocations = face_recognition.face_locations(rgb_small_frame)

        # Codifica as faces encontradas
        faceEncodings = face_recognition.face_encodings(rgb_small_frame, faceLocations)

        faceNames = []
        for face_encoding in faceEncodings:
            matches = face_recognition.compare_faces(knowFaceEncodings, face_encoding)
            name = "Unknown"

            # Verifica a menor distância para encontrar o melhor match
            face_distances = face_recognition.face_distance(knowFaceEncodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = knownFaceNames[best_match_index]

            faceNames.append(name)

    processThisFrame = not processThisFrame

    if 'Rafael Felipe' in faceNames:
        print(GREEN + "Acesso Autorizado." + CYAN + "Bem-vindo de volta Rafael!")
        break
    else:
        print(RED + 'Acesso negado.')
        sleep(3)

# Libera a câmera e fecha as janelas
videoCapture.release()
cv2.destroyAllWindows()
