# Auto-Kennon
名前の通り自動で~~検温~~Formを入力して送信してくれるやつです。

# Requirements
`Python3` が必要になります。また、ライブラリのインストールには、
```bash
pip3 install -r requirements.txt
```
これで `selenium` と `webdriver-manager` がインストールされます(多分)

## Usage
使い方は `main.py` の `url` 、`email` 、`password` を自分のものに置き換えてから `python3 main.py` を実行してください。
置き換え後の `main.py` はこんな感じになります.
```python3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# 定数
url = 'https://forms.office.com/pages/responsepage.aspx?id=MpF9OVdNt0WJIllNfjY_6zTBuuV3eP9JoYM4l7ExYyJUQTBZMVU4T0U4TkpXSkVOWUVUS1ZaWEpRNC4u'
email = "tanaka_tarou@outlook.jp"
password = "password"

~~~後略~~~
```

実行後はこのように出力されれば成功となります。
```bash
====== WebDriver manager ======
Current google-chrome version is 92.0.4515
Get LATEST driver version for 92.0.4515
Driver [/Users/username/.wdm/drivers/chromedriver/mac64/92.0.4515.107/chromedriver] found in cache
main.py:15: DeprecationWarning: use options instead of chrome_options
  browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
アクセス成功
メールを入力した
パスワードを入力した
サインインを維持するか聞かれたのでチェックして「はい」を押した
体温を選択した
送信した
Thanks!
```

`Thanks!` の部分にはFormを送信後に表示される画面のメッセージが出ます。Formや環境によっては `Thanks!` ではない場合もあります。

## なんか動かねえんだけど
エラーが出てるっぽいならエラーメッセージをそのままコピペしてググると解決策が出ます。
大体はChromeのバージョンの差異によるエラーだと思いますがググってください。

# 参考文献
- [pythonを使ってMicrosoft Formsを自動送信する方法(Mac版)](
https://qiita.com/kataoka_ys/items/43c20f912178e796a838)
- [【Selenium】ChromeDriverを自動更新するPythonライブラリが便利](https://yuki.world/python-selenium-chromedriver-auto-update/#t_webdriver_managerdriver)
