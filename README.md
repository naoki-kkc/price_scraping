# price_scraping

T/Oな機能しかないです。

## version

- Python 3.9.1 +

## 準備

Chrome Driverを使います。  
お使いのChromeのバージョンに合わせたChrome Driverを[こちらからダウンロード](https://sites.google.com/chromium.org/driver/home)してください。

また、venvで仮想環境を作成し、pipを使用してrequirements.txtの内容をインストールしてください。

## 使用方法

実行にはURLとXPathが必要です。  
XPathはChrome Dev Toolあたりで取得してください。  

例えば以下のようなドライバーを書いてください。

```
import price_scraping

def main():

    target_url   = 'https://exemple.jp/detail/XXXXXXXX'
    target_xpath = '//*[@id="mainContent"]/div[4]/div/li[3]/dl/dd/p[3]/span[2]/span[1]'

    retval = price_scraping.exec(target_url, target_xpath)

    print(retval)

if __name__ == '__main__':
    main()
```