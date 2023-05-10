from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube


def saveFile():
    file = filedialog.askdirectory()
    saveDest.config(text=file)
    saveDest.place(x=10, y=260) 


def download():
    link = enterTxtBox.get("1.0",END)
    print(link)
    if link == "":
        messagebox.showerror("Error", "Please enter an URL!")
    if link != "":
            yt = YouTube(link)
            stream = yt.streams.get_by_itag(251)
            stream.download(saveDest.cget("text"))
            messagebox.showinfo("Success", "Audio downloaded successfully")

# initializing Window
window = Tk()
window.geometry("525x425")
window.title("YTSnap YouTube Video Downloader v0.1")
window.config(background="#D8D1D1")
window.iconbitmap("icon.ico")

# placing Mainimage
img = ImageTk.PhotoImage(Image.open("main_image.png"))
mainImage = Label(image=img)
mainImage.place(x=0, y=25)

# enter link label
enterLbl = Label(text="Please enter a YouTube link:", font=('Arial', 14))
enterLbl.place(x=10, y=150)

# enter link textbox 
enterTxtBox = Text(window, height=1, width=62)
enterTxtBox.place(x=10, y=182)
 
# save to directory label, txt, button
saveLbl = Label(text="Save to directory:", font=('Arial', 14))
saveLbl.place(x=10, y=220)

saveDest = Label(text="", font=('Arial', 11))
saveDest.place_forget()

saveBtn = Button(window, text="Choose directory", command=saveFile)
saveBtn.place(x=170, y=220)

# download button
downloadBtn = Button(window, text="DOWNLOAD!", width=15, height=3, bg='#EA4640', fg='white', command=download)
downloadBtn.place(x=201, y=310)

window.mainloop()