from os import listdir
from os.path import isfile, join
from PIL import Image

mypath = "train2014/"
files = [f for f  in listdir(mypath) if isfile(join(mypath,f)) and f[-4:]==".jpg"]
outpath = "training_val2014/"
for i in range(82783):
    image = Image.open(f"{mypath}/{files[i]}")
    new_image = image.resize((256,256))
    new_image.save(f"{outpath}/{files[i]}")

