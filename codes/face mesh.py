import cv2
import mediapipe as mp 
import time 

cap = cv2.VideoCapture(r"C:\Users\hp\Desktop\detection of the bels palsy\mediapipe\CAAI_dataset\bels plasy video datadset\bels plasy videos dataset\belsplasy\4.mp4")

pTime = 0 

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)

drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1 )


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img , cv2.COLOR_BGRA2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for facelms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img , facelms, mpFaceMesh.FACEMESH_CONTOURS,
                                  drawSpec, drawSpec)
            
    
    
    
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}' , (20 , 70) , cv2.FONT_HERSHEY_PLAIN, 3, (0 , 255 ,0),3)
    cv2.imshow("Image" , img)
    cv2.waitKey(1)
    
    
    