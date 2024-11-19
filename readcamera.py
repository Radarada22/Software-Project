import cv2

kamera = cv2.VideoCapture('rtsp://admin:12345678@10.55.1.99:1935/')

while True:
    _, frame = kamera.read()
    cv2.imshow("Kamera handphone", frame)
    cv2.waitKey(1)