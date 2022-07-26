# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AppsPosBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'app_name': 'str',
        'title': 'str',
        'description': 'str',
        'template': 'str',
        'default_view': 'str',
        'currency': 'str',
        'show_custom_amount': 'bool',
        'show_discount': 'bool',
        'enable_tips': 'bool',
        'custom_amount_pay_button_text': 'str',
        'fixed_amount_pay_button_text': 'str',
        'tip_text': 'str',
        'custom_css_link': 'str',
        'embedded_css': 'str',
        'notification_url': 'str',
        'redirect_url': 'str',
        'redirect_automatically': 'bool',
        'requires_refund_email': 'bool'
    }

    attribute_map = {
        'app_name': 'appName',
        'title': 'title',
        'description': 'description',
        'template': 'template',
        'default_view': 'defaultView',
        'currency': 'currency',
        'show_custom_amount': 'showCustomAmount',
        'show_discount': 'showDiscount',
        'enable_tips': 'enableTips',
        'custom_amount_pay_button_text': 'customAmountPayButtonText',
        'fixed_amount_pay_button_text': 'fixedAmountPayButtonText',
        'tip_text': 'tipText',
        'custom_css_link': 'customCSSLink',
        'embedded_css': 'embeddedCSS',
        'notification_url': 'notificationUrl',
        'redirect_url': 'redirectUrl',
        'redirect_automatically': 'redirectAutomatically',
        'requires_refund_email': 'requiresRefundEmail'
    }

    def __init__(self, app_name=None, title=None, description=None, template=None, default_view=None, currency=None, show_custom_amount=True, show_discount=True, enable_tips=True, custom_amount_pay_button_text='Pay', fixed_amount_pay_button_text='Buy for {PRICE_HERE}', tip_text='Do you want to leave a tip?', custom_css_link=None, embedded_css=None, notification_url=None, redirect_url=None, redirect_automatically=None, requires_refund_email=None):  # noqa: E501
        """AppsPosBody - a model defined in Swagger"""  # noqa: E501
        self._app_name = None
        self._title = None
        self._description = None
        self._template = None
        self._default_view = None
        self._currency = None
        self._show_custom_amount = None
        self._show_discount = None
        self._enable_tips = None
        self._custom_amount_pay_button_text = None
        self._fixed_amount_pay_button_text = None
        self._tip_text = None
        self._custom_css_link = None
        self._embedded_css = None
        self._notification_url = None
        self._redirect_url = None
        self._redirect_automatically = None
        self._requires_refund_email = None
        self.discriminator = None
        if app_name is not None:
            self.app_name = app_name
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if template is not None:
            self.template = template
        if default_view is not None:
            self.default_view = default_view
        if currency is not None:
            self.currency = currency
        if show_custom_amount is not None:
            self.show_custom_amount = show_custom_amount
        if show_discount is not None:
            self.show_discount = show_discount
        if enable_tips is not None:
            self.enable_tips = enable_tips
        if custom_amount_pay_button_text is not None:
            self.custom_amount_pay_button_text = custom_amount_pay_button_text
        if fixed_amount_pay_button_text is not None:
            self.fixed_amount_pay_button_text = fixed_amount_pay_button_text
        if tip_text is not None:
            self.tip_text = tip_text
        if custom_css_link is not None:
            self.custom_css_link = custom_css_link
        if embedded_css is not None:
            self.embedded_css = embedded_css
        if notification_url is not None:
            self.notification_url = notification_url
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if redirect_automatically is not None:
            self.redirect_automatically = redirect_automatically
        if requires_refund_email is not None:
            self.requires_refund_email = requires_refund_email

    @property
    def app_name(self):
        """Gets the app_name of this AppsPosBody.  # noqa: E501

        The name of the app (shown in admin UI)  # noqa: E501

        :return: The app_name of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppsPosBody.

        The name of the app (shown in admin UI)  # noqa: E501

        :param app_name: The app_name of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._app_name = app_name

    @property
    def title(self):
        """Gets the title of this AppsPosBody.  # noqa: E501

        The title of the app (shown to the user)  # noqa: E501

        :return: The title of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AppsPosBody.

        The title of the app (shown to the user)  # noqa: E501

        :param title: The title of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this AppsPosBody.  # noqa: E501

        The description of the app  # noqa: E501

        :return: The description of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppsPosBody.

        The description of the app  # noqa: E501

        :param description: The description of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def template(self):
        """Gets the template of this AppsPosBody.  # noqa: E501

        Template for items available in the app  # noqa: E501

        :return: The template of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this AppsPosBody.

        Template for items available in the app  # noqa: E501

        :param template: The template of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def default_view(self):
        """Gets the default_view of this AppsPosBody.  # noqa: E501

        Template for items available in the app  # noqa: E501

        :return: The default_view of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._default_view

    @default_view.setter
    def default_view(self, default_view):
        """Sets the default_view of this AppsPosBody.

        Template for items available in the app  # noqa: E501

        :param default_view: The default_view of this AppsPosBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["Static", "Cart", "Light", "Print"]  # noqa: E501
        if default_view not in allowed_values:
            raise ValueError(
                "Invalid value for `default_view` ({0}), must be one of {1}"  # noqa: E501
                .format(default_view, allowed_values)
            )

        self._default_view = default_view

    @property
    def currency(self):
        """Gets the currency of this AppsPosBody.  # noqa: E501

        Currency to use for the app. Defaults to the currency used by the store if not specified  # noqa: E501

        :return: The currency of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AppsPosBody.

        Currency to use for the app. Defaults to the currency used by the store if not specified  # noqa: E501

        :param currency: The currency of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def show_custom_amount(self):
        """Gets the show_custom_amount of this AppsPosBody.  # noqa: E501

        Whether to include a special item in the store which allows user to input a custom payment amount  # noqa: E501

        :return: The show_custom_amount of this AppsPosBody.  # noqa: E501
        :rtype: bool
        """
        return self._show_custom_amount

    @show_custom_amount.setter
    def show_custom_amount(self, show_custom_amount):
        """Sets the show_custom_amount of this AppsPosBody.

        Whether to include a special item in the store which allows user to input a custom payment amount  # noqa: E501

        :param show_custom_amount: The show_custom_amount of this AppsPosBody.  # noqa: E501
        :type: bool
        """

        self._show_custom_amount = show_custom_amount

    @property
    def show_discount(self):
        """Gets the show_discount of this AppsPosBody.  # noqa: E501

        Whether to allow user to input a discount amount. Applies to Cart view only. Not recommended for customer self-checkout  # noqa: E501

        :return: The show_discount of this AppsPosBody.  # noqa: E501
        :rtype: bool
        """
        return self._show_discount

    @show_discount.setter
    def show_discount(self, show_discount):
        """Sets the show_discount of this AppsPosBody.

        Whether to allow user to input a discount amount. Applies to Cart view only. Not recommended for customer self-checkout  # noqa: E501

        :param show_discount: The show_discount of this AppsPosBody.  # noqa: E501
        :type: bool
        """

        self._show_discount = show_discount

    @property
    def enable_tips(self):
        """Gets the enable_tips of this AppsPosBody.  # noqa: E501

        Whether to allow user to input a tip amount. Applies to Cart and Light views only  # noqa: E501

        :return: The enable_tips of this AppsPosBody.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tips

    @enable_tips.setter
    def enable_tips(self, enable_tips):
        """Sets the enable_tips of this AppsPosBody.

        Whether to allow user to input a tip amount. Applies to Cart and Light views only  # noqa: E501

        :param enable_tips: The enable_tips of this AppsPosBody.  # noqa: E501
        :type: bool
        """

        self._enable_tips = enable_tips

    @property
    def custom_amount_pay_button_text(self):
        """Gets the custom_amount_pay_button_text of this AppsPosBody.  # noqa: E501

        Payment button text which appears for items which allow user to input a custom amount  # noqa: E501

        :return: The custom_amount_pay_button_text of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._custom_amount_pay_button_text

    @custom_amount_pay_button_text.setter
    def custom_amount_pay_button_text(self, custom_amount_pay_button_text):
        """Sets the custom_amount_pay_button_text of this AppsPosBody.

        Payment button text which appears for items which allow user to input a custom amount  # noqa: E501

        :param custom_amount_pay_button_text: The custom_amount_pay_button_text of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._custom_amount_pay_button_text = custom_amount_pay_button_text

    @property
    def fixed_amount_pay_button_text(self):
        """Gets the fixed_amount_pay_button_text of this AppsPosBody.  # noqa: E501

        Payment button text which appears for items which have a fixed price  # noqa: E501

        :return: The fixed_amount_pay_button_text of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._fixed_amount_pay_button_text

    @fixed_amount_pay_button_text.setter
    def fixed_amount_pay_button_text(self, fixed_amount_pay_button_text):
        """Sets the fixed_amount_pay_button_text of this AppsPosBody.

        Payment button text which appears for items which have a fixed price  # noqa: E501

        :param fixed_amount_pay_button_text: The fixed_amount_pay_button_text of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._fixed_amount_pay_button_text = fixed_amount_pay_button_text

    @property
    def tip_text(self):
        """Gets the tip_text of this AppsPosBody.  # noqa: E501

        Prompt which appears next to the tip amount field if tipping is enabled  # noqa: E501

        :return: The tip_text of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._tip_text

    @tip_text.setter
    def tip_text(self, tip_text):
        """Sets the tip_text of this AppsPosBody.

        Prompt which appears next to the tip amount field if tipping is enabled  # noqa: E501

        :param tip_text: The tip_text of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._tip_text = tip_text

    @property
    def custom_css_link(self):
        """Gets the custom_css_link of this AppsPosBody.  # noqa: E501

        Link to a custom CSS stylesheet to be used in the app  # noqa: E501

        :return: The custom_css_link of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._custom_css_link

    @custom_css_link.setter
    def custom_css_link(self, custom_css_link):
        """Sets the custom_css_link of this AppsPosBody.

        Link to a custom CSS stylesheet to be used in the app  # noqa: E501

        :param custom_css_link: The custom_css_link of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._custom_css_link = custom_css_link

    @property
    def embedded_css(self):
        """Gets the embedded_css of this AppsPosBody.  # noqa: E501

        Custom CSS to embed into the app  # noqa: E501

        :return: The embedded_css of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._embedded_css

    @embedded_css.setter
    def embedded_css(self, embedded_css):
        """Sets the embedded_css of this AppsPosBody.

        Custom CSS to embed into the app  # noqa: E501

        :param embedded_css: The embedded_css of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._embedded_css = embedded_css

    @property
    def notification_url(self):
        """Gets the notification_url of this AppsPosBody.  # noqa: E501

        Callback notification url to POST to once when invoice is paid for and once when there are enough blockchain confirmations  # noqa: E501

        :return: The notification_url of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._notification_url

    @notification_url.setter
    def notification_url(self, notification_url):
        """Sets the notification_url of this AppsPosBody.

        Callback notification url to POST to once when invoice is paid for and once when there are enough blockchain confirmations  # noqa: E501

        :param notification_url: The notification_url of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._notification_url = notification_url

    @property
    def redirect_url(self):
        """Gets the redirect_url of this AppsPosBody.  # noqa: E501

        URL to redirect user to once invoice is paid  # noqa: E501

        :return: The redirect_url of this AppsPosBody.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this AppsPosBody.

        URL to redirect user to once invoice is paid  # noqa: E501

        :param redirect_url: The redirect_url of this AppsPosBody.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def redirect_automatically(self):
        """Gets the redirect_automatically of this AppsPosBody.  # noqa: E501

        Whether to redirect user to redirect URL automatically once invoice is paid. Defaults to what is set in the store settings  # noqa: E501

        :return: The redirect_automatically of this AppsPosBody.  # noqa: E501
        :rtype: bool
        """
        return self._redirect_automatically

    @redirect_automatically.setter
    def redirect_automatically(self, redirect_automatically):
        """Sets the redirect_automatically of this AppsPosBody.

        Whether to redirect user to redirect URL automatically once invoice is paid. Defaults to what is set in the store settings  # noqa: E501

        :param redirect_automatically: The redirect_automatically of this AppsPosBody.  # noqa: E501
        :type: bool
        """

        self._redirect_automatically = redirect_automatically

    @property
    def requires_refund_email(self):
        """Gets the requires_refund_email of this AppsPosBody.  # noqa: E501

        Whether to redirect user to redirect URL automatically once invoice is paid. Defaults to what is set in the store settings  # noqa: E501

        :return: The requires_refund_email of this AppsPosBody.  # noqa: E501
        :rtype: bool
        """
        return self._requires_refund_email

    @requires_refund_email.setter
    def requires_refund_email(self, requires_refund_email):
        """Sets the requires_refund_email of this AppsPosBody.

        Whether to redirect user to redirect URL automatically once invoice is paid. Defaults to what is set in the store settings  # noqa: E501

        :param requires_refund_email: The requires_refund_email of this AppsPosBody.  # noqa: E501
        :type: bool
        """

        self._requires_refund_email = requires_refund_email

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AppsPosBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AppsPosBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
