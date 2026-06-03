# Advanced Usage of the Requests Library for Automation Testing

## Introduction

The `requests` library provides a simple, elegant API for HTTP interactions. For automation testing, however, basic usage is often insufficient to handle complex scenarios such as session persistence, custom authentication, streaming large payloads, and fine‑grained control over connections. This document covers the advanced features of `requests` that are essential for building robust, maintainable, and high‑performance test automation frameworks. Each section includes practical examples and best practices tailored for QA engineers.

---

## Session Objects

A `Session` object persists parameters across requests, reuses connections, and maintains cookies. This dramatically improves performance when interacting with the same host and is critical for simulating authenticated user sessions.

### Creating and Using a Session

```python
import requests

s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
response = s.get('https://httpbin.org/cookies')
print(response.text)
# Output: {"cookies": {"sessioncookie": "123456789"}}
```

### Merging Session and Request Data

Session‑level defaults (e.g., headers, authentication) are merged with per‑request parameters. Per‑request values take precedence.

```python
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# Both 'x-test' and 'x-test2' are sent
s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
```

**Important:** Method‑level parameters override session‑level ones, but they are **not** persisted across requests. For example, cookies passed in a single request do not affect subsequent requests:

```python
s = requests.Session()
s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
s.get('https://httpbin.org/cookies')  # No cookies sent
```

To add cookies to the session itself, use `Session.cookies`.

### Using Sessions as Context Managers

Sessions should be closed after use to release resources. The context manager ensures proper cleanup even when exceptions occur:

```python
with requests.Session() as s:
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
```

### Removing a Value from a Dict Parameter

If a session‑level dictionary key should be omitted for a particular request, set its value to `None` in the method‑level parameter:

```python
s.headers.update({'x-test': 'true', 'x-other': 'value'})
s.get('https://httpbin.org/headers', headers={'x-test': None})  # 'x-test' is omitted
```

---

## Request and Response Objects

When you make a request, `requests` constructs a `Request` object and returns a `Response` object. The `Response` contains the server’s reply, and its `request` attribute holds the original `PreparedRequest`.

```python
response = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
print(response.headers)          # Headers from the server
print(response.request.headers)  # Headers sent to the server
```

This is useful for debugging and logging.

---

## Prepared Requests

Prepared requests allow you to modify the request **after** it has been constructed but **before** it is sent. This is useful for injecting custom logic, such as modifying the body or headers, while still leveraging session‑level state.

### Basic Preparation

```python
from requests import Request, Session

s = Session()
req = Request('POST', 'https://httpbin.org/post', data={'key': 'value'})
prepped = req.prepare()

# Modify the prepared request
prepped.body = 'No, I want exactly this as the body.'
del prepped.headers['Content-Type']

response = s.send(prepped)
print(response.status_code)
```

### Using Session State

To include session‑level cookies and defaults, prepare the request through the session:

```python
prepped = s.prepare_request(req)  # merges session settings
response = s.send(prepped)
```

### Environment Settings

Prepared requests do **not** automatically inherit environment settings (e.g., `REQUESTS_CA_BUNDLE`). To merge them, use `merge_environment_settings`:

```python
settings = s.merge_environment_settings(prepped.url, {}, None, None, None)
response = s.send(prepped, **settings)
```

---

## SSL Certificate Verification

By default, `requests` verifies SSL certificates. This is essential for production security.

- **Enable verification** (default):
  ```python
  response = requests.get('https://github.com')
  ```

- **Use a custom CA bundle**:
  ```python
  response = requests.get('https://github.com', verify='/path/to/ca-bundle.pem')
  ```

- **Disable verification** (for testing only, never in production):
  ```python
  response = requests.get('https://kennethreitz.org', verify=False)
  ```
  **Warning:** Disabling verification makes the application vulnerable to man‑in‑the‑middle attacks.

- **Environment variables**:
  - `REQUESTS_CA_BUNDLE` – overrides the default CA bundle.
  - `CURL_CA_BUNDLE` – used as a fallback.

---

## Client Side Certificates

To present a client certificate for mutual TLS authentication, use the `cert` parameter. The certificate file must contain the private key unencrypted.

```python
response = requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
```

For session‑wide usage:

```python
s = requests.Session()
s.cert = '/path/client.cert'
```

---

## CA Certificates

`requests` relies on the `certifi` package for the bundle of trusted CA certificates. To keep the bundle up‑to‑date:

```bash
pip install --upgrade certifi
```

If `certifi` is not installed, a fallback bundle is used, which may be outdated. Always include `certifi` in your project dependencies.

---

## Body Content Workflow

By default, the response body is downloaded immediately. For large responses, you can defer downloading using `stream=True`.

```python
response = requests.get('https://github.com/psf/requests/tarball/main', stream=True)
if int(response.headers['content-length']) < 10_000_000:
    content = response.content
```

### Streaming with `iter_content` and `iter_lines`

