import numpy as np
import cv2

img = cv2.imread('chaine.png', cv2.IMREAD_COLOR)


cv2.line(img, (0,0), (150,150), (255,255,255), 15)
cv2.rectangle(img, (15,15), (200,1520), (0,255,0), 5)
cv2.circle(img, (100,63), 55, (0,0,255), -1)

pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 5)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'CodeFacil AI!~', (0,50), font, 1, (255,0,0), 1, cv2.LINE_AA)



cv2.imshow('image1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()