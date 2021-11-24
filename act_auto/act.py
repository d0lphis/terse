from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random, datetime
import numpy

def wait_element_loaded(browser, xpath):
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )





# param: xpath for items in section to click
def get_section_links(browser, xpath):
    res = []

    try:
        wait_element_loaded(browser, xpath)
        elements = browser.find_elements_by_xpath(xpath)

        res = elements

        # list = range(0, len(elements) - 1)
        # idxs_links = random.sample(list, 2)

        # for idx in idxs_links:
        #     # elements[idx].click()
        #     # time.sleep(1)
        #     res.append(elements[idx])

        # i = 0
        # for ele in elements:
        #     # print(ele.get_atribute('href'))
        #     ele.click()

        #     i += 1
        #     if i == 2:
        #         break
    finally:
        print('')
    #     time.sleep(10)
    #     browser.quit()

    return res

# def get_random_elements(all_items_links, count):
#     all_items_links_to_read = []
#     list = range(0, len(all_items_links) - 1)
#     idxs_links = random.sample(list, count)
#     for idx in idxs_links:
#         # elements[idx].click()
#         # time.sleep(1)
#         all_items_links_to_read.append(all_items_links[idx])
#     return all_items_links_to_read

def read_some_paragraphs(items_link_to_read):
    list = range(0, len(items_link_to_read) - 1)
    idxs_links = random.sample(list, random.randint(12, 16))
    for idx in idxs_links:
        item_link = items_link_to_read[idx]
        browser.execute_script("arguments[0].scrollIntoView();", item_link)
        item_link.click()

        all_tabs = browser.window_handles
        for tab in all_tabs:
            if tab != first_tab:
                browser.switch_to.window(tab)

        # first paragraph: 
        wait_element_loaded(browser, '//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[3]/div[1]/p[1]')
        simulate_manual_scroll_up_and_down(browser)
        browser.close()

        browser.switch_to.window(first_tab)
        # break


def watch_some_vids(items_link_to_watch):
    list = range(0, len(items_link_to_watch) - 1)
    idxs_links = random.sample(list, random.randint(2, 3))
    for idx in idxs_links:
        item_link = items_link_to_watch[idx]
        browser.execute_script("arguments[0].scrollIntoView();", item_link)
        item_link.click()

        all_tabs = browser.window_handles
        for tab in all_tabs:
            if tab != first_tab:
                browser.switch_to.window(tab)

        # video title
        vid_title_xpath = '//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[1]/div[1]' 
        wait_element_loaded(browser, vid_title_xpath)
        vid_title = browser.find_element_by_xpath(vid_title_xpath)
        # browser.execute_script("arguments[0].scrollIntoView();", vid_title)
        vid_title_location = vid_title.location
        browser.execute_script('window.scrollBy(0, %s)' % (vid_title_location['y']))
        time.sleep(random.uniform(61, 70))
        browser.close()

        browser.switch_to.window(first_tab)
        # break

def simulate_manual_scroll_up_and_down(browser):
    # xuexi.cn advertise image
    title_xpath = '//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[1]/div'
    title = browser.find_element_by_xpath(title_xpath)
    title_location = title.location
    ad_xpath = '//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[3]/div[1]/div/img'
    ad_img = browser.find_element_by_xpath(ad_xpath)
    ad_img_location = ad_img.location

    current_height = 0
    total_height = browser.execute_script('return action=document.body.scrollHeight')

    simulate_view_start_timestamp = datetime.datetime.now()

    while True:
        # for i in range(0, total_height, random.uniform(1, 300)):
        for down_pixel in numpy.arange(0, total_height, random.uniform(1, 50)):
            random.seed()

            # if current_height > total_height * 0.5:
            # if EC.visibility_of_element_located((By.XPATH, ad_xpath)):
            if current_height > ad_img_location['y']:
                break

            # time.sleep(random.randint(0, 3))
            time.sleep(random.uniform(3, 6))
            browser.execute_script('window.scrollBy(0, %s)' % (down_pixel))
            current_height += down_pixel

        simulate_view_duration = (datetime.datetime.now() - simulate_view_start_timestamp).seconds
        if simulate_view_duration > 60:
            break

        # time.sleep(random.randint(60, 66) - simulate_view_duration)
        for up_pixel in numpy.arange(0, total_height, random.uniform(1, 100)):
            random.seed()

            # if current_height < total_height * 0.2:
            # if EC.visibility_of_element_located((By.XPATH, ad_xpath)):
            if current_height < title_location['y']:
                break

            time.sleep(random.uniform(2, 5))
            browser.execute_script('window.scrollBy(0, %s)' % (-up_pixel))
            current_height -= up_pixel

        simulate_view_duration = (datetime.datetime.now() - simulate_view_start_timestamp).seconds
        if simulate_view_duration > 60:
            break



