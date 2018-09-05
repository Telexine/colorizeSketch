from PIL import Image
import glob
import sys





def merge_images(file1, file2):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result




O_image_list = []
g_image_list = []
c=1
for filename in glob.glob('ori/*.jpg'): #assuming gif
    O_image_list.append(filename)
    new_im = merge_images(filename,filename.replace("ori\\","g\\"))
    new_im.save("output/m_{0:000}.jpg".format(c))
    c=c+1

print("mergs ",c , "pictures")