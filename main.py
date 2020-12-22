from selenium import webdriver

chromedriver = "P:\PycharmProjects\chromedriver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromedriver)
driver.get("https://www.python.org/")

event_elements = driver.find_elements_by_class_name("event-widget a")
date_elements = driver.find_elements_by_class_name("event-widget time")


event_list = [n.text for n in event_elements[1:]]
date_list = [n.get_attribute("datetime").split("T")[0] for n in date_elements]

if len(event_list) == len(date_list):
    events = list(zip(date_list, event_list))

event_dict_list = []
event_dict = {}

for x, y in events:
    event_dict["time"] = x
    event_dict["name"] = y
    event_dict_list.append(dict(event_dict))

keys = [n for n in range(len(event_dict_list))]

result = dict(zip(keys, event_dict_list))

print(result)

driver.close()