- `iter_content(chunk_size)` – iterates over the response data in chunks.
- `iter_lines()` – iterates over the response line by line (useful for streaming APIs).

```python
with requests.get('https://httpbin.org/stream/20', stream=True) as r:
    for line in r.iter_lines(decode_unicode=True):
        if line:
            print(line)  # each line is a JSON object
```

**Important:** When using `stream=True`, you **must** consume the data or call `Response.close` to release the connection back to the pool. Using a context manager (`with` statement) ensures proper cleanup.

---

## Keep‑Alive

Sessions automatically reuse connections (keep‑alive). This reduces latency and overhead for multiple requests to the same host.

```python
with requests.Session() as s:
    s.get('https://httpbin.org/get')
    s.get('https://httpbin.org/get')  # same connection
```

Connections are released only after the entire response body is read. To keep the connection alive, read the content.

---

## Streaming Uploads

For large files, you can stream the upload without loading the entire file into memory by passing a file‑like object to the `data` parameter.

```python
with open('massive-body', 'rb') as f:
    requests.post('http://some.url/streamed', data=f)
```

**Important:** Always open files in binary mode to avoid `Content-Length` calculation errors.

---

## Chunk‑Encoded Requests

You can send a request with chunked transfer encoding by providing an iterator (generator) as the body. The `Content-Length` header is omitted, and the data is sent in chunks.

```python
def gen():
    yield 'hi'
    yield 'there'

requests.post('http://some.url/chunked', data=gen())
```

For chunked responses, iterate with `iter_content` (with `stream=True`) to receive data as it arrives.

---

## POST Multiple Multipart‑Encoded Files

To send multiple files under the same form field (e.g., a multi‑file upload), pass a list of tuples to the `files` parameter.

```python
multiple_files = [
    ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
    ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))
]
response = requests.post('https://httpbin.org/post', files=multiple_files)
```

Again, open files in binary mode.

---

## Event Hooks

Hooks allow you to execute custom functions at specific points in the request/response lifecycle. Currently, only the `response` hook is available.

### Per‑Request Hook

```python
def print_url(response, *args, **kwargs):
    print(response.url)

response = requests.get('https://httpbin.org/', hooks={'response': print_url})
```

### Multiple Hooks

You can attach a list of callbacks; they are executed in order.

```python
def record_hook(response, *args, **kwargs):
    response.hook_called = True
    return response

hooks = {'response': [print_url, record_hook]}
response = requests.get('https://httpbin.org/', hooks=hooks)
print(response.hook_called)  # True
```

### Session‑Wide Hooks

Add hooks to a session to apply them to all requests.

```python
s = requests.Session()
s.hooks['response'].append(print_url)
s.get('https://httpbin.org/')
```

If a hook returns a value, it replaces the original response object.

---

## Custom Authentication

For APIs that use non‑standard authentication schemes, you can create a custom authentication class by subclassing `AuthBase`.

```python
from requests.auth import AuthBase

class PizzaAuth(AuthBase):
    def __init__(self, username):
        self.username = username

    def __call__(self, r):
        r.headers['X-Pizza'] = self.username
        return r

response = requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
```

The `__call__` method receives the `PreparedRequest` and must return it (optionally modified).

---

## Proxies

### Per‑Request Proxies

```python
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}
requests.get('http://example.org', proxies=proxies)
```

### Session‑Wide Proxies

```python
s = requests.Session()
s.proxies.update(proxies)
s.get('http://example.org')
```

**Note:** Session‑level proxies can be overridden by environment variables (`HTTP_PROXY`, `HTTPS_PROXY`, etc.). To ensure proxies are used, pass them explicitly with each request, or set the environment variables before running the script.

### Proxy Authentication

Include credentials in the proxy URL:

```python
proxies = {'http': 'http://user:pass@10.10.1.10:3128/'}
```

**Security Warning:** Avoid storing credentials in code or environment variables that are version‑controlled.

### SOCKS Proxies

Support for SOCKS proxies requires an extra dependency:

```bash
pip install 'requests[socks]'
```

Then use the `socks5` or `socks5h` scheme:

```python
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}
```

- `socks5` – DNS resolution happens on the client.
- `socks5h` – DNS resolution happens on the proxy server.

---

## Streaming Requests (Server‑Sent Events)

For streaming APIs like Twitter’s firehose, use `stream=True` and iterate over `iter_lines()`.

```python
import json

r = requests.get('https://httpbin.org/stream/20', stream=True)
for line in r.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        print(json.loads(decoded_line))
```

When using `decode_unicode=True`, ensure a fallback encoding if the server does not provide one:

```python
if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    if line:
        print(json.loads(line))
```

**Important:** `iter_lines()` is not reentrant safe. If you need to call it from multiple places, store the iterator:

```python
lines = r.iter_lines()
first = next(lines)
for line in lines:
    process(line)
```

---

## Compliance with HTTP Specifications

### Encodings

