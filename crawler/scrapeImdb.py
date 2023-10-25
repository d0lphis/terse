import os, json, time,glob

import requests, urllib
from urllib.request import urlopen

from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd
from threading import Thread



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

def scrape_mvi_info(imdb_id):
    print("\nmovie imdb id:", imdb_id)
    
    print(f"  > start scraping movie info")

    r = requests.get(url="https://www.imdb.com/title/" + imdb_id, headers=headers)
    print("    scrape trailer video responses:", r.status_code)
    
    soup = BeautifulSoup(r.text, 'html.parser')                             # Create a BeautifulSoup object
    jsonData = soup.find('script', {"type": "application/ld+json"})
    # print("    " + jsonData.string)
    jsonSourceObj = json.loads(jsonData.string)
    movie = {}
    movie['title'] = jsonSourceObj['name']

    if 'description' in jsonSourceObj:
        movie['description'] = jsonSourceObj['description']

    if 'image' in jsonSourceObj:
        movie['image'] = jsonSourceObj['image']

    movie['trailer_id'] = ""

    if 'keywords' in jsonSourceObj:
        movie['keywords'] = jsonSourceObj['keywords']
    if 'director' in jsonSourceObj:
        movie['director'] = jsonSourceObj['director']
    if 'actor' in jsonSourceObj:
        movie['actor'] = jsonSourceObj['actor']
    if 'datePublished' in jsonSourceObj:
        movie['datePublished'] = jsonSourceObj['datePublished']

    try:
        if 'trailer' in jsonSourceObj:
            movie['trailer_vid'] = jsonSourceObj['trailer']['embedUrl'].split('/')[-1]
            movie['trailer_name'] = jsonSourceObj['trailer']['name']
            movie['trailer_description'] = jsonSourceObj['trailer']['description']
    except:
        print("    trailer URL not found")
    # print("    " + movie)
    
    print(f"  > finish scraping movie info")

    return movie
##############

