# 纳尼亚传奇1 - 狮子、女巫和魔衣橱 The Chronicles of Narnia - The Lion, the Witch and the Wardrobe (2005)
# to
# The Chronicles of Narnia - The Lion, the Witch and the Wardrobe.纳尼亚传奇1 - 狮子、女巫和魔衣橱.2005

import os, re

def unify_folder_name_pattern(base_dir):

    for root, folder_names, file_names in os.walk(base_dir):
        for folder_name in folder_names:
            print("\nFolder Name:", folder_name)

            try:
                year = None
                yearText = re.search(r'\(\d+\)$', folder_name).group(0)
                if yearText != None:
                    year = yearText.replace("(", "").replace(")", "")
                
                chs_name = ""
                dash = ""
                for chs_nam in re.findall(r'[\u4e00-\u9fff()·、]+[\d]*[ - [\u4e00-\u9fff]+]*', folder_name):
                    # chs_name = chs_name.strip() + dash + chs_nam
                    chs_name = f'{chs_name.strip()} {dash} {chs_nam}'.strip()
                    dash = "-"

                eng_name = folder_name.replace(chs_name, "").replace(yearText, "").strip()

                # print("Eng Name:", repr(eng_name))
                # print("Chs Name:", chs_name)
                # print("Year:", year)
                joiner = "." if eng_name != "" else ""
                unified_name = f'{eng_name}{joiner}{chs_name}.{year}'

                # print(repr(unified_name))
                unified_name = "".join(list(s for s in unified_name if s.isprintable()))    #remove invisible chars
                print("Unified Name:", repr(unified_name))



                os.rename(os.path.join(base_dir, folder_name), os.path.join(base_dir, unified_name))
            except:
                print(f"renaming failure on {folder_name}")



import argparse
parser = argparse.ArgumentParser()
# parser.add_argument("csv_file", help="the csv contains movie names with each per line")
parser.add_argument("base_dir", help="the base folder to generate movie folders")
args = parser.parse_args()
# csv_file = args.csv_file
base_dir = args.base_dir

unify_folder_name_pattern(base_dir)

