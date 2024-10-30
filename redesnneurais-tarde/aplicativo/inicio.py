import cv2


# capiturar a camêra
cap = cv2.VideoCapture(0)
# enquanto a câmera  estiver aberta
while cap.isOpend():
    # sucesso é booleana-0 e 1
    sucesso,frame = cap.read()
    if not sucesso:
        print('ignorando o frame vazio da canera')
        continue
    cv2.imshow('Camera',frame)

    if cv2.waitKey(10) & 0xFF == ord('c'):
        break

# fecha a captura
cap.releasse()
cap.destroyAllWindows()