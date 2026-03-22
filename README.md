# 📸 FaceTrack

FaceTrack is a Python-based **Face Tracking + Face Recognition** project that can detect and recognize faces in real-time using a webcam.  
It allows you to **register new faces**, **train the model**, and then **identify people live**.

---

## 🚀 Features

✅ Real-time face detection using webcam  
✅ Register new faces (create your own dataset)  
✅ Train a face recognition model  
✅ Recognize known faces + show **Unknown** for others  
✅ Simple and beginner-friendly project structure  

---

## 🛠️ Tech Stack

- Python  
- OpenCV  
- Face Recognition / ML Model Training  
- Numpy  

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/aditya-bobate/Facetrack.git
cd Facetrack
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

### ▶️ How to Run

🧍 Step 1: Register Face
```bash
python register.py
```

🏋️ Step 2: Train Model
```bash
python train_model.py
```

👁️ Step 3: Start Face Recognition
```bash
python recognize.py
```

---

### 📁 Project Structure
```
Facetrack/
│── register.py          # Register new face data
│── train_model.py       # Train the face recognition model
│── recognize.py         # Recognize faces in real-time
│── models/              # Saved trained model files
│── dataset/             # Stored face images (created after registering)
│── requirements.txt     # Dependencies
│── README.md
```


