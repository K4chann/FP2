"""This module contains the class Currency."""


class Currency:
    """Represents an amount of euros.

    Can give its equivalent value in other currencies
    """

    ######################
    # Put your code here #
    ######################

    exchange_rates = {
        "EUR": 1.0,
        "JPY": 124.83,
        "USD": 1.11918,
        "GBP": 0.85806
    }

    def __init__(self, value=0):
        """Initialize with value (an amount of euros)."""
        self.value = value

    @property
    def value(self):
        """Return value in euros."""
        return self.__value

    @value.setter
    def value(self, value):
        """Actualize value of euros."""
        self.__value = value

    def convert_to(self, currency):
        """Return the equivalent value of self in another currency.

        currency: currency to convert to
        """
        if currency in Currency.exchange_rates:
            return self.value * Currency.exchange_rates[currency]
        else:
            return None


if __name__ == "__main__":
    # Example of use (not part of the solution)
    c = Currency(10)
    print(c.convert_to("USD"))
    print(c.convert_to("NSN"))
