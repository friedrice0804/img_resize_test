import os
import glob
from PIL import Image

files = glob.glob('./images/*')

for f in files:
    try:
        filters = {'nearest': 0, 'lanczos': 1}
        img = Image.open(f)
        img_resize = img.resize((int(img.width/2), int(img.height/2)), filters['nearest'])

        print('titles: {}'.format(os.path.splitext(f)))
        
        title, ext = os.path.splitext(f)
        img_resize.save(title + '_half' + ext)
    except OSError as e:
        print("ERROR -> ", e)

