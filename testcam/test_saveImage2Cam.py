import cv2 as cv
from picamera.array import PiRGBArray
from picamera import PiCamera
import io
import numpy as np
import time
from datetime import datetime

# initialize the camera and grab a reference to the raw camera capture
# see detail for pi camera setup https://picamera.readthedocs.io/en/release-1.13/fov.html
PICAM_WIDTH = 1920
PICAM_HEIGHT = 1080
camera = PiCamera()
#camera.exposure_speed = 198
#camera.shutter_speed = 4000
camera.resolution = (PICAM_WIDTH, PICAM_HEIGHT)
camera.framerate = 32
camera.iso = 100
rawCapture = PiRGBArray(camera, size=(PICAM_WIDTH, PICAM_HEIGHT))

time.sleep(0.2) # allow the camera to warmup


cam2 = cv.VideoCapture(1)
cam2.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cam2.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
cam2.set(cv.CAP_PROP_BUFFERSIZE, 1)
cv.namedWindow("frame_cam1", cv.WINDOW_AUTOSIZE);
cv.namedWindow("frame_cam2", cv.WINDOW_AUTOSIZE);


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame_cam1 = frame.array
    ret2, frame_cam2 = cam2.read()
    
    #frame_cam1=cv.resize(frame_cam1,[frame_cam1.shape[1]//2,frame_cam1.shape[0]//2])
    frame_cam2=cv.resize(frame_cam2,[frame_cam2.shape[1]//2,frame_cam2.shape[0]//2])

    # Display the resulting frame
    cv.imshow('frame_cam1', frame_cam1)
    cv.imshow('frame_cam2', frame_cam2)

    key = cv.waitKey(5)

    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('c'):
        now = datetime.now()
        time_string = now.strftime("%Y-%m-%d_%H-%M-%S")
        save_path = '/home/pi/Desktop/ProjectMarigold/testcam/saveImages/'
        save_ret1 = cv.imwrite(save_path+'cam1_'+time_string+'.png',frame_cam1)
        save_ret2 = cv.imwrite(save_path+'cam2_'+time_string+'.png',frame_cam2)
        if save_ret1 :
            print('saved at '+save_path+'cam1_'+time_string+'.png')
        if save_ret2 :
            print('saved at '+save_path+'cam2_'+time_string+'.png')
    rawCapture.truncate(0)
cam2.release()

# Destroy all the windows
cv.destroyAllWindows()