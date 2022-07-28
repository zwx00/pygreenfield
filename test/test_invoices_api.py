# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pygreenfield
from pygreenfield.api.invoices_api import InvoicesApi  # noqa: E501
from pygreenfield.rest import ApiException


class TestInvoicesApi(unittest.TestCase):
    """InvoicesApi unit test stubs"""

    def setUp(self):
        self.api = InvoicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_invoices_activate_payment_method(self):
        """Test case for invoices_activate_payment_method

        Activate Payment Method  # noqa: E501
        """
        pass

    def test_invoices_archive_invoice(self):
        """Test case for invoices_archive_invoice

        Archive invoice  # noqa: E501
        """
        pass

    def test_invoices_create_invoice(self):
        """Test case for invoices_create_invoice

        Create a new invoice  # noqa: E501
        """
        pass

    def test_invoices_get_invoice(self):
        """Test case for invoices_get_invoice

        Get invoice  # noqa: E501
        """
        pass

    def test_invoices_get_invoice_payment_methods(self):
        """Test case for invoices_get_invoice_payment_methods

        Get invoice payment methods  # noqa: E501
        """
        pass

    def test_invoices_get_invoices(self):
        """Test case for invoices_get_invoices

        Get invoices  # noqa: E501
        """
        pass

    def test_invoices_mark_invoice_status(self):
        """Test case for invoices_mark_invoice_status

        Mark invoice status  # noqa: E501
        """
        pass

    def test_invoices_unarchive_invoice(self):
        """Test case for invoices_unarchive_invoice

        Unarchive invoice  # noqa: E501
        """
        pass

    def test_invoices_update_invoice(self):
        """Test case for invoices_update_invoice

        Update invoice  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
