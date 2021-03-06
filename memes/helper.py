import ipywidgets as widgets
import IPython.display as display
import requests
import os
from shutil import rmtree


def show_images(docs, max_images=5, dest_dir="./images"):
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)
    image_list = []
    for doc in docs[:max_images]:
        url = doc.tags["uri_absolute"]
        filename = f"{dest_dir}/{url.split('/')[-1]}"
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)

        image = open(filename, "rb").read()
        widget = widgets.Image(value=image, format="jpg", width=300, height=400)
        image_list.append(widget)
    box = widgets.HBox(image_list)
    display.display(box)

def cleanup():
    rmtree("workspace", ignore_errors=True)
    rmtree("images", ignore_errors=True)
    for item in os.listdir():
        if item.endswith(".jpg"):
            os.remove(item)
