import cv2
from facerec import Facerec

# Encode faces from a folder
fdf = Facerec()
fdf.load_encoding_images("storedImages/")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = fdf.findingKnownFaces(frame)
    for face_loc, name in zip(face_locations, face_names):
        top, left, bottom, right = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        
        if name == "Unknown":
            cv2.putText(frame, name,(right, top - 10), cv2.FONT_ITALIC, 1, (0, 0, 200), 2)
        else:
            cv2.putText(frame, name,(right, top - 10), cv2.FONT_ITALIC, 1, (96, 255, 64), 2)
            
        if name == "Unknown":
            # the red border
            cv2.rectangle(frame, (right, top), (left, bottom), (0, 0, 200), 4)
        else:
            # the green border
            cv2.rectangle(frame, (right, top), (left, bottom), (96, 255, 64), 4)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()