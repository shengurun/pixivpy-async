#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pixivpy_async import *
from datetime import *

# change _USERNAME,_PASSWORD first!
_USERNAME = "userbay"
_PASSWORD = "userpay"


def main():
    aapi = AppPixivAPI()
    # aapi.set_additional_headers({'Accept-Language':'en-US'})
    aapi.set_accept_language('en-us') # zh-cn

    aapi.login(_USERNAME, _PASSWORD)
    json_result = aapi.illust_ranking('day', date=(datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'))

    print("Printing image titles and tags with English tag translations present when available")

    for illust in json_result.illusts[:3]:
        print("Illustration: \"" + str(illust.title) + "\"\nTags: " + str(illust.tags) + "\n")




if __name__ == '__main__':
    main()

