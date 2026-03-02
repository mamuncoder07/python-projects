# 🎥⬇️ Video Downloader

<p align="center">
  <b>A Powerful Python GUI Video Downloader with Quality Selection & EXE Support</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![yt-dlp](https://img.shields.io/badge/Downloader-yt--dlp-red?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-Free-brightgreen?style=for-the-badge)

</p>

---

## 📌 Description

This project is a **Python-based Video Downloader Application** that allows users to download videos from online platforms using a simple and user-friendly graphical interface.

The application supports:

✔ Quality selection
✔ Progress tracking
✔ Local storage saving
✔ Executable (.exe) conversion

---

## 🚀 Features

✨ Download videos from URLs
🎯 Select video quality (Best / 1080p / 720p / etc.)
📊 Progress feedback with status
🖥️ Simple and clean GUI
💾 Save videos to local system
⚡ Convert to EXE for easy distribution

---

## 🛠️ Technologies Used

| Technology     | Purpose               |
| -------------- | --------------------- |
| 🐍 Python      | Core Programming      |
| 🖼️ Tkinter    | GUI Interface         |
| ⬇️ yt-dlp      | Video Download Engine |
| 📁 OS Module   | File Handling         |
| ⚙️ PyInstaller | EXE Conversion        |

---

## ▶️ Installation

Install required libraries:

```bash
pip install yt-dlp
pip install pyinstaller
```

Tkinter usually comes pre-installed with Python.

---

## ▶️ How to Run

Run the program:

```bash
python Video_Downloader.py
```

---

## 🖥️ Convert to EXE (Windows)

You can convert the Python script into a standalone executable file.

### 🔹 Basic Command

```bash
pyinstaller --onefile --windowed Video_Downloader.py
```

### 🔹 Recommended Command (With Icon & Dependencies)

```bash
pyinstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." --hidden-import=yt_dlp Video_Downloader.py
```

After building, the executable will be available inside:

```
dist/Video_Downloader.exe
```

---

## 📷 Screenshot

> Add your application screenshot here

---

## 📂 Project Structure

```
Video_Downloader/
│── Video_Downloader.py
│── icon.ico
│── README.md
│── Screenshot
```

---

## 🎯 Learning Objectives

✔ GUI development using Tkinter
✔ Working with external libraries
✔ Video downloading automation
✔ File handling in Python
✔ Creating executable software

---

## 👨‍💻 Author

**Mamun Reja**
🎓 B.Tech AI & ML Student

---

## ⭐ Support

If you like this project, please ⭐ star the repository and share it!

---
