import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import os
import sys


#  Function for PyInstaller icon path
def resource_path(relative_path):
    """ Get absolute path to resource (works for exe) """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_var.set(folder)


def download_video():
    url = url_var.get()
    path = path_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter video URL")
        return

    if not path:
        messagebox.showerror("Error", "Please select download folder")
        return

    try:
        ydl_opts = {
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'format': 'best',
            'noplaylist': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Download Completed!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


#  GUI Window
root = tk.Tk()
root.title("Universal Video Downloader @MAMUN")
root.geometry("500x250")
root.resizable(True, True)
root.configure(bg="#ff0000")

#  Icon load safely
try:
    root.iconbitmap(resource_path("icon.ico"))
except:
    pass


# URL Section
tk.Label(root, text="Video URL:", font=("Arial", 12),
         bg="#ff0000", fg="white").pack(pady=5)

url_var = tk.StringVar()
tk.Entry(root, textvariable=url_var, width=60).pack()


# Path Section
tk.Label(root, text="Download Folder:", font=("Arial", 12),
         bg="#ff0000", fg="white").pack(pady=5)

path_var = tk.StringVar()

frame = tk.Frame(root, bg="#ff0000")
frame.pack()

tk.Entry(frame, textvariable=path_var, width=40).pack(side=tk.LEFT, padx=5)

tk.Button(frame,
          text="Browse",
          bg="#0022ff",
          fg="white",
          command=browse_folder).pack(side=tk.LEFT)


# Download Button
tk.Button(root,
          text="Download Video",
          font=("Arial", 12),
          bg="green",
          fg="white",
          command=download_video).pack(pady=20)


root.mainloop()