import cv2
import numpy as np

image = cv2.imread("En_Dn_image\input\otZD6cyQ8teFb3aqwXRB5d.jpg")
B,G,R=cv2.split(image)

cipher_key = np.random.randint(0, 256, (image.shape[0], image.shape[1]), dtype=np.uint8) 
# print(cipher_key)
cv2.imwrite("En_Dn_image\output\key.jpg", cipher_key)   

encrypted_B = cv2.bitwise_xor(B, cipher_key)  
encrypted_G = cv2.bitwise_xor(G, cipher_key)  
encrypted_R = cv2.bitwise_xor(R, cipher_key)  
encrypted_image=cv2.merge((encrypted_B,encrypted_G,encrypted_R))
cv2.imwrite("En_Dn_image\output\encrypted_image.jpg",encrypted_image)


decrypted_B = cv2.bitwise_xor(encrypted_B, cipher_key) 
decrypted_G = cv2.bitwise_xor(encrypted_G, cipher_key) 
decrypted_R = cv2.bitwise_xor(encrypted_R, cipher_key) 
decrypted_image=cv2.merge((decrypted_B,decrypted_G,decrypted_R))
cv2.imwrite("En_Dn_image/output/decrypted_image.jpg",decrypted_image)
# cv2.imshow("decrypted_image",decrypted_image)

cv2.waitKey()