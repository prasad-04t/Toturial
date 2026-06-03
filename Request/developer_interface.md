# Developer Interface: Comprehensive Reference for Automation Testing Engineers

This document provides an exhaustive reference to the `requests` library’s internal interfaces, classes, and methods. It is intended for automation testing engineers who need to understand the library at a deep level to build robust, maintainable test frameworks. All content is derived from the official `requests` documentation and augmented with best practices for production‑grade testing.

---

## 1. Main Interface

The `requests` module exposes a simple API consisting of seven top‑level methods. All of them return a `Response` object.

### `requests.request(method, url, **kwargs)`

Constructs and sends a `Request`.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `method` | `str` | HTTP method: `GET`, `OPTIONS`, `HEAD`, `POST`, `PUT`, `PATCH`, or `DELETE`. |
| `url` | `str` | Target URL. |
| `params` | `dict`, `list` of tuples, `bytes` | Query string parameters. |
| `data` | `dict`, `list`, `bytes`, file‑like | Body data (form‑encoded or raw). |
| `json` | JSON‑serializable object | JSON‑encoded body (overrides `data` if set). |
| `headers` | `dict` | HTTP headers. |
| `cookies` | `dict`, `CookieJar` | Cookies to send. |
| `files` | `dict` | Multipart‑encoded files. See *file‑tuple* format below. |
| `auth` | tuple, `AuthBase` | Authentication credentials or handler. |
| `timeout` | `float`, `tuple` | Connect/read timeout in seconds. |
| `allow_redirects` | `bool` | Follow redirects? Default `True`. |
| `proxies` | `dict` | Protocol‑to‑URL mapping for proxies. |
| `verify` | `bool`, `str` | SSL verification: `True` (default), `False`, or path to CA bundle. |
| `stream` | `bool` | If `True`, response body is not downloaded immediately. |
| `cert` | `str`, `tuple` | Client certificate: path to `.pem` file or (`cert`, `key`) tuple. |

**Returns:** `Response` object.

**Example:**

```python
import requests
response = requests.request('GET', 'https://httpbin.org/get', params={'key': 'value'})
```

### Shortcut Methods

Each shortcut delegates to `request()` with default arguments appropriate for the verb.

#### `requests.get(url, params=None, **kwargs)`

Sends a `GET` request.

#### `requests.post(url, data=None, json=None, **kwargs)`

Sends a `POST` request.

#### `requests.put(url, data=None, **kwargs)`

Sends a `PUT` request.

#### `requests.patch(url, data=None, **kwargs)`

Sends a `PATCH` request.

#### `requests.delete(url, **kwargs)`

Sends a `DELETE` request.

#### `requests.head(url, **kwargs)`

Sends a `HEAD` request.  
**Note:** `allow_redirects` defaults to `False` for `head`.

#### `requests.options(url, **kwargs)`

Sends an `OPTIONS` request.

---

## 2. Exceptions

All exceptions raised by `requests` inherit from `RequestException`. They are organised in a hierarchy that helps you handle errors precisely.

| Exception | Description |
|-----------|-------------|
| `RequestException` | Base class for all request‑related exceptions. |
| `ConnectionError` | Network problem (DNS failure, refused connection, etc.). |
| `HTTPError` | HTTP error (4xx or 5xx) raised by `raise_for_status()`. |
| `Timeout` | Base class for timeout exceptions. |
| `ConnectTimeout` | Timeout occurred while trying to connect. |
| `ReadTimeout` | Server did not send data in the allotted time. |
| `TooManyRedirects` | Exceeded the maximum number of redirects. |
| `JSONDecodeError` | Response body could not be decoded as JSON. |

**Example error handling:**

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.ConnectTimeout:
    # Handle connection timeout (safe to retry)
except requests.exceptions.ReadTimeout:
    # Handle read timeout
except requests.exceptions.HTTPError as e:
    # Log e.response.status_code and e.response.text
except requests.exceptions.JSONDecodeError:
    # Response was not valid JSON
