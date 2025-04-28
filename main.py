import requests
from tkinter import *
from PIL import Image, ImageTk
from access_key import access_key
 
def getBird():
    base_url = "https://api.unsplash.com"
    api_url = f"{base_url}/photos/random?query=bird&client_id={access_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        bird_image_url = data['urls']['full']
        bird_image = requests.get(bird_image_url)
        if bird_image.status_code == 200:
            file_name = "pic.jpg"
            with open(file_name, "wb") as fileHandler:
                fileHandler.write(bird_image.content)
            img = Image.open(file_name)
            img = ImageTk.PhotoImage(img.resize((400, 400)))
            image_label.config(image=img)
            image_label.image = img
        status_code_label.config(text=bird_image.status_code)
    else:
        status_code_label.config(text=response.status_code)

def getDog():
    base_url = "https://dog.ceo"
    api_url = f"{base_url}/api/breeds/image/random"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        dog_image_url = data['message']
        dog_image = requests.get(dog_image_url)
        if dog_image.status_code == 200:
            file_name = "pic.jpg"
            with open(file_name, "wb") as fileHandler:
                fileHandler.write(dog_image.content)
            img = Image.open(file_name)
            img = ImageTk.PhotoImage(img.resize((400, 400)))
            image_label.config(image=img)
            image_label.image = img
        status_code_label.config(text=dog_image.status_code)
    else:
        status_code_label.config(text=response.status_code)

def getCat():
    base_url = "https://cataas.com"
    api_url = f"{base_url}/cat?json=true"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        cat_image_url = data['url']
        cat_image = requests.get(cat_image_url)
        if cat_image.status_code == 200:
            file_name = "pic.jpg"
            with open(file_name, "wb") as fileHandler:
                fileHandler.write(cat_image.content)
            img = Image.open(file_name)
            img = ImageTk.PhotoImage(img.resize((400, 400)))
            image_label.config(image=img)
            image_label.image = img
        status_code_label.config(text=cat_image.status_code)
    else:
        status_code_label.config(text=response.status_code)

root = Tk()
root.geometry("400x450")
root.title("Picture")
img = Image.open('pic.jpg')
img = ImageTk.PhotoImage(img.resize((400, 400)))
image_label = Label(image = img)
image_label.grid(row=0, column=0, columnspan=4)
status_code_label = Label()
status_code_label.grid(row=1, column=0)
Button(text="Bird", command=getBird).grid(row=1, column=1)
Button(text="Dog", command=getDog).grid(row=1, column=2)
Button(text="Cat", command=getCat).grid(row=1, column=3)
root.mainloop()