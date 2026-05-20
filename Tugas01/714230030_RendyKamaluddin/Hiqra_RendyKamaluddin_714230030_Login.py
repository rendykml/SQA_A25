from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# =========================
# m ggrr
# =========================

driver = webdriver.Chrome()
driver.maximize_window()

# =========================
# BUKA HALAMAN LOGIN
# =========================

driver.get("https://hiqra.sgp.dom.my.id/admin")

# =========================
# INPUT USERNAME / EMAIL
# =========================

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "email"))
)

username.send_keys("admin@example.com")

# =========================
# INPUT PASSWORD
# =========================

password = driver.find_element(By.NAME, "password")
password.send_keys("password")

# =========================
# KLIK LOGIN
# =========================

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# =========================
# VALIDASI DASHBOARD
# =========================

try:
    WebDriverWait(driver, 10).until(
        EC.url_contains("dashboard")
    )

    print("TEST LOGIN BERHASIL ✅")
    print("Masuk ke dashboard")

except:
    print("TEST LOGIN GAGAL ❌")

time.sleep(5)

driver.quit()