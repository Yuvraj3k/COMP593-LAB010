"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
import poke_api
import ctypes
import image_lib
import inspect

# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.exists(images_dir):
  os.makedirs(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.geometry('600x600')
root.minsize(500,500)
root.columnconfigure(0, weight=1)
root.rowconfigure(0 ,weight=1)

# TODO: Set the icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("COMP593.PokeImageViewer")
root.iconbitmap(os.path.join(script_dir, 'poke_ball.ico'))

# TODO: Create frames
frm = ttk.Frame(root)
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)
frm.grid(sticky= NSEW)


# TODO: Populate frames with widgets and define event handler functions
image_path = os.path.join(script_dir, 'poke_ball.png')
photo = PhotoImage(file=image_path)

label = ttk.Label(frm, image=photo)
label.grid(row=0, column=0, padx=10, pady=10)

pokemon_list = poke_api.get_pokemon_name()

if not pokemon_list:
  pokemon_list = []
  
poke_cbox = ttk.Combobox(frm, values=pokemon_list, state="readonly")
poke_cbox.set("Select a Pokemon")
poke_cbox.grid(row=1, column=0, pady=10)

def select_pokemon(event):
    image_path = poke_api.download_pokemon_artwork(poke_cbox.get(), images_dir)

    if image_path:
        photo["file"] = image_path
        label["image"] = photo
        btn_set_wallpaper['state'] = 'normal'
        
    else:
        label["image"] = None
        label["text"] = "Error: No artwork found for " + poke_cbox.get  
        btn_set_wallpaper['state'] = 'disabled'

def set_wallpaper():
    image_path = poke_api.download_pokemon_artwork(poke_cbox.get(), images_dir)
    
    if image_path:
        success = image_lib.set_desktop_background_image(image_path)
        
        if success:
            print("Desktop background set successfully.")
        else:
            print("Failed to set desktop background.")
            
    else:
        print("Error: No artwork found for", poke_cbox.get())



btn_set_wallpaper = Button(frm, text="Set Desktop Image", command=set_wallpaper, state="disabled")
btn_set_wallpaper.grid(row=2, column=0, pady=10)
poke_cbox.bind("<<ComboboxSelected>>", select_pokemon)

root.mainloop()