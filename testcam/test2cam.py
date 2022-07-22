import cv2
  
cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)
  
while(True):
      
    ret1, frame_cam1 = cam1.read()
    ret2, frame_cam2 = cam2.read()
  
    # Display the resulting frame
    cv2.imshow('frame_cam1', frame_cam1)
    cv2.imshow('frame_cam2', frame_cam2)
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
cam1.release()
cam2.release()

# Destroy all the windows
cv2.destroyAllWindows()