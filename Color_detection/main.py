import cv2
import numpy as np

cap=cv2.VideoCapture(0)
_,frame=cap.read()
# frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
writer = cv2.VideoWriter("result.mp4", cv2.VideoWriter_fourcc(*'xivd'),
                          30, (frame.shape[0], frame.shape[1]))

while 1==1:
    _,frame=cap.read()
    r=[]
    g=[]
    b=[]
    # frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    r, g, b=frame.shape
    cv2.rectangle(frame,(230,300),(380,200),0,3)
    pic=frame[240:260 , 300:340]

    blurred = cv2.GaussianBlur(frame, (25,25), 0)
    frame[0:200, 0:640] = blurred[0:200, 0:640]
    frame[300:480, 0:640] = blurred[300:480, 0:640]
    frame[200:300, 0:228] = blurred[200:300, 0:228]
    frame[200:300, 380:640] = blurred[200:300, 380:640]
    r=frame[:,:,2]
    g=frame[:,1,:]
    b=frame[0,:,:]

    r_mean=np.mean(r)
    g_mean=np.mean(g)
    b_mean=np.mean(b)

    # print(r_mean)
    # print(g_mean)
    # print(b_mean)
    
    if r_mean>g_mean and r_mean>b_mean:
        color="Red"

    if g_mean>r_mean and g_mean>b_mean:
        color="Green"

    elif r_mean>=g_mean and r_mean>b_mean and g_mean>b_mean and g_mean>=200 and b_mean<160:
        color="Yellow"

    elif b_mean>g_mean and b_mean>r_mean and g_mean>r_mean:
        color="Blue"

    elif r_mean>g_mean and r_mean>b_mean and g_mean>b_mean:
        color="Orange"

    elif b_mean>g_mean and r_mean>g_mean and  b_mean>r_mean:
        color="Purple"
    
    elif b_mean==g_mean==r_mean==255:
        color="White"

    elif b_mean==g_mean==r_mean==0:
        color="Black"
    else:
        color="Nothing"

    cv2.putText(frame,color,(270,180),cv2.FONT_HERSHEY_SIMPLEX,1,0,2)

    # frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow("result",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

writer.release()
