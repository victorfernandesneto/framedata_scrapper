from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os.path
import psycopg2

conn = psycopg2.connect("dbname=framedata user=postgres password=perfect")
cur = conn.cursor()
sql_tables = """DROP TABLE MOVELIST;
                DROP TABLE CHARACTERS;
                CREATE TABLE CHARACTERS(
                    CHARACTER_NAME VARCHAR(50) PRIMARY KEY
                );
                CREATE TABLE MOVELIST(
                    IDMOVE SERIAL PRIMARY KEY,
                    MOVE_NAME VARCHAR(255),
                    STARTUP VARCHAR(255),
                    ACTIVE VARCHAR(255),
                    RECOVERY_FRAMES VARCHAR(255),
                    OH VARCHAR(255),
                    OB VARCHAR(255),
                    CANCEL VARCHAR(255),
                    DAMAGE VARCHAR(255),
                    SCALING VARCHAR(255),
                    DRIVE_INCREASE VARCHAR(255),
                    DRIVE_DECREASE VARCHAR(255),
                    DRIVE_DECREASE_PC VARCHAR(255),
                    SA_INCREASE VARCHAR(255),
                    HIGH_LOW VARCHAR(255),
                    MISC TEXT,
                    CHARACTER VARCHAR(255),
                    FOREIGN KEY(CHARACTER) REFERENCES CHARACTERS(CHARACTER_NAME)
                );"""
cur.execute(sql_tables)
sql1 = """insert into characters(character_name) values(%s);"""
sql2 = """insert into movelist(move_name, startup, active, recovery_frames, oh, ob, cancel, damage,
                               scaling, drive_increase, drive_decrease, drive_decrease_pc, sa_increase, high_low, 
                               misc, character) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

driver = webdriver.Edge()
driver.get(f"https://www.streetfighter.com/6/character/")
characters_as = driver.find_elements(By.CSS_SELECTOR, ".select_character__select__list__bgBGl > ul > li > a")
characters = {}

for elements in characters_as:
    current_character_url = elements.get_attribute("href")
    current_character_name = os.path.split(current_character_url) # current_character_name[1] é o nome do personagem
    cur.execute(sql1, (current_character_name[1],))
    characters[current_character_name[1]] = current_character_url

for character, url in characters.items():
    driver.get(f"{url}/frame")
    current_character_move_list = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr:not([class])')
    for move in current_character_move_list:
         colunas = move.find_elements(By.TAG_NAME, "td")
         nome_do_move = colunas[0].find_element(By.TAG_NAME, "span").get_attribute("innerText")
         startup = colunas[1].get_attribute("innerText")
         active = colunas[2].get_attribute("innerText")
         recovery = colunas[3].get_attribute("innerText")
         oh = colunas[4].get_attribute("innerText")
         ob = colunas[5].get_attribute("innerText")
         cancel = colunas[6].get_attribute("innerText")
         damage = colunas[7].get_attribute("innerText")
         scaling = colunas[8].get_attribute("innerText") 
         drive_increase = colunas[9].get_attribute("innerText") 
         drive_decrease = colunas[10].get_attribute("innerText") 
         drive_decrease_pc = colunas[11].get_attribute("innerText") 
         sa_increase = colunas[12].get_attribute("innerText") 
         high_low = colunas[13].get_attribute("innerText") 
         misc = colunas[14].get_attribute("innerText")
         cur.execute(sql2, (nome_do_move, startup, active, recovery, oh, ob, cancel, damage, scaling, drive_increase, drive_decrease, drive_decrease_pc, sa_increase, high_low, misc, character))    
conn.commit()
cur.close()
conn.close()