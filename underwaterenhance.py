import numpy as np
import cv2

image=cv2.imread("C:\\Users\\Ananya\\1.jpg")

image = cv2.resize(image, (640, 480))
kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])

def white_balance(img):
    result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
    return result
balanced=white_balance(image)

lab = cv2.cvtColor(balanced, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl = clahe.apply(l)
limg = cv2.merge((cl, a, b))
enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)


def adjust_gamma(enhanced, gamma=1.5):
    invGamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** invGamma * 255
                     for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(enhanced, table)

image_gamma = adjust_gamma(enhanced, gamma=1.2)

b, g, r = cv2.split(image_gamma)
b = cv2.subtract(b, 10)
image_balanced = cv2.merge([b, g, r])

wb = cv2.xphoto.createSimpleWB()
final_image = wb.balanceWhite(image_balanced)


cv2.imshow("Original1",image)
cv2.imshow("Final",final_image)
cv2.imwrite('Finalimage1.jpg',final_image)


k=cv2.waitKey(0)
cv2.destroyAllWindows()