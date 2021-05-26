import requests
import numpy as np
import cv2
ip=input("Your IP >> ")
while True:
	link=f"http://{ip}:8080/photo.jpg"
	img=requests.get(link)
	vid=np.array(bytearray(img.content),dtype=np.uint8)
	a=cv2.imdecode(vid,-1)
	cv2.imshow("frame",a)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
