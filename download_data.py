# download_data.py
import gdown

url = 'https://drive.google.com/drive/folders/1WbWIvW7GkR7MF1mKQ74Nwy8HEEaj2odW?usp=drive_link'
# this is link for downloading the photos dataset
# this dataset is used for training the cycled GAN
url_photos = 'https://drive.google.com/drive/folders/1Meduo_JZx-12eyCN6oWU8vyWA6NLuAFz?usp=drive_link'
output = 'monet_dataset.zip'
gdown.download(url, output, quiet=False)


