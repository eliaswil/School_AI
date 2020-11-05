import cv2
import numpy as np

import os

# get the video into a capture
video = cv2.VideoCapture('WideMayer480p_Compressed.mp4') # 0 ... webCam
# video = cv2.VideoCapture(0) # 0 ... webCam

# needed for frontal face detection
haar_file = 'haarcascade_frontalface_default.xml'




def play_video(video):
    if(video.isOpened() == False):
        print('Cant open file')
        pass

    else:
        while(video.isOpened()):
            returnValue, frame = video.read()

            if(returnValue == True):
                cv2.imshow('Frame', frame)

                if(cv2.waitKey(25) & 0xFF == ord('q')):
                    break
                pass
            else:
                break
        video.release()
        pass

    cv2.destroyAllWindows()
    pass

def get_and_save_frames_from_video(video, folder):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
        pass
    except OSError:
        print('problem with directory')
        pass

    current_frame_counter = 0

    while True:
        returnValue, frame = video.read()
        if(returnValue):
            frame_name = './' + folder + '/frame_' + str(current_frame_counter) + '.jpg'
            print(f'create the frame: {frame_name}')

            cv2.imwrite(frame_name, frame)
            current_frame_counter += 1
            pass
        else:
            break
        pass

    video.read()
    cv2.destroyAllWindows()

    pass

def face_detection(haar_file, video, save_faces=False):

    # folder for detected faces
    faces = 'faces'

    # sub folder in faces
    special_faces = 'persons'

    # join of foldernames to path
    face_path = os.path.join(faces, special_faces)

    if not os.path.isdir(face_path):
        os.makedirs(face_path)
        pass

    face_cascade = cv2.CascadeClassifier(haar_file)
    face_counter = 0

    size = (width, height) = (150, 120)

    while True:
        return_value, frame = video.read()

        if(not return_value):
            print('failed to capture frame')
            break

        converted_to_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detected_faces = face_cascade.detectMultiScale(converted_to_gray, 1.3, 5)

        for(x,y, face_width, face_height) in detected_faces:
            cv2.rectangle(converted_to_gray, (x,y), (x+face_width, y+face_height), (255,0,0), 3)
            
            if(save_faces):
                face = converted_to_gray[y:y+face_height, x:x+face_width]
                face_resize = cv2.resize(face, size)

                filename = f'{face_path}/face_{face_counter}.jpg'
                cv2.imwrite(filename, face_resize)
                face_counter += 1
                pass


            pass

        cv2.imshow('converted to gray', converted_to_gray)

        if(cv2.waitKey(25) & 0xFF == ord('q')):
            break

        pass

    video.release()
    cv2.destroyAllWindows()

    pass



# playVideo(video)
# get_and_save_frames_from_video(video, 'frames')
face_detection(haar_file, video)