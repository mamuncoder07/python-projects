# Video Downloader 🎥⬇️

## 📌 Description

This project is a Python-based video downloader application that allows users to download videos from online platforms using a simple graphical interface.

The tool supports selecting video quality and saving the downloaded file to the local system.

## 🚀 Features

* Download videos from URLs
* Quality selection option
* Simple GUI interface
* Progress feedback
* Save videos to local storage
* Convert to executable (.exe)

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* yt-dlp
* OS module
* PyInstaller

## ▶️ Installation

Install required libraries:

```bash
pip install yt-dlp
pip install pyinstaller
```

Tkinter usually comes pre-installed with Python.

## ▶️ How to Run

Run the program:

```bash
python Video_Downloader.py
```

## 🖥️ Convert to EXE (Windows)

You can convert the Python file into a standalone executable (.exe) using PyInstaller.

Basic command:

```bash
pyinstaller --onefile --windowed Video_Downloader.py
```

Recommended command (with icon and dependencies):

```bash
pyinstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." --hidden-import=yt_dlp Video_Downloader.py
```

After building, the executable file will be available in the `dist` folder:

```
dist/Video_Downloader.exe
```

## 📷 Screenshot

(Add your application screenshot here)

## 📂 Project Structure

```
Video_Downloader/
│── Video_Downloader.py
│── icon.ico
│── README.md
│── Screenshot
```

## 🎯 Learning Objectives

* GUI development using Tkinter
* Working with external libraries
* Video downloading automation
* File handling in Python
* Creating executable applications

## 👨‍💻 Author

Mamun Reja
B.Tech AI & ML Student
