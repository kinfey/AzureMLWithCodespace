import os
from zipfile import ZipFile
import urllib.request


data_file = './fowl_data.zip'
download_url = 'https://azuremlexamples.blob.core.windows.net/datasets/fowl_data.zip'
urllib.request.urlretrieve(download_url, filename=data_file)

with ZipFile(data_file, 'r') as zip:
    print('extracting files...')
    zip.extractall()
    print('finished extracting')
    data_dir = zip.namelist()[0]

os.remove(data_file)
