import requests
from tkinter import *
from PIL import Image, ImageTk
from access_key import access_key
 
def getPicture():
    base_url = "https://api.unsplash.com"
    api_url = f"{base_url}/photos/random?query=bird&client_id={access_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        pic_image_url = data['urls']['regular']
        pic_image = requests.get(pic_image_url)
        file_name = f"pic.{pic_image_url.split(".")[-1]}"
        if pic_image.status_code == 200:
            with open(file_name, "wb") as fileHandler:
                fileHandler.write(pic_image.content)
            img = Image.open(file_name)
            img = ImageTk.PhotoImage(img.resize((400, 400)))
            image_label.config(image=img)
            image_label.image = img
        status_code_label.config(text=pic_image.status_code)
    else:
        status_code_label.config(text=response.status_code)
    
root = Tk()
root.geometry("400x450")
root.title("Picture")
image_label = Label(width = 400, height = 400)
image_label.grid(row=0, column=0, columnspan=3)
status_code_label = Label()
status_code_label.grid(row=1, column=0)
Button(text="next", command=getPicture).grid(row=1, column=2)
getPicture()
root.mainloop()