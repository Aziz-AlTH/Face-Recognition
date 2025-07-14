# Face-Recognition
# Face Recognition Project using OpenCV &amp; face_recognition  This project performs face recognition on a given test image using the `face_recognition` library and OpenCV. It compares detected faces with a set of known faces and labels them accordingly.

## 📷 Features

- Load and encode known faces from a local folder
- Detect and recognize faces in a test image
- Match unknown faces to known people
- Draw labeled boxes around recognized faces
- Display result with OpenCV window

## 🛠️ Technologies

- Python 3.9+
- [face_recognition](https://github.com/ageitgey/face_recognition)
- OpenCV (cv2)
- NumPy

  
2-Create a virtual environment (optional)

conda create -n face_env python=3.9

conda activate face_env

3-Install dependencies

pip install face_recognition opencv-python

conda install -c conda-forge dlib

4-Run the app

python face_recognition_app.py



🖼️ Input Requirements
All known faces must be clear, front-facing photos.

File names will be used as names for recognition (Neves.jpeg → "Neves").


✅ Output
A window will open showing the test image with recognized faces outlined and labeled.

If no match is found, the label "Unknown" will be shown.

📚 License
This project is for educational and academic purposes.

Made with ❤️ by Abdulaziz (Computer Science Student)

