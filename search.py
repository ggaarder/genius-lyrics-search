def genius_api_client_access_token():
    # https://genius.com/api-clients
    return 'get it yourself'

def genius_lrc_url(search_term):
    """edited from github.com/jasonqng/genius-lyrics-search"""
    import urllib2, json

    querystring = "http://api.genius.com/search?q={}&page={}".format(urllib2.quote(search_term), 1)
    request = urllib2.Request(querystring)
    request.add_header("Authorization", "Bearer " + genius_api_client_access_token())
    request.add_header("User-Agent", "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)")
    response = urllib2.urlopen(request, timeout=4)
    raw = response.read()
    json_obj = json.loads(raw)

    # return the first result
    return json_obj["response"]["hits"][0]["result"]["url"]
