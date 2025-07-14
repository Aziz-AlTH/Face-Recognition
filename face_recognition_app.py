import face_recognition
import cv2
import os
import numpy as np

# تحميل الصور المعروفة وتشفيرها
known_faces_dir = './known_faces'
known_encodings = []
known_names = []

for filename in os.listdir(known_faces_dir):
    path = os.path.join(known_faces_dir, filename)
    image = face_recognition.load_image_file(path)
    encoding = face_recognition.face_encodings(image)

    if encoding:
        known_encodings.append(encoding[0])
        name = os.path.splitext(filename)[0]
        known_names.append(name)

# تحميل صورة الاختبار
test_image_path = './test_images/Test_Face.jpeg'
test_image = face_recognition.load_image_file(test_image_path)
test_locations = face_recognition.face_locations(test_image)
test_encodings = face_recognition.face_encodings(test_image, test_locations)

# تحويل الصورة لاستخدام OpenCV في العرض
image_bgr = cv2.cvtColor(test_image, cv2.COLOR_RGB2BGR)

for face_encoding, face_location in zip(test_encodings, test_locations):
    results = face_recognition.compare_faces(known_encodings, face_encoding)
    distances = face_recognition.face_distance(known_encodings, face_encoding)

    name = "Unknown"
    if any(results):
        best_match_index = np.argmin(distances)
        name = known_names[best_match_index]

    # رسم المستطيل واسم الشخص
    top, right, bottom, left = face_location
    cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(image_bgr, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# عرض الصورة النهائية
cv2.imshow("Face Recognition", image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
