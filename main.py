# import our packages
import requests
from bs4 import BeautifulSoup
from lxml import html

tsla_email = 'braasch.matt@yahoo.com'
tsla_passwd = 'Sandygs97'
order_page = ''

gmail_email = ''
gmail_password = ''

if __name__ == '__main__':
    # define login url
    login_url = "https://auth.tesla.com/oauth2/v1/authorize?client_id=teslaweb&response_type=code&scope=openid%20email%20profile&redirect_uri=https%3A//www.tesla.com/openid-connect/generic&state=2rGU9SNwf_WfsQhCsrpdYFOQmCfWPz2UUVM38Uj1dw4"
    # make session
    with requests.Session() as s:
        # set header get page html
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
        # s.headers = headers
        result = s.get(login_url)
        tree = html.fromstring(result.text)
        # get auth token and trans_id
        auth_token = list(set(tree.xpath("//input[@name='_csrf']/@value")))[0]
        print('auth token: {}'.format(auth_token))
        # send payload we received
        params = (
            ('client_id', 'teslaweb'),
            ('response_type', 'code'),
            ('scope', 'openid email profile'),
            ('redirect_uri', 'https://www.tesla.com/openid-connect/generic'),
            ('state', 'VxKTLWGVmnj36uBk0CimBe8QdxhitlVg3rA2azW1CbA'),
        )
        data = {
            '_csrf': auth_token,
            '_phase': 'authenticate',
            '_process': '1',
            'cancel': '',
            'identity': tsla_email,
            'credential': tsla_passwd
        }

        response = s.post('https://auth.tesla.com/oauth2/v1/authorize', params=params, data=data)
        # get referral code
        # headers = result.headers
        print('after post, getting referral'.format(headers))
        account_url = "https://www.tesla.com/teslaaccount/"
        result = s.get(account_url, headers=headers)
        print('got html for teslaaccount, retrieving referral code.')
        soup = BeautifulSoup(result.content, 'html.parser')
        link_list = [a['href'] for a in soup.find_all('a', href=True)]
        for link in link_list:
            if 'ts.la' in link:
                print(link)

