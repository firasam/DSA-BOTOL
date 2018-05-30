import scandir
import os
import image_compression

if __name__ == '__main__':
    image_folder = 'images/'
    for n, image_file in enumerate(scandir.scandir(image_folder)):
        img = image_file
        path = img.path.split("/")[1]
        save = 'result/' + path
        #print(path)
        os.system("python image_compression.py -c %s -k 80 80 80 -f %s" % (img.path,save))
         