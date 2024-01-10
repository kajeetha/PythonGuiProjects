import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import*

def change_color():
    color = colorchooser.askcolor(title = "pick a color")
    text_area.config(fg = color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), sizebox.get()))

def new_file():
    window.title("untitled")
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=" .txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])

    #this is so the window will change to the title of whatever file
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())

    except Exception:
        print("could not read file")

    finally:
        file.close()
def save_file():
    file = filedialog.asksaveasfilename(initialfile='untitled.txt', defaultextension= ".txt", filetypes=[("All Files", "*.*"), ("Text Documents", ".txt")])

    if file is None:
        return

    else:

        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("could not save file")

        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About this program", "This is a program written using python")

def quit():
    window.destroy()

window= Tk()
window.title("Text Editor Program")
file = None
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

fontname = StringVar(window)
fontsize = StringVar(window)
fontsize.set("25")
fontname.set("Arial")



text_area = Text(window, font = (fontname.get(), fontsize.get()))
scrollbar = Scrollbar(text_area)
window.grid_rowconfigure(0 , weight = 1) #weight so it doesn't back expand
window.grid_columnconfigure(0 , weight = 1)
text_area.grid(sticky = N + E + S+ W) #so the text area should take most of the window.

scrollbar.pack(side = RIGHT, fill = Y)
text_area.config(yscrollcommand=scrollbar.set)


frame = Frame(window)
frame.grid()
sizebox = Spinbox(frame, from_=1, to=100, textvariable=fontsize, command = change_font)
sizebox.grid(row=0, column=2)
color_button = Button(frame, text = "color", command = change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, fontname, *font.families(), command = change_font) #returns all of the different fonts available to option menu
font_box.grid(row=0, column =1)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu=file_menu) #this make sit a dropdown
file_menu.add_command(label = "new", command = new_file)
file_menu.add_command(label = "save", command = save_file)
file_menu.add_command(label = "open", command = open_file)
file_menu.add_separator()
file_menu.add_command(label = "exit", command = quit)

edit_menu = Menu(menu_bar, tearoff= 0)
menu_bar.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "cut", command = cut)
edit_menu.add_command(label = "copy", command = copy)
edit_menu.add_command(label = "paste", command = paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "About", command = about)

window.mainloop()