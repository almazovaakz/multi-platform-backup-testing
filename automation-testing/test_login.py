import tempfile, shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 


tmp_profile = tempfile.mkdtemp()
opts = Options()
opts.add_argument(f'--user-data-dir={tmp_profile}')
opts.add_argument('--headless=new')
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

try:
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    assert "You logged into a secure area!" in driver.page_source
finally:
    driver.quit()
    shutil.rmtree(tmp_profile, ignore_errors=True)
