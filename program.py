# import face_recognition
# import cv2
# import numpy as np
# import csv
# import os
# from datetime import datetime
# video_capture=cv2.VideoCapture(0)
# gandhi_image=face_recognition.load_image_file("712Pnx73P8L._AC_UF1000,1000_QL80_.jpg")
# gandhi_encoding=face_recognition.face_encodings(gandhi_image)[0]
#
# modi_image=face_recognition.load_image_file("download.jpeg")
# modi_encoding=face_recognition.face_encondings(modi_image)[0]
# known_face_encoding=[gandhi_encoding,modi_encoding]
# known_faces_names=["Mahatama Gandhi","Narendra Modi"]
#
# celebrity=known_faces_names.copy()
#
# face_locations=[]
# face_enconding=[]
# face_names=[]
# s=True
#
# now=datetime.now()
# current_date=now.strftime("%y-%m-%d")
#
# f=open(current_date+'.csv','w+',newline=' ')
# lnwriter=csv.writer(f)
#
# while True:
#     _,frame =video_capture.read()
#     small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
#     rgb_small_frame=small_frame[:,:,::,-1]
#     if s:
#         face_locations=face_recognition.face_locations(rgb_small_frame)
#         face_encondings=face_recognition.face_encondingd(rgb_small_frame,face_locations)
#         face_names=[]
#         for face_enconding in face_encondings:
#             matches=face_recognition.compare_faces(known_face_encoding,face_enconding)
#             name=""
#             face_distance=face_recognition.face_distance(known_face_encoding,face_enconding)
#             best_match_index=np.argmin(face_distance)
#             if matches[best_match_index]:
#                 name=known_faces_names[best_match_index]
#
#             face_names.append(name)
#             if name in known_faces_names:
#                 if name in celebrity:
#                     celebrity.remove(name)
#                     print(celebrity)
#                     current_time=now.strftime("%H-%M-%s")
#                     lnwriter.writerow([name,current_time])
#     cv2.imshow("Attendance System",frame)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break
#
# video_capture.release()
# cv2.destroyAllWindows()
# f.close()


import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)
gandhi_image = face_recognition.load_image_file("gandhi.jpeg")
gandhi_encoding = face_recognition.face_encodings(gandhi_image)[0]

modi_image = face_recognition.load_image_file("download.jpeg")
modi_encoding = face_recognition.face_encodings(modi_image)[0]

known_face_encoding = [gandhi_encoding, modi_encoding]
known_faces_names = ["Mahatma Gandhi", "Narendra Modi"]

celebrity = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%y-%m-%d")

f = open(current_date + '.csv', 'w+', newline=' ')
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                if name in celebrity:
                    celebrity.remove(name)
                    print(celebrity)
                    current_time = now.strftime("%H-%M-%s")
                    lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
