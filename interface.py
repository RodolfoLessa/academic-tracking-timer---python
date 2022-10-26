import pandas as pd
from gooey import Gooey, GooeyParser
import numpy as np
from random import randint


@Gooey(program_name="Divisão de tempo do Universitário",
       default_size=(710, 700),
       navigation='TABBED', header_bg_color='#FF0000',
       body_bg_color='#FFF900')
def parse_args():
    parser = GooeyParser()
    price_group = parser.add_argument_group('Price')
    price_group.add_argument("prices",
                             metavar='How fancy are we feeling today?',
                             action='store',
                             choices=['$', '$$', '$$$', '$$$$', 'surprise me'],
                             default='$')
    postcode_group = parser.add_argument_group('Postcode')
    postcode_group.add_argument('postcode',
                                metavar='What is your postcode?',
                                action='store',
                                help="6 digit postcode",
                                gooey_options={
                                    'validator': {
                                        'test': 'len(user_input) == 6',
                                        'message': '6 digit postcode!'
                                    }
                                })
    args = parser.parse_args()
    return args


def match_postcode(postcode, df):
    df.zipcode = df.zipcode.str.replace("\s", "")
    restaurants = df[df['zipcode'] == postcode]
    return restaurants


def match_price(prices, restaurants):
    if prices == 'surprise me':
        price_len = randint(1, 4)
    else:
        price_len = len(prices)
    print(price_len)
    restaurants['length'] = restaurants['prices'].str.len()
    restaurants = restaurants[restaurants['length'] == str(price_len)]
    return restaurants

# def show_recommendations(message):
#    app = wx.App()
#    dlg = wx.MessageDialog(None, message, 'What about this one?', wx.ICON_INFORMATION)
#    dlg.ShowModal()

# def show_error_message(message):
#    app = wx.App()
#    dlg = wx.MessageDialog(None, message, 'Whoops', wx.ICON_INFORMATION)
#    dlg.ShowModal()


if __name__ == '__main__':
    args = parse_args()
    prices = args.prices
    postcode = args.postcode

    df = pd.read_excel("yelp-ams.xlsx")
    df2 = match_postcode(postcode, df)
    df3 = match_price(prices, df2)
