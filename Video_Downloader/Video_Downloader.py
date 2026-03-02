import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import yt_dlp
import os
import sys
import threading


# PyInstaller resource path
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_var.set(folder)


# ===== Progress Hook =====
def progress_hook(d):
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '0%').strip()
        percent = percent_str.replace('%', '')

        speed = d.get('_speed_str', '0 KB/s')

        try:
            progress_var.set(float(percent))
        except:
            pass

        status_label.config(text=f"{percent_str}  |  Speed: {speed}")
        root.update_idletasks()

    elif d['status'] == 'finished':
        progress_var.set(100)
        status_label.config(text="Processing...")


# ===== Download Worker Thread =====
def download_worker(url, path):

    try:
        ydl_opts = {
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'format': 'best',
            'noplaylist': True,
            'progress_hooks': [progress_hook]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Download Completed!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def download_video():
    url = url_var.get()
    path = path_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter video URL")
        return

    if not path:
        messagebox.showerror("Error", "Please select download folder")
        return

    progress_var.set(0)
    status_label.config(text="Starting...")

    # Start thread
    threading.Thread(target=download_worker, args=(url, path), daemon=True).start()


# ===== GUI =====
root = tk.Tk()
root.title("Universal Video Downloader @MAMUN")
root.geometry("500x330")
root.configure(bg="#ff0000")

try:
    root.iconbitmap(resource_path("icon.ico"))
except:
    pass


# URL
tk.Label(root, text="Video URL:", font=("Arial", 12),
         bg="#ff0000", fg="white").pack(pady=5)

url_var = tk.StringVar()
tk.Entry(root, textvariable=url_var, width=60).pack()


# Path
tk.Label(root, text="Download Folder:", font=("Arial", 12),
         bg="#ff0000", fg="white").pack(pady=5)

path_var = tk.StringVar()

frame = tk.Frame(root, bg="#ff0000")
frame.pack()

tk.Entry(frame, textvariable=path_var, width=40).pack(side=tk.LEFT, padx=5)

tk.Button(frame, text="Browse",
          bg="#0022ff", fg="white",
          command=browse_folder).pack(side=tk.LEFT)


# Progress Bar
progress_var = tk.DoubleVar()

progress = Progressbar(root,
                       variable=progress_var,
                       maximum=100,
                       length=400)

progress.pack(pady=15)

status_label = tk.Label(root,
                        text="Waiting...",
                        bg="#ff0909",
                        fg="white")

status_label.pack()


# Download Button
tk.Button(root,
          text="Download Video",
          font=("Arial", 12),
          bg="green",
          fg="white",
          command=download_video).pack(pady=20)


root.mainloop()
