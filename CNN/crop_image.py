import os
from PIL import Image

image_dir = './images'
save_dir = './cropped'
# image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
image_files = ['9.png']

for image_file in image_files:
  image_path = os.path.join(image_dir, image_file)
  image = Image.open(image_path)
  width, height = image.size
  piece_width = width // 4

  crop_1 = image.crop((4, 0, piece_width+2, height))
  crop_2 = image.crop((piece_width + 1, 0, piece_width * 2 - 1, height))
  crop_3 = image.crop((piece_width * 2 -2, 0, piece_width * 3 -4, height))
  crop_4 = image.crop((piece_width * 3 - 5, 0, piece_width * 4 - 7, height))

  crop_1.save(os.path.join(save_dir, 'crop_1.png'))
  crop_2.save(os.path.join(save_dir, 'crop_2.png'))
  crop_3.save(os.path.join(save_dir, 'crop_3.png'))
  crop_4.save(os.path.join(save_dir, 'crop_4.png'))

  image.close()