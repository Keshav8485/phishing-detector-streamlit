import re
import pandas as pd
from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)
    hostname = parsed.netloc
    path = parsed.path

    features = {
        'url_length': len(url),
        'hostname_length': len(hostname),
        'path_length': len(path),
        'has_ip': int(bool(re.search(r'(\d{1,3}\.){3}\d{1,3}', hostname))),
        'has_https': int(parsed.scheme == 'https'),
        'has_at_symbol': int('@' in url),
        'has_hyphen': int('-' in hostname),
        'num_dots': url.count('.'),
        'has_suspicious_words': int(any(word in url.lower() for word in ['login', 'verify', 'bank', 'update', 'free']))
    }

    return pd.DataFrame([features])
