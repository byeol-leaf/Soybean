import os
file_path = 'E:\deeplearning project\code\Soybean\ImgTools\Bean'
file_names = os.listdir(file_path)


i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1