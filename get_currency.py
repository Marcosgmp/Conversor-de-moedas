import xmltodict

def currency_name():
    with open("coin.xml", "rb") as currency_files:
        dic_currency = xmltodict.parse(currency_files)

    currency = dic_currency["xml"]
    return currency


def conv_name():
    with open("conversions.xml", "rb") as conv_files:
        dic_conv = xmltodict.parse(conv_files)

    conversions = dic_conv["xml"]
    dic_conv_available = {}
    for fr_conversion in conversions:
        source_currency, destination_currency = fr_conversion.split("-")
        if source_currency in dic_conv_available:
            dic_conv_available[source_currency].append(destination_currency)
        else:
            dic_conv_available[source_currency] = [destination_currency]
    return dic_conv_available
    