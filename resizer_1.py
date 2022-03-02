import os
import glob
import time
from PIL import Image


class CustomExceptionHandler(Exception):
    def __init__(self) -> None:
        super().__init__()
        print('Option not available. Please try again.')
        raise SystemExit()


class Resizer(object):
    def __init__(self, folder, filter) -> None:
        self.files = glob.glob('./' + folder + '/*')
        self.filter = filter
    
    def __call__(self) -> None:
        start_ = time.time()
        for file in self.files:
            try:
                img = Image.open(file)
                img = img.resize( (int(img.width/6), int(img.height/6)), self.filter)

                title, exten = os.path.splitext(file)
                print('Resizing file: {}.{}'.format(title, exten))

                img.save(title + '_res_' + exten)
            except OSError as e:
                print("Error occured during reading files.", e)
                
        end_ = time.time()
        duration = end_-start_
        print('time took: %.2f' %duration)


def filter_list(filter) -> int:
    # Image.NEAREST (0), Image.LANCZOS (1), Image.BILINEAR (2), 
    # Image.BICUBIC (3), Image.BOX (4) or Image.HAMMING (5)
    filters = {'nearest': 0, 'lanczos': 1, 'bilinear': 2, 
               'bicubic': 3, 'box': 4, 'hamming': 5}
    sel_filter = None

    for i in filters:
        if i == filter:
            sel_filter = filter

    if sel_filter is None:
        raise CustomExceptionHandler
    else:
        sel_filter = filters[sel_filter]
        return sel_filter


if __name__ == '__main__':
    sel_filter = str(input("Select one of filter below\n"\
                           "(nearest, lanczos, bilinear, bicubic, box, hamming): "))
    sel_filter = filter_list(sel_filter)

    folder_name = str(input("folder in which images are stored: "))

    if not os.path.isdir(folder_name):
        raise FileNotFoundError
    else:
        run = Resizer(folder= folder_name, filter= sel_filter)
        run()
    



