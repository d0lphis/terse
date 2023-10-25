# USAGE:
#  python ./scraper.py
# cd <base_dir>
# tinyMediaManagerCMD movie -u -n -t

import os, regex, time
from lxml import etree
import pymysql, requests
import concurrent.futures
# from threading import Thread
# from threading import Lock

# from MultithreadDownloaderCliWithProgressForSingleFile.Downloader import Downloader

# scrap
#   'https://www.douban.com/doulist/1654175/?start=0&sort=seq&playable=0&sub_type=
#   'https://www.douban.com/doulist/1654175/?start=25&sort=seq&playable=0&sub_type=
#   'https://www.douban.com/doulist/1654175/?start=50&sort=seq&playable=0&sub_type=
#   'https://www.douban.com/doulist/1654175/?start=75&sort=seq&playable=0&sub_type=
#   'https://www.douban.com/doulist/1654175/?start=100&sort=seq&playable=0&sub_type=
# then get chinese name, english name and year from html content, and construct folder name
# then create folders



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
posterDownloadInfo = {}

def savePoster(posterStr, mviPosterFilePath):
    # response = requests.get(posterStr, headers=headers, timeout=(10, 10))
    response = requests.get(posterStr, headers=headers)
    print(f"Status Code: {response.status_code}")

    if response.content != "":
        with open(mviPosterFilePath, "wb") as f:
            f.write(response.content)
        return response.content

def downloadPoster(posterStr, mviPosterFilePath):
    if os.path.isfile(mviPosterFilePath):
        print("    ", mviPosterFilePath + ' already exists')
        return None
    else:
        # for k in ["l_ratio_poster", "m_ratio_poster", "s_ratio_poster"]:
        #   # print(posterStr.replace("l_ratio_poster", k))
        #   savePoster(posterStr.replace("l_ratio_poster", k), mviPosterFilePath)
        #   # os.system("pause")
        return savePoster(posterStr, mviPosterFilePath)

def scapeDoubanTopList(top_list_urls):
    # db = pymysql.connect(host="", port=3306, user="root",
    #                      password="123456", db="bo", charset="utf8")
    # cursor = db.cursor()
    # csvv = open('E://爬虫数据/豆瓣排行数据+演员.csv', 'w+', newline='', encoding='utf-8-sig')
    # writer = csv.writer(csvv)
    # writer.writerow(('排名', '电影名称', '导演','演员','国家', '评分', '评价人数', '名句'))

    for url in top_list_urls:
        re = requests.get(url, headers=headers)
        # print(re)
        ye = etree.HTML(re.text)
        # print(ye)
        infos = ye.xpath('//div[@id="wrapper"]//ol[1]/li')
        # print(infos)
        for info in infos:
            yanyuan = info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().split('\n')[0].strip().split('\xa0')[-1].split(':')[-1]
            # print(info)
            num = info.xpath('.//div[@class="pic"]/em/text()')[0]
            name = info.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]
            daoyan = info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().split('\n')[0].split('\xa0')[0].split(':')[1].strip()
            guojia = info.xpath('.//div[@class="bd"]/p')[0].xpath('string(.)').strip().replace('\xa0','').split('\n')[1].split('/')[1].split()[0]
            pingfen = info.xpath('.//div[@class="star"]/span[2]/text()')[0]
            pingjiarenshu = info.xpath('.//div[@class="star"]/span[4]/text()')[0]
            mingju = info.xpath('.//div[@class="bd"]//p//span/text()')
            if not mingju:
                mingju = "无"
            mingju = mingju[0]
            print(num,name,daoyan,yanyuan,guojia,pingfen,pingjiarenshu,mingju)
            # sql = 'insert into doub values ("%s","%s","%s","%s","%s","%s","%s","%s")' % (num,name,daoyan,yanyuan,guojia,pingfen,pingjiarenshu,mingju)
            # cursor.execute(sql)
            # db.commit()
            #             writer.writerow((num,name,daoyan,yanyuan,guojia,pingfen,pingjiarenshu,mingju))

