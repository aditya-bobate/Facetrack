# ⬡ FaceTrack

FaceTrack is a Python-based **Face Recognition Attendance System** with a full GUI built using Tkinter. It supports real-time face detection, automated attendance marking, role-based access control, and Excel export.

---

## 🚀 Features

- ✅ Real-time face detection & recognition using webcam
- ✅ Automated attendance marking (On Time / Late)
- ✅ Beautiful dark-themed GUI (Tkinter)
- ✅ Role-based login — Student, Admin (Teacher), Head Admin (HOD)
- ✅ HOD can approve/reject new admin requests
- ✅ HOD can delete student accounts
- ✅ Export attendance records to Excel
- ✅ SQLite database for storing users & attendance
- ✅ Subject-wise attendance sessions

---

## 🛠️ Tech Stack

- Python
- OpenCV (LBPH Face Recognizer)
- Tkinter (GUI)
- SQLite3 (Database)
- OpenPyXL (Excel Export)

---

## 📦 Installation

**1️⃣ Clone the repository**
```bash
git clone https://github.com/aditya-bobate/Facetrack.git
cd Facetrack
```

**2️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

**3️⃣ Make sure `haarcascade_frontalface_default.xml` is in the project root**
> Download from OpenCV's GitHub if missing.

---

## ▶️ How to Run
```bash
python main.py
```

---

## 👥 Account Types

| Role | Access |
|------|--------|
| **Student** | Face capture on registration, attendance marked automatically |
| **Admin (Teacher)** | Start attendance sessions, add subjects, export to Excel |
| **Head Admin (HOD)** | Approve/reject admin requests, delete students, view stats |

> Default HOD login — Username: `headadmin` Password: `admin123`

---

## 📁 Project Structure
```
Facetrack/
│── main.py              # Main application (GUI + all screens)
│── register.py          # Face registration helper
│── train_model.py       # Train the LBPH face recognition model
│── recognize.py         # Standalone face recognition
│── templates/           # UI templates (if any)
│── haarcascade_frontalface_default.xml
│── requirements.txt
│── README.md
```

> `dataset/`, `models/`, `facetrack.db` and `attendance.xlsx` are excluded from the repo via `.gitignore`.

---

## 📊 How Attendance Works

1. Admin selects a subject and starts a session
2. Webcam opens and detects faces in real time
3. Recognized students are marked **On Time** or **Late** based on a 15-minute window
4. Records are saved to the SQLite database
5. Admin can export all records to `attendance.xlsx`
