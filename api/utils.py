import requests
import datetime
import json
from pprint import pprint


def find_by_hbl(hbl_no):
    headers = {
        'Origin': 'https://unipass.customs.go.kr',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,da;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.100 Safari/537.36',
        'isAjax': 'true',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://unipass.customs.go.kr/csp/index.do?tgMenuId=MYC_MNU_00000450',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'DNT': '1',
    }

    data = {
        'firstIndex': '0',
        'page': '1',
        'pageIndex': '1',
        'pageSize': '10',
        'pageUnit': '10',
        'recordCountPerPage': '10',
        'qryTp': '2',
        'cargMtNo': '',
        'mblNo': '',
        'hblNo': f'{hbl_no}',
        'blYy': f'{datetime.datetime.today().year}'
    }

    response = requests.post(
        'https://unipass.customs.go.kr'
        '/csp/myc/bsopspptinfo/cscllgstinfo/ImpCargPrgsInfoMtCtr/retrieveImpCargPrgsInfoLst.do',
        headers=headers,
        data=data
    )

    return response.json()['resultList'][0]
