"""____Работа с ожиданиями. Парсинг Интернет банкинг/телеграммбот_____"""

from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from LogPasswd import login, passwd
import time
import telebot


print("Бот активирован!")
bot = telebot.TeleBot("1329901094:AAGWu4A1ICJWYg__gONJXYUcc-2H52uzTBU")
@bot.message_handler(content_types=['text'])
def otvet_bot(message):
	if message.text == "/balans":
		d = {
			"1":"0748", "2":"9592", "3":"9300", "4":"9192", "5":"0664",
			"6":"3582", "7":"7580", "8":"3990", "9":"8071", "10":"5504", "11":"4762",
			"12":"3861", "13":"0974", "14":"2451", "15":"5602", "16":"9018",
			"17":"3326", "18":"5798", "19":"0031", "20":"9474", "21":"0640",
			"22":"2039", "23":"8739","24":"8567", "25":"8381", "26":"7490",
			"27":"7829", "28":"1517", "29":"0259", "30":"2897", "31":"9038",
			"32":"0840", "33":"4218", "34":"5833", "35":"5307", "36":"2904",
			"37":"6315", "38":"4328", "39":"1546","40":"1656"
			}		
		option = wd.ChromeOptions()
		option.headless = True
		driver = wd.Chrome(options=None, executable_path=r"C:\Users\nmedvedev\Desktop\Selenium\chromedriver.exe")
		driver.get("https://ibank.asb.by/wps/portal/ibank/Home/ibLogin/!ut/p/z1/jY_NDoIwEISfhqPugqjorWJUFIKJiWIvpk34i9CSUkz06a16MtHo3nb2m8wsUEiACnYpc6ZLKVhl9iMdnZAsXXsT4zpe7B0kvh3bQ2c_2MVDOPwC6OP8ZQjC-gn4S7Jyx6GRXM_BYD5bzceTCDEYPRo4KvKjHGjDdNErRSYhqWReChNOf9npHwXySvLXr0TwgWeSVJqlKlX9Thm50LpppxZayNOKqa7lTJz7_GrhJ0shWw3JOwlNndzCbLetD157BxXZMwQ!/dz/d5/L2dBISEvZ0FBIS9nQSEh/p0/IZ7_0AG41KO0JGEO20A9V4JL5S0PK7=CZ6_0AG41KO0JOFV20AC1O152V3SO5=LA0=/#Z7_0AG41KO0JGEO20A9V4JL5S0PK7")	
		try:
			wait = WebDriverWait(driver, 10)
			b = wait.until(
				EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/table[1]/tbody/tr/td/div/form/input"))
				)
			c = wait.until(
				EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/table[1]/tbody/tr/td/div/form/div/input"))
				)
		finally:
			b.send_keys(login)
			c.send_keys(passwd)
		try:
			wait = WebDriverWait(driver, 5)
			b = wait.until(
				EC.presence_of_element_located((By.CLASS_NAME, "button"))
				)
		finally:
			b.click()
		b = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[2]/table[1]/tbody/tr/td/div/form/p[1]/span")
		text_b = b.text
		s_text_b = text_b.split(" ")[-1]
		print("Зашли в банк")
		if s_text_b in d:
			b = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[2]/table[1]/tbody/tr/td/div/form/input[2]")
			b.send_keys(d[s_text_b])
		driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[2]/table[1]/tbody/tr/td/div/form/input[5]").click()
		driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/li[3]/a").click()
		driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div/div[1]/table/tbody/tr/td/div/ul/li[1]/a").click()
		result = driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div/div[2]/table/tbody/tr/td/div/form/div/span[2]/table/tbody/tr[1]/td/table[1]/tbody/tr/td[5]/div/nobr")
		bot.send_message(message.chat.id, f"Денег осталось: {result.text} б.р.")
		driver.quit()
	else:
		bot.send_message(message.chat.id, r"/balans")


bot.polling(none_stop=True)