### launch Chrome simply
# driver_path = r"C:\D\por\SeleniumDriver\chromedriver.exe"
# browser = webdriver.Chrome(executable_path=driver_path)
# browser = webdriver.Chrome()

### launch Chrome by specifying user profile
# options = webdriver.ChromeOptions()
# options.add_argument(r"--user-data-dir=C:/Users/Will/AppData/Local/Google/Chrome/User Data")
# options.add_argument("--profile-directory=Default")
# options.add_argument(r'--disk-cache-dir="%Temp%\Chrome"')
# options.add_argument("--user-agent=android")
# options.add_argument("disable-infobars")
# options.add_argument("start-maximized")
# options.add_argument(r'--enable-extensions')
# options.add_argument(r'--enable-user-scripts')
# browser = webdriver.Chrome(options=options,executable_path=driver_path)

### launch Edge by specifying user profile
# pip install msedge-selenium-tools selenium==3.141
# from msedge.selenium_tools import Edge,EdgeOptions
# driver_path = r"C:\D\por\SeleniumDriver\MicrosoftWebDriver.exe"
# options = EdgeOptions()
# options.use_chromium = True
# options.add_argument(r"--user-data-dir=C:\Users\Will\AppData\Local\Microsoft\Edge\User Data")
# browser = Edge(options=options,executable_path=driver_path)

### firstly launch the command to open Edge: "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --profile-directory=Default --remote-debugging-port=65500 --user-data-dir="C:\Users\Will\AppData\Local\Microsoft\Edge\User Data\Debug"
### logon
### then execute this script
# pip install msedge-selenium-tools selenium==3.141
from msedge.selenium_tools import Edge,EdgeOptions
driver_path = r"C:\D\por\SeleniumDriver\MicrosoftWebDriver.exe"
options = EdgeOptions()
options.use_chromium = True
options.add_experimental_option("debuggerAddress", "127.0.0.1:65500")
options.add_argument("--user-agent=android")
# options.add_argument("−−mute−audio")
options.add_argument("--headless");  #hide browser
browser = Edge(options=options,executable_path=driver_path)




url = 'https://www.xuexi.cn/'
#url = 'https://pc.xuexi.cn/points/my-points.html'
#url = 'https://www.xuexi.cn/xxqg.html?id=d6cf0ec34e5c41afbbd5fa99fdf90c7a'
browser.get(url)	#open browser

# time.sleep(20)    #hold for manual logon



# browser.maximize_window()
first_tab = browser.current_window_handle
# sys.exit()



# top lines
# //*[@id="d6df"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[1]/div[1]/div/div/div/span
# //*[@id="d6df"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/span
# //*[@id="d6df"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[2]/div[1]/div/div/div/span
# //*[@id="d6df"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[2]/div[2]/div/div/div/span
# //*[@id="d6df"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[3]/div[1]/div/div/div/span
# //*[@id="d6df"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[3]/div[2]/div/div/div/span
# //*[@id="d6df"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[4]/div[1]/div/div/div/span
# //*[@id="d6df"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[4]/div[2]/div/div/div/span
top_lines_links = get_section_links(browser, '//*[@id="d6df"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[*]/div[*]/div/div/div/span')

# important news
# //*[@id="231c"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[1]/div[1]/div/div/div/span
# //*[@id="231c"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[2]/div[8]/div/div/div/span
important_news_links = get_section_links(browser, '//*[@id="231c"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[*]/div[*]/div/div/div/span')

# study review
study_review_links = get_section_links(browser, '//*[@id="f657"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[*]/div[*]/div/div/div/span')

