import requests as rq
import time
import sys
import logging


def main():
    headers = {
        'authority': 'grants.myrosmol.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer tLerzYsmt1ypKQnEzOhDzCAovfviQ--y',
        'referer': 'https://grants.myrosmol.ru/events',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    resp = rq.get('https://grants.myrosmol.ru/api/events?my=&page=1&per-page=12', headers=headers)
    items = resp.json()
    processed_items = []
    for item in items:
        d = {
            'id': item['ID'],
            'name': item['name'],
            "organizerName": item["organizerName"],
            'region': item['regions'][0]['name'],
            'eventType': item['eventType']['name'],
            'ageFrom': item['eventAccess']['ageFrom'],
            'ageTo': item['eventAccess']['ageTo'],
            'beginsAt': item['beginsAt'],
            'endsAt': item['endsAt'],
            'registrationBeginsAt': item['registrationBeginsAt'],
            'registrationEndsAt': item['registrationEndsAt'],
            'url': "https://grants.myrosmol.ru/events/" + item['ID']
        }
        try:
            item['maxAmount'] = item.get['grants'][0]['maxAmount']
        except:
            item['maxAmount'] = None
        try:
            item['minAmount'] = item.get['grants'][0]['minAmount']
        except:
            item['minAmount'] = None
        processed_items.append(d)
    # POST REQUESTS TO MAXIM_SERVICE
    logging.warning(sys.argv)
    logging.warning(f'{sys.argv[1]}:{sys.argv[2]}/postEvent')
    rq.post(f'{sys.argv[1]}:{sys.argv[2]}/postEvent', data={'items': processed_items})


if __name__ == '__main__':
    logging.warning("START")
    while True:
        try:
            main()
        except Exception as e:
            logging.warning(e)
            pass
        time.sleep(60)
