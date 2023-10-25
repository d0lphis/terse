import os
import pandas as pd

def generate_folders_by_csv(csv_file, base_dir):
    folder_names = list(pd.read_csv(args.csv_file).iloc[:, 0])
    # print(folder_names)
    for folder_name in folder_names:
        folder_name = folder_name.replace(": ", " - ").replace("：", " - ")

        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        mvi_path = os.path.join(folder_path, "a.mp4")
        if not os.path.exists(mvi_path):
            with open(mvi_path, mode='a'):
                pass



import argparse
parser = argparse.ArgumentParser()
parser.add_argument("csv_file", help="the csv contains movie names with each per line")
parser.add_argument("base_dir", help="the base folder to generate movie folders")
args = parser.parse_args()
csv_file = args.csv_file
base_dir = args.base_dir

generate_folders_by_csv(csv_file, base_dir)

