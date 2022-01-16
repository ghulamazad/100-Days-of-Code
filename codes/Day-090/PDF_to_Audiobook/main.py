from tkinter import *
from tkinter import filedialog
from pdfToAudio import PDFToAudio
import _thread as thread


def convert_to_audio():
    file_path = source_lbl.cget("text")
    dest = destination_folder_lbl.cget("text")
    pdf2Audio = PDFToAudio()
    pdf2Audio.pdf_to_audio(
        pdf_file=file_path, lang=PDFToAudio.ENGLISH, dest=dest)
    process_lbl.config(
        text="Completed")


def show_process():
    thread.start_new_thread(convert_to_audio, ())
    process_lbl.config(
        text="Processing...")


def upload_pdf():
    pdf_file_path = filedialog.askopenfilename(
        initialdir="/", title="Select PDF File", filetypes=[("PDF Files", ".pdf"), ])
    source_lbl.config(text=pdf_file_path, fg='red')


def destination_folder():
    destination_path = filedialog.askdirectory(initialdir="/")
    destination_folder_lbl.config(
        text=destination_path, fg='red')


window = Tk()
window.title("PDF To AudioBook")
window.minsize(width=200, height=200)
window.config(padx=26, pady=26)
window.geometry("600x250")

title_lbl = Label(window, text="PDF To AudioBook",
                  font=("Time New Roman", 16, 'bold'), fg='red')
title_lbl.grid(row=0, column=1, columnspan=3, pady=(12, 12))

a_lbl = Label(window, text="Select PDF File: ")
a_lbl.grid(row=1, column=0, sticky="E")
upload_pdf_btn = Button(window, text="Browse", padx=16, command=upload_pdf)
upload_pdf_btn.grid(row=1, column=1, sticky="W")

source_lbl = Label(window, text="")
source_lbl.grid(row=1, column=2, sticky="W")

b_lbl = Label(window, text="Select Destination Folder: ")
b_lbl.grid(row=2, column=0, pady=(12, 12), sticky="E")
destination_folder_btn = Button(
    window, text="Browse", padx=16, command=destination_folder)
destination_folder_btn.grid(row=2, column=1, sticky="W")

destination_folder_lbl = Label(window, text="")
destination_folder_lbl.grid(row=2, column=2, sticky="W")

convert_btn = Button(
    window, text="Convert", padx=16, command=show_process)
convert_btn.grid(row=3, column=2)

process_lbl = Label(window, text="", fg='red')
process_lbl.grid(row=4, column=1, columnspan=3, pady=(12, 12))

window.mainloop()