except requests.exceptions.RequestException:
    # Catch‑all for other request errors
```

---

## 3. Request Sessions

The `Session` object provides persistent state across requests: cookies, headers, authentication, connection pooling, and proxy settings. It is the recommended way to perform multiple requests to the same host.

### `class requests.Session`

**Attributes**

| Attribute | Description |
|-----------|-------------|
| `auth` | Default authentication tuple or `AuthBase` object. |
| `cert` | Default client certificate (string or tuple). |
| `cookies` | `RequestsCookieJar` with all outstanding cookies. |
| `headers` | Case‑insensitive dictionary of default headers. |
| `hooks` | Dictionary of event hooks (e.g., `'response'`). |
| `max_redirects` | Maximum number of redirects allowed. |
| `params` | Default query parameters (dictionary). |
| `proxies` | Dictionary of protocol → proxy URL. |
| `stream` | Default `stream` value for requests. |
| `trust_env` | If `True`, respects environment variables (proxies, netrc). Default `True`. |
| `verify` | Default SSL verification setting (bool or path). |

**Methods**

| Method | Description |
|--------|-------------|
| `close()` | Closes all adapters and releases connections. |
| `delete(url, **kwargs)` | Sends a `DELETE` request. |
| `get(url, **kwargs)` | Sends a `GET` request. |
| `head(url, **kwargs)` | Sends a `HEAD` request. |
| `options(url, **kwargs)` | Sends an `OPTIONS` request. |
| `patch(url, data=None, **kwargs)` | Sends a `PATCH` request. |
| `post(url, data=None, json=None, **kwargs)` | Sends a `POST` request. |
| `put(url, data=None, **kwargs)` | Sends a `PUT` request. |
| `request(method, url, **kwargs)` | Core method; merges session defaults. |
| `mount(prefix, adapter)` | Registers a transport adapter for a URL prefix. |
| `prepare_request(request)` | Prepares a `PreparedRequest` using session settings. |
| `send(request, **kwargs)` | Sends a `PreparedRequest`. |
| `merge_environment_settings(url, proxies, stream, verify, cert)` | Returns a dict of settings merged with environment variables. |

**Usage**

```python
with requests.Session() as s:
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})
    s.get('https://httpbin.org/get')
```

**Connection Pooling**  
Sessions automatically reuse connections for the same host, improving performance.

**Context Manager**  
Using `with` guarantees that the session is closed even if an exception occurs.

---

## 4. Lower‑Level Classes

These classes give you fine‑grained control over request construction and response handling.

### `class requests.Request`

A user‑created request object, used to construct a `PreparedRequest`.

**Parameters:**
- `method`, `url`, `headers`, `files`, `data`, `params`, `auth`, `cookies`, `hooks`, `json`

**Methods:**
- `prepare()` → `PreparedRequest`
- `register_hook(event, hook)`
- `deregister_hook(event, hook)`

### `class requests.PreparedRequest`

The fully mutable request object that is actually sent over the wire. Created by calling `prepare()` on a `Request` or via `Session.prepare_request()`.

**Attributes:**
- `body` – the request body (bytes)
- `headers` – dictionary of headers
- `hooks` – dictionary of hooks
- `method` – HTTP verb
- `url` – target URL

**Methods:**
- `prepare(method, url, headers, files, data, params, auth, cookies, hooks, json)`
- `prepare_auth(auth, url)`
- `prepare_body(data, files, json)`
- `prepare_cookies(cookies)`
- `prepare_headers(headers)`
- `prepare_hooks(hooks)`
- `prepare_method(method)`
- `prepare_url(url, params)`

**Example (customising before sending):**

```python
from requests import Request, Session