# comprehensive news
comprehensive_news_links = get_section_links(browser, '//*[@id="4d3a"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div[*]/div[*]/div/div/div/span')



all_items_links = top_lines_links + important_news_links + study_review_links + comprehensive_news_links
# all_items_links_to_read = get_random_elements(all_items_links, random.randint(6, 8))
read_some_paragraphs(all_items_links)


















# browser.execute_script('window.scrollTo(150, 7000)')
# study TV
# //*[@id="1018"]/div/div/div/div/div/section/section/div/div/section/div[1]/div/div/div[1]/span/div
# //*[@id="1018"]/div/div/div/div/div/section/section/div/div/section/div[2]/div/div/div[1]/span/div
# //*[@id="1018"]/div/div/div/div/div/section/section/div/div/section/div[3]/div/div/div[1]/span/div
# //*[@id="1018"]/div/div/div/div/div/section/section/div/div/section/div[4]/div/div/div[1]/span/div
# study_tv_important_links_xpath = '//*[@id="1018"]/div/div/div/div/div/section/section/div/div/section/div[*]/div/div/div[1]/span/div'
# //*[@id="9309"]/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/section/div/div/section/div[1]/div/div/div[1]/span/div
# //*[@id="9309"]/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/section/div/div/section/div[2]/div/div/div[1]/span/div
# //*[@id="9309"]/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/section/div/div/section/div[3]/div/div/div[1]/span/div
# //*[@id="9309"]/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/section/div/div/section/div[4]/div/div/div[1]/span/div
study_tv_important_links_xpath = '//*[@id="9309"]/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/section/section/div/div/section/div[*]/div/div/div[1]/span/div'
study_tv_important_links = get_section_links(browser, study_tv_important_links_xpath)
# study_tv_important_links_to_read = get_random_elements(study_tv_important_links, random.randint(2, 3))
watch_some_vids(study_tv_important_links)



study_tv_topic_tab_xpath = '//*[@id="9309"]/div/div/div/div/div/div/div/div[2]/div/section/div/div/div/div/div/section/div/div/div/div/div/section/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div'
study_tv_topic_tab = browser.find_element_by_xpath(study_tv_topic_tab_xpath)
browser.execute_script("arguments[0].scrollIntoView();", study_tv_topic_tab)
study_tv_topic_tab.click()
# //*[@id="f2f1"]/div/div/div/div/div/section/section/div/div/section/div[1]/div/div/div[1]/span/div
# //*[@id="f2f1"]/div/div/div/div/div/section/section/div/div/section/div[2]/div/div/div[1]/span/div
# //*[@id="f2f1"]/div/div/div/div/div/section/section/div/div/section/div[3]/div/div/div[1]/span/div
# //*[@id="f2f1"]/div/div/div/div/div/section/section/div/div/section/div[4]/div/div/div[1]/span/div
# study_tv_topic_links_xpath = '//*[@id="f2f1"]/div/div/div/div/div/section/section/div/div/section/div[*]/div/div/div[1]/span/div'
study_tv_topic_links_xpath = study_tv_important_links_xpath
study_tv_topic_links = get_section_links(browser, study_tv_important_links_xpath)
# study_tv_topic_links_to_read = get_random_elements(study_tv_topic_links, random.randint(2, 3))
watch_some_vids(study_tv_topic_links)


# study_tv_sight_tab_xpath = '//*[@id="5ea4"]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div'
study_tv_sight_tab_xpath = study_tv_topic_tab_xpath
study_tv_sight_tab = browser.find_element_by_xpath(study_tv_sight_tab_xpath)
browser.execute_script("arguments[0].scrollIntoView();", study_tv_sight_tab)
study_tv_sight_tab.click()
# study_tv_sight_links_xpath = '//*[@id="c5bb"]/div/div/div/div/div/section/section/div/div/section/div[*]/div/div/div[1]/span/div'
study_tv_sight_links_xpath = study_tv_important_links_xpath
study_tv_sight_links = get_section_links(browser, study_tv_sight_links_xpath)
# study_tv_sight_links_to_read = get_random_elements(study_tv_sight_links, random.randint(2, 3))
watch_some_vids(study_tv_sight_links)











#browser.implicitly_wait(10)
#time.sleep(2)