def get_video_link_by_imdbid(video_id):
    print("\n  > start getting video link by trailer id")
    # print("    trailer id:", video_id)

    video_url = "https://www.imdb.com/video/"+video_id
    print("    trailer url:", video_url)
    r = requests.get(url=video_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    script = soup.find("script", {'type': 'application/json'})
    # print("    " + script)
    json_object = json.loads(script.string)
    # print("    " + json_object["props"]["pageProps"]["videoPlaybackData"]["video"]["playbackURLs"])
    videos = json_object["props"]["pageProps"]["videoPlaybackData"]["video"]["playbackURLs"]                # links video quality order auto,1080,720

    for video in videos[1:]:
        video_link = video["url"]
        # print("    " + video_link)
        break
    print("    trailer download link:", video_url)

    print(f"  > finish getting video link by trailer id")

    return video_link

def download_video(video_url, video_save_full_path):
    print(f"\n  > start downloading trailer")
    print("    trailer url:", video_url)

    if not os.path.exists(video_save_full_path):
        file_size_str = requests.head(video_url).headers['Content-Length']
        file_size = str(float(file_size_str)/1024/1024)
        print("    " + file_size + " MB")

        # r = requests.get(video_url, headers=headers)
        ru = urlopen(video_url)
        # f = open(f"trailers/"+imdb_id+'-'+mvi_title+".mp4", 'wb')
        f = open(video_save_full_path, 'wb')

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = ru.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            s = file_size_dl/1024/1024
            if s % 5 == 0:
                print("    " + str(float(file_size_dl/1024/1024)), "MB Downloaded")
            f.write(buffer)
        #    status = str( (file_size_dl, file_size_dl * 100. / float(file_size_str)))
        #    status = status + chr(8)*(len(status)+1)
        #    print(status)

        f.close()

    #    with open('videos/'+unique_filename+'.mp4', 'wb') as f:
    #        f.write(r.content)
        print(f"    trailer {video_save_full_path} downloaded")
    else:
        print(f"    trailer {video_save_full_path} already exists, skip download")

    print("  > finish downloading trailer")

def download_poster(poster_url, poster_save_full_path):
    print("\n  > start downloading poster")
    print("    poster url:", poster_url)

    if not os.path.exists(poster_save_full_path):
        img_url = "https://m.media-amazon." + poster_url.split(".")[2] + "."
        r = requests.get(img_url, headers=headers)
        # with open(f'trailers/'+imdb_id+'-'+mvi_title+'.JPG', 'wb') as f:
        #     f.write(r.content)
        with open(poster_save_full_path, 'wb') as f:
            f.write(r.content)
        print(f"    poster {poster_save_full_path} downloaded")
    else:
        print(f"    poster {poster_save_full_path} already exists, skip download")

    print("  > finish downloading poster")

def get_mvi_file_name_in_folder(folder_path):
    list_of_files = filter(os.path.isfile, glob.glob(os.path.join(folder_path, '*')))
    large_file_full_name = max(list_of_files, key = lambda x: os.stat(x).st_size)
    large_file_size = os.stat(large_file_full_name).st_size
    the_mvi_file_name = None
    if large_file_size > 200*1024*1024:
        the_mvi_file_name = os.path.splitext(os.path.basename(large_file_full_name))[0]
        print("    movie file detected:", large_file_size/(1024*1024*1024), 'G', '\t', the_mvi_file_name)
    else:
        print("    no movie file found, set movie name as a")
    return the_mvi_file_name

def update_trailer_path_in_nfo(nfo_file_path, trailer_local_file_full_path):
    print(f"\n  > start updating nfo {nfo_file_path}")
    print("    nfo local path:", nfo_file_path)

    if os.path.exists(trailer_local_file_full_path):
        nfo = etree.parse(nfo_file_path)
        trailer = nfo.getroot().findall("trailer")[0]

        original_online_trailer_url = trailer.text if trailer.text != None else ""

        tailer_local_file_name = "".join(os.path.splitext(os.path.basename(trailer_local_file_full_path)))
        if tailer_local_file_name not in original_online_trailer_url:
            commented_online_trailer_dom = etree.Comment("".join(["<trailer>", original_online_trailer_url.replace("&", "&amp;"), "</trailer>"]))
            print(commented_online_trailer_dom.text)

            trailer.addnext(commented_online_trailer_dom)                                           # comment original online trailer section
            trailer.text = tailer_local_file_name                                                   # generate local trailer section

            nfo.write(nfo_file_path, xml_declaration=True)
            print(f"    trailer path updated from {original_online_trailer_url} to {tailer_local_file_name} in nfo")
        else:
            print(f"    trailer path already directs to {tailer_local_file_name} in nfo, skip update")
    else:
        print(f"    trailer local path provided {trailer_local_file_full_path} not existing, skip update")
    print(f"  > finish updating nfo")

def scrape_imdb_to_local(imdb_id, nfo_file_path):
    mvi_title = None
    if imdb_id != None:
        movie = scrape_mvi_info(imdb_id)
        if not 'trailer_vid' in movie:
            print("not trailer scraped from imdb, skip download")
            return
        # with open(f'trailers/'+imdb_id +'.json', 'w') as json_file:
        #     json.dump(movie, json_file)

        print(f"\n  > start constructing params")
        mvi_title = movie['title'].replace(": ", " - ").replace("：", " - ")
        print("    movie title:", mvi_title)

        trailer_id = movie['trailer_vid']
        print("    movie trailer id:", trailer_id)

        mvi_folder_path = os.path.dirname(nfo_file_path)
        print("    movie local folder path:", mvi_folder_path)
        # os.makedirs('trailers/', exist_ok=True)

        trailer_local_file_name = get_mvi_file_name_in_folder(mvi_folder_path)
        trailer_local_file_name = trailer_local_file_name if trailer_local_file_name != None else "a"
        trailer_local_file_full_path = os.path.join(mvi_folder_path, trailer_local_file_name + "-trailer.mp4")
        print("    trailer local file path to save:", trailer_local_file_full_path)

        poster_local_file_full_path = os.path.join(mvi_folder_path, imdb_id + "." + mvi_title + ".imdb-poster.gif")
        print("    poster local file path to save:", poster_local_file_full_path)

        print(f"  > finish constructing params")

        download_video(get_video_link_by_imdbid(trailer_id), trailer_local_file_full_path)

        download_poster(movie['image'], poster_local_file_full_path)

    update_trailer_path_in_nfo(nfo_file_path, trailer_local_file_full_path)

    





def start(vids_info):
    # # os.makedirs('trailers', exist_ok=True)
    # imdb_ids = []                                                                             # media folder and imdb id pairs provided(for handling multiple movie folders batchly)
    # if type(vids_info) == dict:
    #     imdb_ids = [v for k, v in vids_info.items()]
    # elif type(vids_info) == list:                                                             # a list of imdb ids provided
    #     imdb_ids = vids_info
    # elif os.path.exists(vids_info):                                                           # a csv file containing imdb ids provided
    #     imdb_ids = pd.read_csv(vids_info).iloc[:, 0]
    #     imdb_ids = list(imdb_ids)
    # else:
    #     print("param wrong")
    #     return

    # # print(imdb_ids)
    # # return

    # # for imdb_id in imdb_ids :
    # #     scrape_imdb_to_local(imdb_id)

    # # '''
    # # paralle processing
    # threads = []
    # for imdb_id in imdb_ids:
    #     process = Thread(target=scrape_imdb_to_local, args=[imdb_id, vids_info[imdb_id]])
    #     process.start()
    #     threads.append(process)
    #     time.sleep(2.5)  # ip gets blocked
    # for process in threads:
    #     process.join()
    # # '''

    threads = []
    for nfo_file_path, imdb_id in vids_info.items():
        process = Thread(target=scrape_imdb_to_local, args=[imdb_id, nfo_file_path])
        process.start()
        threads.append(process)
        time.sleep(2.5)  # ip gets blocked
    for process in threads:
        process.join()







# get_mvi_file_name_in_folder("E:\\mediago\\thmovie\\company\\moviefolder\\")       #the direct movie folder that contains movie file, non suport recursive



# scrape_imdb_to_local(imdb_id='tt1160419')



# start(vids_info='conf/imdb_ids.csv')



# start(
#     vids_info=[
#         "tt1843866",
#         "tt3498820",
#         "tt0458339",
#     ]
# )



import argparse
parser = argparse.ArgumentParser()
parser.add_argument("base_dir", help="the base folder to generate movie folders")
args = parser.parse_args()
print(args.base_dir)

# base_dir = "E:\\mediago\\thmovie\\"
# base_dir = "C:\\Users\\Will\\Desktop\\a\\"
base_dir = args.base_dir

# vids_info = []
vids_info = {}
nfo_files = glob.glob(base_dir+"\\**\\*.nfo", recursive=True)
for nfo_file_path in nfo_files:
    # print(nfo_file_path)
    imdb_id = etree.parse(nfo_file_path).getroot().findall("id")[0].text
    # print(imdb_id)
    # vids_info.append(imdb_id)
    vids_info[nfo_file_path] = imdb_id
    # break
print(vids_info)
start(vids_info)

