import os
import xmltodict

for filename in os.listdir():
    if filename.endswith('.xml'):
        txt_name = os.path.basename(filename)
        print(txt_name)
        with open(filename) as fd:
            annot = xmltodict.parse(fd.read())
        try:
            print(annot['annotation']['object'][0] is not None)
            for bndbox in annot['annotation']['object']:
                box = bndbox['bndbox']
                out = bndbox['name'] + ' ' + box['xmin'] + ' ' + box['ymin'] + ' ' + box['xmax'] + ' ' + box['ymax'] + '\n'
                # print(out)
        except KeyError:
            bndbox = annot['annotation']['object']
            box = bndbox['bndbox']
            out = bndbox['name'] + ' ' + box['xmin'] + ' ' + box['ymin'] + ' ' + box['xmax'] + ' ' + box['ymax'] + '\n'
            # print(out)
        output = open(txt_name + '.txt', 'a')
        output.write(out)
        output.close()