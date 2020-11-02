import requests

from pytattscom import config
from pytattscom.util import RecursiveNamespace


def get_companies():
    uri = f'{config.API_BASE}/{config.API_ENDPOINT["companies"]}'
    r = requests.get(uri)
    r.raise_for_status()
    r_json = r.json()
    assert r_json.get('Success', False) is True

    companies = [RecursiveNamespace(**x) for x in r_json['Companies']]
    return companies


def get_company_products():
    uri = f'{config.API_BASE}/{config.API_ENDPOINT["companyproducts"]}'
    r = requests.get(uri)
    r.raise_for_status()
    r_json = r.json()
    assert r_json.get('Success', False) is True

    company_products = [RecursiveNamespace(**x) for x in r_json['Companies']]
    return company_products
