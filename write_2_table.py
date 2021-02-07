import pandas as pd 
from common_utils.sql_functions import write2table
import configparser

#读取ini配置
cfparser = configparser.ConfigParser()
cfparser.read('mysql_connection_config.ini',encoding="utf-8")

config_sections = cfparser.sections()

host = cfparser.get('connection','host')
port = cfparser.get('connection','port')
database = cfparser.get('connection','database')
charset = cfparser.get('connection','charset')
username = cfparser.get('connection','username')
password = cfparser.get('connection','password')

#读取每次超过50W行就保存到另一个XLSX文档
seperate_batch = 500000

engine_text = f'mysql://{username}:{password}@{host}:{port}/{database}?charset={charset}'

file_path = r"D:\My Documents\Documents\vchat\NewChatFiles\calc_amount(India) - day calculations-2021.01.15-2021.01.17.xlsx"

data = pd.read_excel(file_path)

write2table(engine_text, data, 'warning_test',how='normal')