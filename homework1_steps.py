import time
from selenium.webdriver.support.select import Select

from selenium import webdriver

driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(20)

# locators
sign_in_link = "//a[contains(text(),'Sign in')]"
create_email_box = "//input[@id='email_create']"
create_acct_button = "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/button[1]/span[1]"
email = "wwwoww1@email.com"
password = "Maradona10"
mr_button = "//input[@id='id_gender1']"
first_name = "//input[@id='customer_firstname']"
last_name = "//input[@id='customer_lastname']"
email_input = "//input[@id='email']"
password_input = "//input[@id='passwd']"
select_day = "//select[@id='days']"
select_month = "//select[@id='months']"
select_year = "//select[@id='years']"
newsletter_checkbox = "//input[@id='newsletter']"
receive_checkbox = "//input[@id='optin']"
address_firstname = "//input[@id='firstname']"
address_lastname = "//input[@id='lastname']"
company_name = "//input[@id='company']"
address_input = "//input[@id='address1']"
city_input = "//input[@id='city']"
select_state = "//select[@id='id_state']"
zipcode = "//input[@id='postcode']"
select_country = "//select[@id='id_country']"
add_info_text_area = "//textarea[@id='other']"
phone_num = "//input[@id='phone_mobile']"
assign_address = "//input[@id='alias']"
register_button = "//body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div[4]/button[1]/span[1]"
sign_out_button = "//header/div[2]/div[1]/div[1]/nav[1]/div[2]/a[1]"
heading_xpath = "//h1[contains(text(),'My account')]"


url = "http://automationpractice.com/index.php"
driver.get(url)
print(f"opened the browser and website :{url}")
time.sleep(1)

element = driver.find_element_by_xpath(sign_in_link)
print("clicking the element")
element.click()
time.sleep(1)

element = driver.find_element_by_xpath(create_email_box)
print(f"entering the following text :{email}")
element.send_keys(email)
time.sleep(1)

element = driver.find_element_by_xpath(create_acct_button)
print("clicking the element")
element.click()
time.sleep(1)

element = driver.find_element_by_xpath(mr_button)
print("clicking the element")
element.click()
time.sleep(1)

element = driver.find_element_by_xpath(first_name)
print(f"entering the following text : Michael ")
element.send_keys('Michael')
time.sleep(1)

element = driver.find_element_by_xpath(last_name)
print(f"entering the following text : Scofield ")
element.send_keys('Scofield')
time.sleep(1)

element = driver.find_element_by_xpath(email_input)
print(f"entering the following text : {email} ")
element.clear()
element.send_keys(email)
time.sleep(1)

element = driver.find_element_by_xpath(password_input)
print(f"entering the following text : {password} ")
element.clear()
element.send_keys(password)
time.sleep(1)

dd_list = driver.find_element_by_xpath(select_day)
day_selection = Select(dd_list)
# print(f"all options of day : ", day_selection.options)
day_selection.select_by_index(10)
# print(f" option i selected : ", day_selection.all_selected_options)
time.sleep(2)

dd_list = driver.find_element_by_xpath(select_month)
month_selection = Select(dd_list)
# print(f"all options of month : ", month_selection.options)
month_selection.select_by_index(5)
# print(f" option i selected : ", month_selection.all_selected_options)
time.sleep(1)

dd_list = driver.find_element_by_xpath(select_year)
year_selection = Select(dd_list)
# print(f"all options of year : ", year_selection.options)
year_selection.select_by_index(36)
# print(f" option i selected : ", month_selection.all_selected_options)
time.sleep(2)

element = driver.find_element_by_xpath(newsletter_checkbox)
print("clicking the element")
element.click()
time.sleep(1)


element = driver.find_element_by_xpath(receive_checkbox)
print("clicking the element")
element.click()
time.sleep(1)



element = driver.find_element_by_xpath(address_firstname)
print(f"entering the following text : Michael ")
element.clear()
element.send_keys('Michael')
time.sleep(1)


element = driver.find_element_by_xpath(address_lastname)
print(f"entering the following text : Scofield ")
element.clear()
element.send_keys('Scofield')
time.sleep(1)


element = driver.find_element_by_xpath(company_name)
print(f"entering the following text : RSB Group ")
element.clear()
element.send_keys('RSB Group')
time.sleep(1)


element = driver.find_element_by_xpath(address_input)
print(f"entering the following text : 123 abc street ")
element.clear()
element.send_keys('123 abc street')

element = driver.find_element_by_xpath(city_input)
print(f"entering the following text : Las Vegas ")
element.clear()
element.send_keys('Las Vegas')
time.sleep(1)


dd_list = driver.find_element_by_xpath(select_state)
state_selection = Select(dd_list)
# print(f"all options of states : ", state_selection.options)
state_selection.select_by_index(29)
# print(f" option i selected : ", state_selection.all_selected_options)
time.sleep(1)


element = driver.find_element_by_xpath(zipcode)
print(f"entering the following text : 89119 ")
element.clear()
element.send_keys('89119')
time.sleep(1)
#
# dd_list = driver.find_element_by_xpath(select_country)
# usa_selection = Select(dd_list)
# print(f"all options of country : ", usa_selection.options)
# usa_selection.select_by_index(0)
# print(f" option i selected : ", usa_selection.all_selected_options)
#
element = driver.find_element_by_xpath(add_info_text_area)
print(f"entering the following text : Hello World!!! ")
element.clear()
element.send_keys('Hello World!!!')
time.sleep(1)



element = driver.find_element_by_xpath(phone_num)
print(f"entering the following text : 7024097887 ")
element.clear()
element.send_keys('7024097887')
time.sleep(1)


element = driver.find_element_by_xpath(assign_address)
print(f"entering the following text : My address")
element.clear()
element.send_keys('My address')
time.sleep(1)


element = driver.find_element_by_xpath(register_button)
print("clicking the element")
element.click()
time.sleep(4)

url2 = driver.current_url
print(url2)
assert url2 == "http://automationpractice.com/index.php?controller=my-account"


element = driver.find_element_by_xpath(sign_out_button)
print("clicking the element")
element.click()
print("just signed out")
time.sleep(4)

driver.quit()
print("Now closing the browser..")

















