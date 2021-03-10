"""
@Software: PyCharm
@File    : read_video.py
@Time    : 2021/2/28
@Author  : xhjiang
@aim     : obtain images

"""

import cv2
import numpy as np
import os
import random
from PIL import Image


if __name__ == '__main__':

    src_path = 'F:/dataset/codec_sequence/wangsiqi/CDVL/selected/no_deal'
    dst_path = 'F:/dataset/codec_sequence/wangsiqi/CDVL/selected_images'

    # if not os.path.exists(dst_path):
    #     os.mkdir(dst_path)

    file_lists = os.listdir(src_path)

    for i, file in enumerate(file_lists):
        save_image_path=dst_path+'/'+str(i)
        if not os.path.exists(save_image_path):
            os.mkdir(save_image_path)
        print('%d / %d: %s'%(i, len(file_lists), file))
        path = os.path.join(src_path, file)
        vid = cv2.VideoCapture(path)
        if not vid.isOpened():
            continue

        width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = vid.get(cv2.CAP_PROP_FPS)
        number = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))


        index=0
        count = 0
        while(True):
            count += 1
            succ, frame = vid.read()
            if not succ:
                break

            cv2.imwrite(os.path.join(save_image_path, '{:06d}.png'.format(count)), frame)

            print('%d / %d'%(count, number))