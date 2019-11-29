from selenium import webdriver
import pyautogui, time


chrome_browser = webdriver.Chrome('C:/Users/anthony.ime/Documents/python/projects/sys_buddy2/chromedriver.exe')

chrome_browser.get('https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den_US&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&urp=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
chrome_browser.maximize_window()
assert 'Google Drive: Sign-in' in chrome_browser.title
next_button = chrome_browser.find_elements_by_id('identifierNext')

user_message = chrome_browser.find_element_by_id('identifierId')
user_message.clear()
user_message.send_keys('tooneynta92@gmail.com')
pyautogui.click(933, 680)
time.sleep(5)
password_input = chrome_browser.find_elements_by_name('password')
password_input.clear()
pyautogui.click(630, 507)
time.sleep(0.5)
pyautogui.typewrite('TONDENVIC929499!', interval=0.25)
time.sleep(2)
pyautogui.click(940, 585)
time.sleep(29)
pyautogui.click(313, 187)
pyautogui.typewrite('Work_Force_Attendance (9) (1)', interval=0.18)
pyautogui.click(283, 184)
time.sleep(6)
pyautogui.rightClick(330, 328)
time.sleep(4)
pyautogui.click(564, 745)