s = Session()
req = Request('POST', 'https://httpbin.org/post', data={'key': 'value'})
prepped = s.prepare_request(req)
prepped.body = 'Custom body'
response = s.send(prepped)
```

### `class requests.Response`

The object returned by all request methods. It encapsulates the server’s response.

**Attributes**

| Attribute | Description |
|-----------|-------------|
| `apparent_encoding` | The encoding guessed from content (by `charset_normalizer`/`chardet`). |
| `content` | Response body as bytes. |
| `cookies` | `RequestsCookieJar` of received cookies. |
| `elapsed` | `timedelta` between sending the request and receiving the headers. |
| `encoding` | Encoding used for `.text`. You can set it manually. |
| `headers` | Case‑insensitive dictionary of response headers. |
| `history` | List of `Response` objects from redirects (oldest first). |
| `is_permanent_redirect` | `True` if the response is a permanent redirect (301, 308). |
| `is_redirect` | `True` if the response is any redirect (3xx). |
| `links` | Parsed `Link` header as a dictionary. |
| `next` | `PreparedRequest` for the next request in a redirect chain, if any. |
| `ok` | `True` if status code is < 400. |
| `raw` | Underlying `urllib3.response.HTTPResponse` (requires `stream=True`). |
| `reason` | Textual reason (e.g., "Not Found"). |
| `request` | The `PreparedRequest` that generated this response. |
| `status_code` | HTTP status code (e.g., 200, 404). |
| `text` | Response body as decoded string (respects `encoding`). |
| `url` | Final URL after redirects. |

**Methods**

| Method | Description |
|--------|-------------|
| `close()` | Releases the connection back to the pool. |
| `iter_content(chunk_size=1, decode_unicode=False)` | Iterates over response data in chunks. |
| `iter_lines(chunk_size=512, decode_unicode=False, delimiter=None)` | Iterates over response data line by line. |
| `json(**kwargs)` | Decodes the response body as JSON. Raises `JSONDecodeError` on failure. |
| `raise_for_status()` | Raises `HTTPError` if status code is 4xx or 5xx. |

**Example (streaming):**

```python
with requests.get('https://httpbin.org/stream/20', stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode('utf-8'))
```

### Transport Adapters

Adapters provide a pluggable mechanism for handling HTTP and HTTPS requests. The default is `HTTPAdapter`.

#### `class requests.adapters.BaseAdapter`

Abstract base class for all adapters. Must implement `send()`.

#### `class requests.adapters.HTTPAdapter`

The built‑in adapter using `urllib3`. It handles connection pooling, retries, SSL, and proxies.

**Constructor parameters:**
- `pool_connections` – number of connection pools to cache (default 10)
- `pool_maxsize` – maximum connections per pool (default 10)
- `max_retries` – number of retries (default 0)
- `pool_block` – block if pool is exhausted (default `False`)

**Key methods:**
- `send(request, stream=False, timeout=None, verify=True, cert=None, proxies=None)` – sends a request.
- `close()` – closes all pooled connections.
- `mount` is called on the session to register an adapter for a URL prefix.

**Example (retries with backoff):**

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

s = requests.Session()
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[502, 503, 504])
s.mount('https://', HTTPAdapter(max_retries=retries))
```

---

## 5. Authentication

Authentication handlers are subclasses of `AuthBase` and are passed via the `auth` parameter.

### Provided Authentication Classes

| Class | Description |
|-------|-------------|
| `HTTPBasicAuth(username, password)` | HTTP Basic Authentication. |
| `HTTPDigestAuth(username, password)` | HTTP Digest Authentication. |
| `HTTPProxyAuth(username, password)` | HTTP Proxy Authentication. |

### Custom Authentication

Subclass `AuthBase` and implement `__call__(self, r)`. The method receives a `PreparedRequest` and must return it (possibly modified).

```python
class MyAuth(requests.auth.AuthBase):
    def __call__(self, r):
        r.headers['X-Custom-Token'] = 'secret'
        return r

requests.get('https://api.example.com', auth=MyAuth())
```

### OAuth 1 and OAuth 2

These are provided by the `requests-oauthlib` library. See its documentation for details.

### netrc Authentication

If `auth` is omitted, `requests` automatically reads credentials from the user’s `~/.netrc` (or `%USERPROFILE%\_netrc`). This can be disabled by setting `session.trust_env = False`.

