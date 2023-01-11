from selenium import webdriver
from pandas import DataFrame
from time import sleep


def open_navegador(url):
    path_geckodriver = "geckodriver" #caminho do seu geckodriver
    driver = webdriver.Firefox(executable_path=path_geckodriver)
    driver.get(url)
    return driver


def get_data_page(url, num_break):
    driver = open_navegador(url)
    tb_main = driver.find_element_by_id('example')
    xpath_tr = "//tbody/tr"
    tr = tb_main.find_elements_by_xpath(xpath_tr)
    count = 1
    dic_data_country = {"Country": [], "Internet_users": []}
    for i in tr:
        count = count + 1
        xpath_td = "//tbody/tr[{}]/td[{}]"
        td_country = tb_main.find_element_by_xpath(xpath_td.format(count, 2)).text
        td_internet_users = tb_main.find_element_by_xpath(xpath_td.format(count, 3)).text
        dic_data_country["Country"].append(td_country)
        dic_data_country["Internet_users"].append(td_internet_users)
        if count == num_break+1:
            break
    sleep(5)
    driver.close()
    return dic_data_country


def create_file_csv(file_name, dic_data_country):
    my_dataframe = DataFrame(dic_data_country)
    my_dataframe.to_csv(file_name)


url = "https://www.internetlivestats.com/internet-users-by-country/"
num_break = 100
path = "/pasta/" #Alterar para o caminho da pasta que deseja salvar o excel
file_name = "Internet_users_2016.csv"
path_file_name = path.format(file_name)
my_data_out = get_data_page(url, num_break)
create_file_csv(path_file_name, my_data_out)
