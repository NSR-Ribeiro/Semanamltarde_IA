import cv2 #pip install opencv-python
#importando mediapipe
import mediapipe as mp # pip install mediapipe

# desenhar os pontos
mp_drawing = mp.solutions.mp_drawing_utils

# coletar solução do Face Mesh
mp_face_mesh = mp.solutions.face_mesh

# enquanto a camêra estiver aberta
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5,min_tracking_confidence) as apelido

# capiturar a camêra
cap = cv2.VideoCapture(0)
# enquanto a câmera  estiver aberta
while cap.isOpend():
    # sucesso é booleana-0 e 1
    sucesso,frame = cap.read()
    if not sucesso:
        print('ignorando o frame vazio da câmera')
        continue
    cv2.imshow('Camera',frame)

    if cv2.waitKey(10) & 0xFF == ord('c'):
        break

# fecha a captura
cap.releasse()
cap.destroyAllWindows()