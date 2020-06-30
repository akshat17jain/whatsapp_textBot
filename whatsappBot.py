from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("enter name or group: ")
msg = input("enter message: ")
count = int(input("enter count: "))

input("enter QR code and pess any key ")

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]") 


for index in range(count):
	msg_box.send_keys(msg)
	driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print("SUCCESS")
