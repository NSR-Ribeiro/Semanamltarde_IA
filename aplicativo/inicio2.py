import cv2

# Captura da câmera
cap = cv2.VideoCapture(0)

# Enquanto a câmera estiver aberta
while cap.isOpened():  # Corrigido de isOpend para isOpened
    # sucesso é booleana - 0 e 1
    sucesso, frame = cap.read()
    if not sucesso:
        print('Ignorando o frame vazio da câmera')
        continue
    
    cv2.imshow('Camera', frame)

    if cv2.waitKey(10) & 0xFF == ord('c'):
        break

# Fecha a captura
cap.release()  # Corrigido de releasse para release
cv2.destroyAllWindows()  # Corrigido de destroyAllWindows para cv2.destroyAllWindows
