import unittest

import requests

from pytattscom import config
from pytattscom.companies import get_companies, get_company_products


class CompaniesTestCase(unittest.TestCase):
    def test_companies_endpoint(self):
        uri = f'{config.API_BASE}/{config.API_ENDPOINT["companies"]}'
        r = requests.get(uri)
        r.raise_for_status()
        companies_json = r.json()
        self.assertTrue(companies_json.get('Success', False))

        company = next(x for x in companies_json['Companies'] if x['CompanyId'] == 'NSWLotteries')
        self.assertIsNotNone(company)

    def test_get_companies(self):
        companies = get_companies()
        company = next(x for x in companies if getattr(x, 'CompanyId') == 'NSWLotteries')
        self.assertIsNotNone(company)

    def test_get_company_products(self):
        companies = get_company_products()
        company = next(x for x in companies if getattr(x, 'CompanyId') == 'NSWLotteries')
        self.assertIsNotNone(company)

        product = next(x for x in company.Products if getattr(x, 'ProductId') == 'Powerball')
        self.assertIsNotNone(product)


if __name__ == '__main__':
    unittest.main()
