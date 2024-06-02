from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import random
import time


# Configuração de constantes
URL = 'https://www.saucedemo.com/'
CSV_FILE = 'login.csv'
XPATH_ITEMS = [
    '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]', 
    '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]', 
    '//*[@id="add-to-cart-sauce-labs-bike-light"]'
]

def open_browser():
    """Inicializa o navegador e acessa a URL definida."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(URL)
    time.sleep(2)  # Espera a página carregar
    return driver
        
def read_csv(file_path):
    """Lê dados de login de um arquivo CSV."""
    users, passwords = [], []
    current_section = None
    
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                if row == ['Usernames:']:
                    current_section = 'users'
                elif row == ['Password:']:
                    current_section = 'passwords'
                elif current_section == 'users':
                    users.append(row[0])
                elif current_section == 'passwords':
                    passwords.append(row[0])
    
    # Filtrando usuários que deram erros após testes
    users = [user for i, user in enumerate(users) if i not in [1, 1, 2]]
    return users, passwords

def login(driver, username, password):
    """Realiza login no site."""
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def add_items_to_cart(driver):
    """Adiciona itens ao carrinho."""
    for xpath in XPATH_ITEMS:
        driver.find_element(By.XPATH, xpath).click()
    time.sleep(3)  # Espera para garantir que os itens sejam adicionados

def checkout(driver, username):
    """Finaliza a compra."""
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)  # Tempo para visualizar o carrinho
    
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    
    first_name, last_name = username.split('_')
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys(first_name)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys(last_name)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys(random.randint(10000000, 99999999))
    time.sleep(2)
    
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    total_value_element = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')
    total_value = total_value_element.text.split('$')[-1]
    
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(1)
    
    print(f'Compra finalizada com sucesso! Valor total: ${total_value}')


def main():
    driver = open_browser()
    users, passwords = read_csv(CSV_FILE)
    random_user = random.choice(users)
    login(driver, random_user, passwords[0])
    add_items_to_cart(driver)
    checkout(driver, random_user)

if __name__ == '__main__':
    main()