When no encoding is specified in the HTTP headers and the `Content-Type` is `text/*`, `requests` defaults to `ISO-8859-1` per RFC 2616. To use a different encoding, set `r.encoding` manually before accessing `r.text`.

### HTTP Verbs

All standard HTTP verbs are supported via convenience methods (`get`, `post`, `put`, `patch`, `delete`, `head`, `options`) and the generic `request` method. The following example uses the GitHub API to demonstrate various verbs:

```python
import requests
from requests.auth import HTTPBasicAuth

# GET an issue
r = requests.get('https://api.github.com/repos/psf/requests/issues/482')
issue = r.json()
print(issue['title'])

# POST a comment (requires authentication)
auth = HTTPBasicAuth('user', 'pass')
url = 'https://api.github.com/repos/psf/requests/issues/482/comments'
body = {'body': 'Sounds great!'}
r = requests.post(url, json=body, auth=auth)
comment_id = r.json()['id']

# PATCH to update the comment
update_url = f'https://api.github.com/repos/psf/requests/issues/comments/{comment_id}'
new_body = {'body': 'I will do it after feeding my cat.'}
r = requests.patch(update_url, json=new_body, auth=auth)

# DELETE the comment
r = requests.delete(update_url, auth=auth)

# HEAD to check rate limit headers
r = requests.head('https://api.github.com/repos/psf/requests/issues/482')
print(r.headers['x-ratelimit-remaining'])
```

### Link Headers

Some APIs use `Link` headers for pagination. `requests` automatically parses them into `Response.links`:

```python
r = requests.head('https://api.github.com/users/kennethreitz/repos?page=1&per_page=10')
print(r.links['next'])   # {'url': '...', 'rel': 'next'}
```

---

## Transport Adapters

Transport adapters allow you to customize how requests are sent over the network. By default, `requests` uses the `HTTPAdapter` (powered by `urllib3`). You can create custom adapters to change SSL versions, add retries, or implement other low‑level behaviour.

### Example: Forcing SSLv3

```python
import ssl
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

class Ssl3HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_version=ssl.PROTOCOL_SSLv3
        )

s = requests.Session()
s.mount('https://', Ssl3HttpAdapter())
```

### Example: Automatic Retries

```python
from urllib3.util import Retry
from requests.adapters import HTTPAdapter

s = requests.Session()
retries = Retry(
    total=3,
    backoff_factor=0.1,
    status_forcelist=[502, 503, 504],
    allowed_methods={'GET', 'POST'}
)
s.mount('https://', HTTPAdapter(max_retries=retries))
```

Adapters are mounted to a URL prefix. The adapter with the longest matching prefix is used.

---

## Header Ordering

By default, the order of headers in the request is not guaranteed. If order matters (e.g., for certain servers), pass an `OrderedDict` to the `headers` parameter. Note that default headers (e.g., `User-Agent`) may still be added; to control ordering fully, set session‑level headers to an `OrderedDict`.

```python
from collections import OrderedDict

headers = OrderedDict()
headers['X-First'] = 'value1'
headers['X-Second'] = 'value2'
response = requests.get('https://httpbin.org/headers', headers=headers)
```

---

## Timeouts

Timeouts are critical to prevent hanging tests. By default, requests never time out.

- **Single timeout** (applies to both connect and read):
  ```python
  response = requests.get('https://github.com', timeout=5)
  ```

- **Separate connect and read timeouts**:
  ```python
  response = requests.get('https://github.com', timeout=(3.05, 27))
  ```

- **No timeout** (not recommended for production tests):
  ```python
  response = requests.get('https://github.com', timeout=None)
  ```

**Note:** The connect timeout applies per connection attempt. If the host resolves to multiple IP addresses, the effective timeout may be multiplied. The read timeout is the time between receiving bytes, not the total download time.

---

## Best Practices for Automation Testing

1. **Always use sessions** to reuse connections and maintain cookies.
2. **Set default timeouts** at the session level to avoid hanging tests.
3. **Handle exceptions** explicitly – `ConnectionError`, `Timeout`, `HTTPError`.
4. **Log request/response details** for debugging (use hooks or logging).
5. **Use environment variables** for sensitive data like credentials and base URLs.
6. **Mock external calls** in unit tests to isolate the code under test.
7. **Validate JSON responses** against schemas to ensure data integrity.
8. **Consider retry mechanisms** for flaky network conditions, but with backoff.
9. **Close sessions** (use context manager) to free resources.
10. **Keep the `certifi` package updated** to trust the latest root certificates.

---

## Conclusion

The advanced features of the `requests` library empower automation test engineers to build reliable, efficient, and secure test suites. By mastering sessions, streaming, custom authentication, transport adapters, and proper error handling, you can simulate complex user interactions and validate API behaviour under real‑world conditions. These techniques are not only interview‑ready but also form the backbone of production‑grade test automation frameworks.

For further details, refer to the official `requests` documentation and explore the source code of the library to understand the underlying mechanics.