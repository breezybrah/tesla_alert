import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

browser.open("https://www.tesla.com/teslaaccount", headers=headers)

browser.select_form('#form')
browser.get_current_form().print_smmary()