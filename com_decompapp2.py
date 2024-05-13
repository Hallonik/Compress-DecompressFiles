import tkinter as tk
from compressmodule import compress,decompress
from tkinter  import filedialog


def open_file():
    filename=filedialog.askopenfilename(initialdir='/',title="Select a file to compress")
    return filename

def op_file():
    filename=filedialog.askopenfilename(initialdir='/',title="Select a file to decompress")
    return filename


def compression(i,o):
    compress(i,o)

def decompression(ip,op):
    decompress(ip,op)

window=tk.Tk()
window.title("Compression engine")
window.geometry("600x400")



compress_button=tk.Button(window,text="COMPRESS",command=lambda:compression(open_file(),"CompressedFile"))



compress_button.grid(row=2,column=1)



decompress_button=tk.Button(window,text="DECOMPRESS",command=lambda:decompression(op_file(),"DecompressedFile"))



decompress_button.grid(row=6,column=1)

window.mainloop()