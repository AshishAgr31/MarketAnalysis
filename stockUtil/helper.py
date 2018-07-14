import urllib2

import bs4

from stockUtil.models import Company


def get_link_fileptr(url):
    """
    For fetching content from a url.
    """
    # connectTor() select connection from either proxy or tor/without proxy = urllib2.ProxyHandler( { 'http' :
    # 'http://Username:Password@ProxyServer:Port' , 'https' : 'https://Username:Password@ProxyServer:Port' })
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(auth, urllib2.HTTPHandler)
    # select this opener when using tor/no proxy.
    # opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler )
    # select this opener when using proxy.
    urllib2.install_opener(opener)
    try:
        link_file = urllib2.urlopen(url)
    except urllib2.URLError:
        return get_link_fileptr(url)  # if any error occurs, then fetch again.
    else:
        return link_file  # Success


def get_data(url):
    fileptr = get_link_fileptr(url)
    data = fileptr.read()
    soup = bs4.BeautifulSoup(data, "html.parser")
    return soup


def get_all_company_name():
    company_list_url = "https://www.moneycontrol.com/india/stockpricequote/"
    alpha_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z", "Others"]
    for alphabet in alpha_list:
        url = company_list_url + alphabet
        soup = get_data(url)
        tds = soup.find_all('td')
        for td in tds:
            a = td.find('a')
            if a is not None:
                url_parameter = a.get('href').split("/")[7]
                name = a.text
                comp = Company(name=name, url_id=url_parameter)
                comp.save()
