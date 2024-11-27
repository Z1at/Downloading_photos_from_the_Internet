import os
from icrawler.builtin import GoogleImageCrawler
import shutil


class DownloadPhotos:
    @staticmethod
    def create_folder(path):
        try:
            os.mkdir(path)
            return "Folder has been created"
        except FileExistsError:
            return "Folder already exists"

    @staticmethod
    def get_photos(path, request, quantity):
        google = GoogleImageCrawler(storage={'root_dir': path})
        google.crawl(keyword=" ".join(request), max_num=quantity)
        print(" ".join(request))

    @staticmethod
    def delete_folder(path):
        shutil.rmtree(path)
