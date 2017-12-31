# genius-lyrics-search
Search lyrics on [https://api.genius.com](https://api.genius.com) and return the url.

## Requirements and Setup
* Python 2
* Get yourself a client access token from Genius.com: [https://genius.com/api-clients](https://genius.com/api-clients) and **modify the code**.

## Example

```python
>>> genius_lrc_url('We are the Champions')
u'https://genius.com/Queen-we-are-the-champions-lyrics'
>>> genius_lrc_url('Somebody to Love')
u'https://genius.com/Queen-somebody-to-love-lyrics'
```
