"""
Convert images to hexadecimal arrays
Write "python convert_img.py -i ./img_test.jpg -o ./converted_img.hex" in terminal
"""
from __future__ import division, absolute_import, print_function

import cv2
import logging
import argparse
import numpy as np
from PIL import Image
from pathlib import Path

#config for logging 
logging.basicConfig(format="%(asctime)s-%(levelname)s-%(message)s", level=logging.INFO)

def convert_hexadecimal_img(input_path, output_path, output_shape):
    #resize to specific shape
    image_arr = np.asarray(Image.open(Path(input_path).resolve())) #absolute path 
    image_arr = np.resize(image_arr, output_shape)    

    with open(Path(output_path).resolve(), "a") as file:
        for h in range(image_arr.shape[0]):
            for w in range(image_arr.shape[1]):
                for c in range(image_arr.shape[2]):
                    file.write(f'{image_arr[h][w][c]:x}')
                    file.write("\n")

def main(args):
    if args.using_webcam is True:
        video = cv2.VideoCapture(0)
        
        while True:
            _, frame = video.read()
            
            #convert to hexadecimal
            
            #display
            cv2.imshow('Webcam', frame)
            
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        
        video.release()
        cv2.destroyAllWindows()
    else:
        convert_hexadecimal_img(args.input_img, args.output_img, args.output_shape)        


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert image/video to hexadecimal")
    parser.add_argument("--using_webcam", default=False, help="Using realtime webcam or only convert images")
    parser.add_argument("-i", "--input_img", help="Input image path to convert")
    parser.add_argument("-o", "--output_img", help="Output image path to convert")
    parser.add_argument("--output_shape", default=(640, 640, 3), help="Output shape of image")

    args = parser.parse_args()
    ret = main(args)
    logging.info("Successfully converted!")
    exit(ret) 
