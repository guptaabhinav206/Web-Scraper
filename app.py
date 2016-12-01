import json
from lxml import html
import requests
import traceback
import re

url = 'http://www.shopclues.com/computers/desktops-and-monitors/monitors.html'
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}


def product_parser(s):

    page = requests.get(s[0], headers=headers)
    try:
        doc = html.fromstring(page.content)

        # Fetching product attributes
        prod_name = doc.xpath("//h1[@itemprop='name']//text()")[0]

        prod_id = re.findall('(\.*Product ID : \d*)', page.content)[0].split(" ")[3]

        category = doc.xpath("//span[@itemprop='title']//text()")[3]

        prod_thumbnail = doc.xpath("//img[@title='%s']/@src2" %prod_name)[0]

        prod_price = doc.xpath("//meta[@itemprop='price']/@content")[0]

        prod_discount = doc.xpath("//span[@class='you-save']//text()")

        # product with no discount
        if not prod_discount:
            prod_discount = 0
        else:
            prod_discount = prod_discount[0]

        # product json structure
        data = {
            'NAME': prod_name,
            'PRODUCT_ID': prod_id,
            'CATEGORY': category,
            'THUMBNAIL': prod_thumbnail,
            'SELLING_PRICE': prod_price,
            'DISCOUNT': prod_discount,
            'AVAILABILITY': [],
            'URL': s[0],
            'EST DELIVERY': {}
        }

        # Pin codes list (can be extended more)
        pin_codes = [560070, 575001, 671551]

        # Get request to the ajax call for getting product availability at the input pin codes
        for code in pin_codes:
            response = requests.get('http://www.shopclues.com/nss.php?pincode_no='+str(code)+'&product_ids='+str(prod_id))
            if response.status_code == 200:
                json_data = json.loads(response.content)
                # Product availability is 1 if found else 0
                if 'pin_result' in json_data:
                    if json_data['pin_result'] != -1 or json_data['pin_result'] != 0:
                        data['EST DELIVERY'].update({code: [json_data['sdate'], json_data['fdate']]})
                        data['AVAILABILITY'].append((code, 1))
                    else:
                        data['EST DELIVERY'].update({code: []})
                        data['AVAILABILITY'].append((code, 0))
                else:
                    raise KeyError
            else:
                raise requests.ConnectionError("Expected status code 200, but got {}".format(response.status_code))

        return data

    except Exception as e:
        traceback.print_exc(e)


def extract_urls():

    page = requests.get(url, headers=headers)
    # Contains source of the given url.
    text_file = open("Output.txt", "w")
    text_file.write(page.content)
    a = []
    # Regex for fetching first 10 product urls
    r = re.compile('(?<=href=").*?(?=")(?=.*class="name")')
    f = open('Output.txt', 'r')
    count = 1
    for lines in f:
        if len(r.findall(lines)) > 0:
            if count <= 10:
                a.append(r.findall(lines))
                count += 1
            else:
                break

    data = {
        'url': a
    }

    # file with the url json
    f1 = open('urls.json', 'w')
    # file with the product json
    f2 = open('products.json', 'w')
    json.dump(data, f1, indent=4)
    res = []
    for item in a:
        res.append(product_parser(item))

    json.dump(res, f2, indent=4)


if __name__ == "__main__":
    extract_urls()
