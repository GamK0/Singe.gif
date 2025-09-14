import imageio.v3 as iio

filenames = ['singe1.jpg', 'singe2.jpg', 'singe3.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('singe.gif', images, duration = 500, loop = 0)