---

## 6. Encodings

Requests provides utility functions to help with character encodings.

### `requests.utils.get_encodings_from_content(content)`

Extracts a list of encodings from a bytestring (e.g., from `<meta>` tags in HTML). Returns a list of strings.

### `requests.utils.get_encoding_from_headers(headers)`

Returns the encoding from the `Content-Type` header, if present.

### `requests.utils.get_unicode_from_response(r)`

Returns the response content as Unicode, using the best available encoding.

---

## 7. Cookies

Requests provides a convenient cookie jar that behaves like a dictionary.

### `class requests.cookies.RequestsCookieJar`

Extends `http.cookiejar.CookieJar` with a dict‑like interface. It is the default cookie jar used by sessions.

**Key methods:**

| Method | Description |
|--------|-------------|
| `get(name, default=None, domain=None, path=None)` | Returns the cookie value, optionally narrowing by domain/path. |
| `set(name, value, **kwargs)` | Sets a cookie (supports domain, path, etc.). |
| `keys()` | Returns a list of cookie names. |
| `values()` | Returns a list of cookie values. |
| `items()` | Returns a list of (name, value) tuples. |
| `update(other)` | Merges another jar or dict. |
| `clear(domain=None, path=None, name=None)` | Clears matching cookies. |
| `get_dict(domain=None, path=None)` | Returns a plain dict of cookies for the given domain/path. |

**Utility functions:**

- `cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)`
- `dict_from_cookiejar(cj)`
- `add_dict_to_cookiejar(cj, cookie_dict)`

---

## 8. Status Code Lookup

The `requests.codes` object provides symbolic names for HTTP status codes.

```python
requests.codes.ok          # 200
requests.codes.not_found   # 404
requests.codes.teapot      # 418
```

The object behaves like a dictionary; both uppercase and lowercase names are accepted. Common aliases exist (e.g., `ok`, `OK`, `okay` all map to 200).

---

## 9. Migration Notes

### Migrating from 0.x to 1.x

- `Response.json` changed from a property to a method: `r.json()`.
- Session API changed: `requests.session()` is now a class, and configuration is done via attributes (e.g., `s.auth = ...`).
- Hooks other than `response` were removed.
- `prefetch` parameter was replaced by `stream` (with opposite logic).
- The `config` parameter was removed; logging should be used for verbosity.

### Migrating from 1.x to 2.x

- `RequestException` now inherits from `IOError` (instead of `RuntimeError`).
- Invalid URL escape sequences raise `InvalidURL` (subclass of `RequestException`) instead of `ValueError`.
- `httplib.IncompleteRead` now becomes `ChunkedEncodingError`.
- Proxy URLs must now include the scheme (e.g., `http://`).
- Header keys are now native strings on all Python versions.
- Header values should always be strings.

---

## 10. Best Practices for Automation Testing

- **Use Sessions** to maintain cookies and reuse connections across multiple test cases.
- **Always set timeouts** to prevent hanging tests.
- **Handle exceptions** appropriately – log the response body when an HTTP error occurs.
- **Validate JSON responses** against a schema using `jsonschema`.
- **Mock external calls** in unit tests (e.g., with `responses` or `unittest.mock`).
- **Secure credentials** – never hardcode them; use environment variables or secret stores.
- **Enable debug logging** during test development to inspect request/response details.
- **Use `verify=False` only in local development** – never in production.
- **Configure retries** for flaky networks using `HTTPAdapter` with a `Retry` object.
- **Close sessions** (or use context managers) to release connections.

---

## 11. Conclusion

The `requests` library’s developer interface provides a complete set of tools for constructing, sending, and handling HTTP requests. By understanding the main interface, session management, lower‑level classes, authentication mechanisms, and the exception hierarchy, automation test engineers can build reliable, efficient, and secure test frameworks. This reference document serves as a comprehensive guide to all the interfaces you will need in production‑grade testing.

For further information, refer to the official `requests` documentation and the source code of the library itself.