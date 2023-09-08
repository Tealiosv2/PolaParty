import datetime


class Polaroid:
    def __init__(self, **kwargs):
        self.image_path = kwargs["image_path"]
        self.name = kwargs["name"]
        self.date = kwargs["date"]
        self.description = kwargs["description"]

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Date: {self.date}\n" \
               f"Description: {self.description}\n" \
               f"Image Path: {self.image_path}\n"

