
def url_get_serp_search(urls):
    '''
        retrieves search keywords from SERP's url
        tested on google and bing


        usage
            s = ['https://www.google.com/search?client=firefox-b-d&q=Hello+World%26']
            s.append('https://www.google.com/search?client=firefox-b-d&q=Hello+World')
            url_get_serp_search(chr(10).join(s))

            # Hello World&
            # Hello World

            # note the '&' preservation when decoding the url

    '''

    from urllib.parse import unquote

    return [
        unquote(k.replace('+', ' ').splitlines()[0])
        for k in
        re_findall(r'&q=([^&]+)', '\n'.join(urls))
        ]



if __main__ == '__main__':
    for text in url_get_serp_search(urls):
        print(text)

