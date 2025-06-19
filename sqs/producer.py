import sys
import os
import boto3
import requests

def download_image(url:str) -> str:
    r = requests.get(url=url)
    if r.status_code == 200:
        print('Download feito com sucesso!!!')
    else:
        print('Ocorreu um erro ao baixar a imagem, tente outro link...')

if __name__ == "__main__":
    print("Iniciando processo de download de imagem...")
    url_download = sys.argv[1]
    download_image(url_download)
