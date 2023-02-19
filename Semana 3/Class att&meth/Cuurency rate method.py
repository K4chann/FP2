"""This module contains the class Currency."""


class Currency:
    """Represents an amount of euros.

    Can give its equivalent value in other currencies
    """

    __exchange_rates = {
        "EUR": 1.0,
        "JPY": 124.83,
        "USD": 1.11918,
        "GBP": 0.85806
    }

    ######################
    # Put your code here #
    ######################

    @classmethod
    def rate(cls, currency):
        """Return currency rate."""
        if currency not in cls.__exchange_rates.keys():
            return None
        return cls.__exchange_rates[currency]

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

    print(Currency.rate("GBP"))
    print(Currency.rate("CAD"))
