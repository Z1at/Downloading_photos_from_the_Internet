import os
from DownloadPhotos import DownloadPhotos


class CommandLine:
    def __init__(self):
        self.path = os.getcwd()

    def down(self, name):
        self.path = os.path.join(self.path, name)
        return DownloadPhotos.create_folder(self.path)

    def up(self):
        self.path = os.path.split(self.path)[0]

    def get_photos(self, request, quantity):
        DownloadPhotos.get_photos(self.path, request, quantity)

    def get_files(self):
        return os.listdir(self.path)

    def get_path(self):
        return self.path

    def delete(self):
        DownloadPhotos.delete_folder(self.path)
        self.up()
