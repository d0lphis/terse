#!/usr/bin/python

import argparse, glob, os
from PIL import Image

formats = ["BMP", "DIB", "EPS", "GIF", "ICNS", "ICO", "IM", "JPG", "JPEG",
           "J2K", "J2P", "JPX", "MSP", "PCX", "PNG", "PPM", "SGI",
           "SPIDER", "TGA", "TIFF", "WebP", "XBM"]
parser = argparse.ArgumentParser(description="Pillow example - batch converter.")
parser.add_argument('-outdir', default='.', help='Directory to save converted image files')
parser.add_argument('outformat', choices=formats,
                    help='Output image format required. The output file will be written with the same base-name as the input file, but with an extension reflecting the format')
parser.add_argument('infiles', nargs='+', help='File pattern of input image files, use *, ? and [] to specify patterns')
args = parser.parse_args()

infiles = []
for name in args.infiles:
    infiles += glob.glob(name)

for fname in infiles:
    if os.path.isdir(fname): continue
    base = os.path.basename(fname)
    f, ext = os.path.splitext(base)
    if len(ext) <= 1: continue
    ext = ext[1:]
    if ext.upper() not in formats:
        print('{}: format not supported .. ignoring'.format(fname))
        continue
    image = Image.open(fname)
    opath = os.path.join(args.outdir, '{}.{}'.format(f, args.outformat.lower()))
    image.save(opath, args.outformat)
