from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# 定数
url = 'https://forms.office.com/Pages/YOUR_FORMS_URL'
email = "your_email@outlook.com"
password = "Y0ur_pA4s5w0rd"

# ブラウザを立ち上げないようにオプションを指定
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# ブラウザを生成
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
browser.get(url)
print("アクセス成功")
sleep(5)

# メールを入力
browser.find_element_by_id('i0116').send_keys(email)
browser.find_element_by_id('idSIButton9').click()
print("メールを入力した")
sleep(1.5)

# パスワードを入力
browser.find_element_by_id('i0118').send_keys(password)
browser.find_element_by_id('idSIButton9').click()
print("パスワードを入力した")
sleep(1.5)


# サインインの状態を維持するかで「はい」を選択
browser.find_element_by_id('KmsiCheckboxField').click()
browser.find_element_by_id('idSIButton9').click()
print("サインインを維持するか聞かれたのでチェックして「はい」を押した")
sleep(2)


# 体温を選択
browser.find_elements_by_xpath('//input[@value="36.0〜36.9"]')[0].click()
print("体温を選択した")

# 送信
browser.find_element_by_class_name("__submit-button__").click()
print("送信した")
sleep(2)

# 最終的なhtmlを取得
print(browser.find_element_by_class_name("thank-you-page-comfirm-text").text)

# 閉じる
browser.quit()
