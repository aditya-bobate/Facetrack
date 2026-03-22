import cv2
import os

name = input("Enter Student Name: ")
roll = input("Enter Roll No: ")

label_name = f"{name}_{roll}"
folder = f"dataset/{label_name}"
os.makedirs(folder, exist_ok=True)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0
MAX_IMAGES = 20

print("Press 's' to save face | ESC to exit")

while True:
    ret, frame = cam.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if count < MAX_IMAGES:
            cv2.putText(frame, f"{count}/{MAX_IMAGES}",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

    cv2.imshow("Face Registration", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s') and len(faces) == 1:
        count += 1
        cv2.imwrite(f"{folder}/{count}.jpg", face_img)
        print(f"Saved image {count}")

    if key == 27 or count >= MAX_IMAGES:
        break

cam.release()
cv2.destroyAllWindows()
print("✅ Dataset collection complete")
