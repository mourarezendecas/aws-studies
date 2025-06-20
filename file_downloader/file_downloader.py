import requests
import mimetypes
from dataclasses import dataclass

@dataclass
class FileDownloader:
    url:str

    def download_image(self):
        response = requests.get(url=self.url)
        response.raise_for_status()
        return response

    def get_filename(self, response):
        if "content-disposition" in response.headers:
            content_disposition = response.headers["content-disposition"]
            filename = content_disposition.split("filename=")[1]
        else:
            filename = self.url.split("/")[-1]
            with open(filename, mode="wb") as file:
                file.write(response.content)
        print(f"Nome do arquivo: {filename}")
        return filename

    def get_mimetype(self, object_name):
        guessed_mimetype, _ = mimetypes.guess_type(object_name)
        if guessed_mimetype:
            content_type = guessed_mimetype
        else:
            content_type = 'application/octet-stream'
        return content_type