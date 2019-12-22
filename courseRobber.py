from selenium import webdriver
from PIL import Image, ImageEnhance
import pytesseract
from retrying import retry

my_id = input('Your ID:')
my_pswd = input('Your password:')
my_course_id = input('ID of course you need:')
# my_id = 'id'
# my_pswd = 'password'
# my_course_id = 'course id'

print('Welcome. Press <Ctrl+C> or close the browser to quit.')
# chromedriver.exe must be added to PATH
driver = webdriver.Chrome()
driver.get("http://portal.ecnu.edu.cn")

driver.save_screenshot('0.png')
codeImage = driver.find_element_by_id('codeImage')
img = Image.open('0.png')
# Adjust location && size for img.crop()
left = codeImage.location['x'] * 1.51
top = codeImage.location['y'] * 1.5
right = left + codeImage.size['width'] * 1.3
bottom = top + codeImage.size['height'] * 1.5

img = img.crop((left, top, right, bottom))
img = img.convert('L')
img = ImageEnhance.Contrast(img).enhance(3)
# Single text line with only numbers
my_code = pytesseract.image_to_string(img,
config='--psm 7 -c tessedit_char_whitelist=0123456789')

driver.find_element_by_id('un').send_keys(my_id)
driver.find_element_by_id('pd').send_keys(my_pswd)
driver.find_element_by_name('code').send_keys(my_code)
driver.find_element_by_class_name('login_box_landing_btn').click()

def stop_func(attempts, delay):
    print('Loading... Attempts: %d, Delay: %d' % (attempts, delay))

@retry(wait_fixed=2000, stop_func=stop_func)
def click_edu():
    driver.find_element_by_link_text('本科教学').click()

def switch_2_new_tag():
    driver.switch_to.window(driver.window_handles[-1])

@retry(wait_fixed=2000, stop_func=stop_func)
def click_course():
    driver.find_element_by_css_selector('li.li_1 a.subMenu').click()

@retry(wait_fixed=2000, stop_func=stop_func)
def click_choose():
    driver.find_elements_by_link_text('点击进入')[3].click()

@retry(wait_fixed=2000, stop_func=stop_func)
def click_entry():
    driver.find_element_by_link_text('进入选课>>>>')[0].click()

@retry(wait_fixed=2000, stop_func=stop_func)
def click_filter():
    driver.find_element_by_id('electableLessonList_filter_submit').click()

@retry(wait_fixed=2000, stop_func=stop_func)
def click_op():
    driver.find_element_by_class_name('lessonListOperator').click()

click_edu()
switch_2_new_tag()
click_course()
click_choose()
click_entry()
switch_2_new_tag()

while True:
    try:
        # An exception will occur if user closes the browser
        driver.find_element_by_name('electableLesson.no').send_keys(my_course_id)
    except:
        break

    click_filter()
    click_op()

    al = driver.switch_to.alert
    if al.text == '上限人数已满，请稍后再试':
        al.accept()
        print('Refreshing...')
        driver.refresh()
        continue
    else:
        al.accept()
        print('Success!')
        break