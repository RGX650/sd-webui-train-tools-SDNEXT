import sys
import cv2
import os
import numpy as np

def transparence2Black(img) -> cv2.Mat:
    sp = img.shape
    width = sp[0]
    height = sp[1]
    for yh in range(height):
        for xw in range(width):
            color_d = img[xw, yh]
            if (len(color_d) == 4 and color_d[3] != 255):
                scale = 1-((255 - color_d[3]) / 255)

                img[xw, yh] = [color_d[0]*scale, color_d[1]
                               * scale, color_d[2]*scale, 255]
    return img

# range all image in folder

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv_img

def readCv2Images(inputPath: str, level: int = 0) -> list[(str, cv2.Mat)]:
    res = []
    import os
    for file in os.listdir(inputPath):
        if level > 0:
            if os.path.isdir(os.path.join(inputPath, file)):
                res += readCv2Images(os.path.join(inputPath, file), level-1)
        elif file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".bmp"):
            img = cv_imread(os.path.join(inputPath, file))
            res.append((file,img))
    return res

def rangeAllImage(inputPath, outputPath) -> list[cv2.Mat]:
    res = [cv2.Mat]
    import os
    for (file,img) in readCv2Images(inputPath):
        img = transparence2Black(img)
        cv2.imwrite(str(os.path.join(outputPath, file)), img)
        # convert to image
        res.append(img)
    return res

# read path from command line
if __name__ == '__main__':
    if len(sys.argv) == 3:
        rangeAllImage(sys.argv[1], sys.argv[2])
    else:
        print("please input folder path")