def scapeDoubanDouList(dou_list_urls, base_dir):
    for url in dou_list_urls:
        print(url)
        re = requests.get(url, headers=headers)
        # print(re)
        ye = etree.HTML(re.text)
        # print(ye)
        # infos = ye.xpath('//div[@id="content"]//div[@class="doulist-item"]')
        infos = ye.xpath('//div[@id="content"]//div[contains(@class, "doulist-item")]')
        # print(infos)
        # print(len(infos))
        i = 0
        for info in infos:
            print()
            try:
                # i += 1
                # print(i,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                # print(info)

                titleRaw = info.xpath('.//div[@class="title"]/a/text()')
                titleRawStr = str("".join(titleRaw).replace("\n", "").strip())
                # print(titleRawStr)

                if (titleRawStr.__contains__(" 第")):
                    continue

                # titleRawList = regex.findall(r'[a-z]+(?:\s+[a-z]+)*|[\u4e00-\u9fa5]+(?:\s+[\u4e00-\u9fa5]+)*', titleRawStr, regex.I)
                # titleRawList = regex.split('(?<=[A-Za-z+])\s*(?=[\u4e00-\u9fa5+])', titleRawStr)
                titleRawList = regex.split(' ', titleRawStr, 1)

                titleStrChs = titleRawList[0]
                # print(titleStrChs)
                titleStrEng = titleRawList[1]
                # print(titleStrEng)
                # print(titleStrEng, titleStrChs, sep='\t')



                yearRaw = info.xpath('.//div[@class="abstract"]/text()')
                # print(yearRaw)
                yearRawStr = str("".join(yearRaw).replace("\n", "").strip())
                yearRawList = regex.split('年份: ', yearRawStr)
                # print(yearRawList)
                yearStr = yearRawList[1]
                # print("  ", yearStr)



                folderName = ".".join([titleStrEng, titleStrChs, yearStr])
                print(folderName)



                posterRaw = info.xpath('.//div[@class="post"]/a/img/@src')
                posterStrS = str("".join(posterRaw).replace("\n", "").strip())
                posterStr = posterStrS.replace("s_ratio_poster", "l_ratio_poster")
                print("  ", posterStr)



                mviFolderPath = os.path.join(base_dir, folderName.replace(": ", " - "))
                if os.path.exists(mviFolderPath):
                    print("    ", mviFolderPath + ' already exists')
                else:
                    os.mkdir(mviFolderPath)

                mviFilePath = os.path.join(mviFolderPath, "a.mp4")
                if os.path.exists(mviFilePath):
                    print("    ", mviFilePath + ' already exists')
                else:
                    with open(mviFilePath, 'w') as fp: 
                        pass





                mviPosterFilePath = os.path.join(mviFolderPath, "a-poster.jpg")
                # response = requests.get(posterStr)
                # if os.path.exists(mviPosterFilePath):
                #     print("    ", mviPosterFilePath + ' already exists')
                # else:
                #     with open(mviPosterFilePath, "wb") as f:
                #         f.write(response.content)
                #     # DOWNLOADER = Downloader(threads_num=10)
                #     # DOWNLOADER.start(
                #     #     url=posterStr,
                #     #     target_file=mviPosterFilePath,
                #     # )
                
                posterDownloadInfo[posterStr] = mviPosterFilePath



            except:
                print("info handling wrong")
            finally:
                continue

    print()
    print(posterDownloadInfo)
    # lock = Lock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        for x in posterDownloadInfo:
            print()
            print("  ", "start downloading", x, "to", posterDownloadInfo[x])
            # time.sleep(6)
            future = executor.submit(downloadPoster, x, posterDownloadInfo[x])
            # print(future.result())
            return






# top_list_urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 251, 25)]
# scapeDoubanTopList(top_list_urls)

# dou_list_urls = ['https://www.douban.com/doulist/1654175/?start={}&sort=seq&playable=0&sub_type='.format(str(i)) for i in range(0, 126, 25)]   #MCU
# dou_list_urls = ['https://www.douban.com/doulist/19820050/?start={}&sort=seq&playable=0&sub_type='.format(str(i)) for i in range(0, 26, 25)]   #DCEU
dou_list_urls = ['https://www.douban.com/doulist/46060607/?start={}&sort=seq&playable=0&sub_type='.format(str(i)) for i in range(0, 24, 25)]     #XMEN
base_dir = "C:\\Users\\Will\\Desktop\\a\\"
scapeDoubanDouList(dou_list_urls, base_dir)
