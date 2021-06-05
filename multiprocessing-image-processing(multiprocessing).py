import concurrent.futures
import time
from PIL import Image, ImageFilter
import glob
import os

size = (1200, 1200)
img_dir = 'Images'
proc_dir = "Processed"

img_paths = glob.glob(f'{img_dir}{os.path.sep}*.jpg')
print(f"{len(img_paths)} images found")

def process_image(img_path):
    img = Image.open(img_path)
    img = img.filter(ImageFilter.GaussianBlur(25))
    img.thumbnail(size)
    img.save(img_path.replace(img_dir, proc_dir))
    print(f'{os.path.split(img_path)[1]} was processed')


start = time.time()
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(process_image, img_paths)

end = time.time()
print(f'Total time elapsed: {end-start} seconds')



