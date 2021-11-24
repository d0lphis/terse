# coding=utf-8

# [requirement]
# install Microsoft Visual C++ 14.0+
# conda install shapely
# conda install nomkl
# conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# conda activate paddle_env
# python -m pip install "paddleocr>=2.0.1"
# python -m pip install paddlepaddle

# [usage]
# python convert_img_to_txt_paddleocr.py a.jpg


import sys

import vidder






def main():
    IMG_FILE_FULL_NAME = sys.argv[1]
    texts = vidder.extract_texts(IMG_FILE_FULL_NAME)
    for line in texts:
        print(line[1][0])

if __name__ == "__main__":
    main()