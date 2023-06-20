def home_page():
    about_us_window.destroy()
    import os
    os.system("python klg.py")

from tkinter import *
import sys
about_us_window = Tk()
about_us_window.title("ABOUT US")
about_us_window.wm_attributes("-fullscreen", "true")
about_us_window.config(bg="aquamarine")
about_us_window.iconbitmap("lpu_logo.ico")


about_us_window1 = Frame(about_us_window, bg="aquamarine")
about_us_window1.pack(side=LEFT,pady=0)

about_us_window2 = Frame(about_us_window, bg="aquamarine")
about_us_window2.pack(side=LEFT, pady=50)

about_us_window3 = Frame(about_us_window, bg="aquamarine")
about_us_window3.pack(side=LEFT, pady=50)

image1 = PhotoImage(file="anshraj.gif")
image2 = PhotoImage(file="asimIqbal.gif")
image3 = PhotoImage(file="VishnuKoundinya.gif")

Label(about_us_window1, image=image1).pack(padx=50, pady=20)
Label(about_us_window1, image=image2).pack(padx=50, pady=20)
Label(about_us_window1, image=image3).pack(padx=50, pady=20)


Label(about_us_window2, text="Name: Ansh Raj", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Reg. No. 12114120", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Roll No. A07", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)

Label(about_us_window2, bg="aquamarine").pack(anchor=NW, pady=30)

Label(about_us_window2, text="Name: Asim Iqbal", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Reg. No. 12114037", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Roll No. A08", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)

Label(about_us_window2, bg="aquamarine").pack(anchor=NW, pady=30)

Label(about_us_window2, text="Name: GM Sri Vishnu Koundinya", font="halston 15 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Reg. No. 12114356", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Roll No. A09", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)

python = PhotoImage(file="python.gif")
start = PhotoImage(file="start.gif")

Label(about_us_window3, text="Current Version", font="halston 20 italic", bg="aquamarine", fg="blue").pack(anchor=NW, padx=100, pady=20)
Label(about_us_window3, text=sys.version, bg="aquamarine").pack(anchor=NW, padx=100)
Label(about_us_window3, image=python).pack(anchor=NW, padx=100, pady=20)
Label(about_us_window3, text="Click on the START button to continue...", font="halston 25 italic", bg="aquamarine", fg="maroon").pack(anchor=NW)
Button(about_us_window3, image=start, command=home_page).pack(anchor=NW, padx=200, pady=30)

about_us_window.mainloop()