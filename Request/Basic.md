# Requests Library for Automation Testing: Professional Documentation

## Introduction

The `requests` library is the de facto standard for making HTTP requests in Python. Its elegant, intuitive API and robust feature set make it an indispensable tool for automation testing engineers, particularly in the context of API testing, service virtualization, and integration testing. 

## Prerequisites

- Python 3.7 or later installed.
- `requests` library installed. It is recommended to install it within a virtual environment:
  ```bash
  pip install requests
  ```
- Verify the installation and version:
  ```python
  import requests
  print(requests.__version__)
  ```
- For handling Brotli‑compressed responses, install an optional Brotli library:
  ```bash
  pip install brotli  # or brotlicffi
  ```

## Core Concepts: Making HTTP Requests

The `requests` module provides a simple API for all standard HTTP methods. The following examples demonstrate the most common operations.

### Importing the Module

```python
import requests
```

### GET Request

```python
response = requests.get('https://api.github.com/events')
```

### POST Request with Form Data

```python
response = requests.post('https://httpbin.org/post', data={'key': 'value'})
```

### Other HTTP Methods

```python
response = requests.put('https://httpbin.org/put', data={'key': 'value'})
response = requests.delete('https://httpbin.org/delete')
response = requests.head('https://httpbin.org/get')
response = requests.options('https://httpbin.org/get')
```

Each method returns a `Response` object, which encapsulates all information returned by the server.

## Passing Parameters in URLs

Query string parameters can be passed as a dictionary using the `params` keyword. This is the recommended approach, as it automatically handles encoding.

```python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=payload)
print(response.url)  # https://httpbin.org/get?key2=value2&key1=value1
```

- Dictionary keys with a value of `None` are omitted.
- To pass multiple values for the same key, use a list as the value:
  ```python
  payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
  response = requests.get('https://httpbin.org/get', params=payload)
  print(response.url)  # https://httpbin.org/get?key1=value1&key2=value2&key2=value3
  ```

## Handling Responses

A `Response` object provides several ways to access the server’s reply.

### Text Content

Use `.text` to obtain the response body as a string. Requests automatically decodes the content based on the HTTP headers.

```python
response = requests.get('https://api.github.com/events')
print(response.text)
```

If you need to override the encoding, set the `encoding` property before accessing `.text`:

```python
response.encoding = 'ISO-8859-1'
print(response.text)
```

### Binary Content

For non‑textual responses (e.g., images, PDFs), use `.content` to obtain the raw bytes. Transfer encodings like `gzip` and `deflate` are automatically decoded.

```python
response = requests.get('https://example.com/image.png')
with open('image.png', 'wb') as f:
    f.write(response.content)
```

### JSON Content

If the response is JSON, use the `.json()` method. It returns a Python dictionary/list.

```python
response = requests.get('https://api.github.com/events')
data = response.json()
print(data[0]['repository']['url'])
```

**Note:** `.json()` may raise `requests.exceptions.JSONDecodeError` if the response is not valid JSON. Always handle this appropriately, and remember that a successful decode does not imply a successful HTTP request.

### Raw Response Content

For low‑level access to the raw socket response (e.g., when streaming large files), set `stream=True` and use `.raw`. However, the recommended way to stream content is to iterate over `.iter_content()`:

```python
response = requests.get('https://example.com/largefile.zip', stream=True)
with open('largefile.zip', 'wb') as fd:
    for chunk in response.iter_content(chunk_size=8192):
        fd.write(chunk)
```

`.iter_content()` automatically handles decoding of compressed transfers, whereas `.raw` does not.

### Status Codes

Check the HTTP status code with `.status_code`. For convenience, `requests` provides a `codes` object for symbolic comparisons:

```python
if response.status_code == requests.codes.ok:
    print('Success')
else:
    print('Failure')
```

To raise an exception for client or server errors (4xx/5xx), use `.raise_for_status()`:

```python
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f'HTTP error occurred: {e}')
```

### Headers

Response headers are accessible via the `.headers` attribute, which behaves like a dictionary but is case‑insensitive:

```python
content_type = response.headers.get('Content-Type')
print(content_type)
```

### Cookies

Cookies returned by the server can be accessed via `.cookies`:

```python
cookie_value = response.cookies.get('session_id')
```

To send cookies with a request, use the `cookies` parameter:

```python
cookies = {'session_id': 'abc123'}
response = requests.get('https://example.com/api', cookies=cookies)
```

For more advanced cookie handling (domain, path), use `requests.cookies.RequestsCookieJar`.

### Redirection and History

By default, `requests` follows redirects for all methods except `HEAD`. The `history` attribute contains a list of `Response` objects representing the redirect chain, ordered from oldest to most recent.

```python
response = requests.get('http://github.com/')
print(response.url)                # https://github.com/
print(response.status_code)        # 200
print(response.history)            # [<Response [301]>]
```

To disable redirection, use `allow_redirects=False`:

```python
response = requests.get('http://github.com/', allow_redirects=False)
print(response.status_code)        # 301
print(response.history)            # []
```

For `HEAD` requests, enable redirection with `allow_redirects=True`.

## Advanced Request Customization

### Custom Headers

Add custom headers by passing a dictionary to the `headers` parameter. Header names are case‑insensitive, but it is conventional to use title case.

```python
headers = {'User-Agent': 'my-automation-framework/1.0'}
response = requests.get('https://api.github.com/some/endpoint', headers=headers)
```

**Important:** Some headers are overridden by other mechanisms (e.g., `Authorization` from `auth` or `.netrc`, `Content-Length` automatically determined). Custom headers are simply passed through.

### Authentication

Requests supports several authentication methods:

- **Basic Authentication:** Use the `auth` parameter.
  ```python
  response = requests.get('https://api.example.com/data', auth=('username', 'password'))
  ```
- **Bearer Token / OAuth2:** Set the `Authorization` header explicitly.
  ```python
  headers = {'Authorization': 'Bearer YOUR_TOKEN'}
  response = requests.get('https://api.example.com/data', headers=headers)
  ```
- **Digest Authentication:** Use `requests.auth.HTTPDigestAuth`.
- **Netrc:** Credentials from `~/.netrc` are automatically used if no `auth` is provided.

### Timeouts

Always specify a timeout to prevent indefinite hangs. The `timeout` parameter defines the maximum number of seconds to wait for a response (i.e., until the server starts sending data). It does not limit the total download time.

```python
try:
    response = requests.get('https://api.github.com/', timeout=5)
except requests.exceptions.Timeout:
    print('Request timed out')
```

### Proxies

Configure proxies by passing a dictionary to the `proxies` parameter:

```python
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080',
}
response = requests.get('https://api.github.com/', proxies=proxies)
```

You can also set environment variables (`HTTP_PROXY`, `HTTPS_PROXY`) that requests will respect.

### SSL Verification

By default, requests verifies SSL certificates. To disable verification (e.g., for testing with self‑signed certificates), set `verify=False`. **Never disable verification in production** without a strong security review.

```python
response = requests.get('https://self-signed.badssl.com/', verify=False)
```

To use a custom CA bundle, pass the path:

```python
response = requests.get('https://api.example.com/', verify='/path/to/ca-bundle.pem')
```

### Sessions: Persisting Cookies and Connection Pooling

A `Session` object reuses the same TCP connection across multiple requests and persists cookies and headers. This is essential for efficiency and for maintaining state (e.g., login sessions) in test automation.

```python
with requests.Session() as session:
    # Login
    session.post('https://example.com/login', data={'user': 'test', 'pass': 'pass'})
    # Subsequent requests share cookies
    response = session.get('https://example.com/user/profile')
```

Sessions also support connection pooling, which dramatically improves performance when making many requests to the same host.

## Working with Data

### Form‑Encoded Data (application/x-www-form-urlencoded)

Pass a dictionary to the `data` parameter for standard HTML form submissions:

```python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)
```

If a key has multiple values, use a list of tuples or a dictionary with lists:

```python
payload = [('key1', 'value1'), ('key1', 'value2')]
response = requests.post('https://httpbin.org/post', data=payload)
```

### JSON Data

To send JSON‑encoded data, you have two options:

1. **Manually serialize and set the header:**
   ```python
   import json
   payload = {'some': 'data'}
   headers = {'Content-Type': 'application/json'}
   response = requests.post(url, data=json.dumps(payload), headers=headers)
   ```
2. **Use the `json` parameter** (recommended, available in requests 2.4.2+):
   ```python
   payload = {'some': 'data'}
   response = requests.post(url, json=payload)
   ```
   This automatically sets `Content-Type: application/json` and serializes the dictionary.

### Multipart‑Encoded File Uploads

Use the `files` parameter to upload files. Open the file in binary mode (`'rb'`).

```python
files = {'file': open('report.xls', 'rb')}
response = requests.post('https://httpbin.org/post', files=files)
```

You can explicitly set the filename, content type, and additional headers:

```python
files = {
    'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})
}
```

To send a file from a string (e.g., in‑memory data), use a tuple `(filename, data)`:

```python
files = {
    'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')
}
```

**Important:** For very large files, consider streaming the upload. The `requests-toolbelt` library provides support for streaming multipart uploads.

## Error Handling and Exceptions

Requests raises exceptions for network‑related problems, timeouts, and excessive redirects. All exceptions inherit from `requests.exceptions.RequestException`.

| Exception                    | Description                                      |
|------------------------------|--------------------------------------------------|
| `ConnectionError`            | DNS failure, refused connection, etc.            |
| `Timeout`                    | The server did not respond within the timeout.   |
| `TooManyRedirects`           | Exceeded the configured number of redirects.     |
| `HTTPError`                  | Raised by `raise_for_status()` for 4xx/5xx responses. |
| `JSONDecodeError`            | Invalid JSON when calling `.json()`.             |

Example of comprehensive error handling:

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    # Handle timeout
except requests.exceptions.ConnectionError:
    # Handle network issues
except requests.exceptions.HTTPError as e:
    # Handle HTTP error (4xx/5xx)
except requests.exceptions.JSONDecodeError:
    # Handle invalid JSON
except requests.exceptions.RequestException as e:
    # Catch-all for other request-related errors
```

## Best Practices for Automation Testing

### 1. Use Sessions for Efficiency

In test suites, create a session once (e.g., in a fixture) and reuse it across tests. This reduces connection overhead and preserves cookies.

```python
# pytest fixture example
import pytest
import requests

@pytest.fixture(scope='session')
def api_session():
    session = requests.Session()
    # Optionally set base URL, headers, etc.
    session.headers.update({'User-Agent': 'MyTestFramework/1.0'})
    yield session
    session.close()
```

### 2. Separate Configuration from Code

Store base URLs, credentials, and other environment‑specific values in environment variables or configuration files. Use a library like `python-dotenv` for local development.

```python
import os
BASE_URL = os.environ.get('API_BASE_URL', 'https://default.api.com')
```

### 3. Assert Response Structure

Validate both the HTTP status code and the content. Use assertions that provide clear error messages.

```python
def test_get_user(api_session):
    response = api_session.get(f'{BASE_URL}/users/1')
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    data = response.json()
    assert data['id'] == 1, f'Expected user ID 1, got {data["id"]}'
    assert 'name' in data, 'Response missing "name" field'
```

### 4. Use Retries for Flaky Networks

Wrap important requests in a retry mechanism. The `requests` library does not provide built‑in retries, but you can use `urllib3`’s `Retry` object with a session adapter.

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))
```

### 5. Logging and Debugging

Enable logging for the `requests` and `urllib3` modules to capture request/response details. This is invaluable for diagnosing test failures.

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('urllib3').setLevel(logging.DEBUG)
```

Alternatively, use a custom hook to log every request and response.

### 6. Mocking External Calls in Unit Tests

When testing code that uses `requests`, mock the network calls to avoid dependencies and ensure deterministic tests. The `responses` library or `unittest.mock` can be used.

```python
import responses

@responses.activate
def test_my_function():
    responses.add(responses.GET, 'https://api.example.com/data',
                  json={'result': 'success'}, status=200)
    # Call the function that uses requests.get
    result = my_function()
    assert result == 'success'
```

### 7. Validate JSON Schema

For APIs that return complex JSON structures, validate the response against a schema using libraries like `jsonschema`.

```python
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"}
    },
    "required": ["id", "name"]
}
data = response.json()
validate(instance=data, schema=schema)
```

### 8. Handle Timeouts Consistently

Set a default timeout at the session level to ensure all requests are protected:

```python
session = requests.Session()
session.timeout = 10  # Default timeout for all requests via this session
```

## Performance Considerations

- **Connection Pooling:** Sessions automatically pool connections, reducing latency for repeated requests to the same host.
- **Streaming Large Responses:** Use `stream=True` and `iter_content` to avoid loading large responses into memory.
- **Asynchronous Requests:** For high‑throughput scenarios, consider `requests-futures` or `aiohttp` for asynchronous I/O. The synchronous `requests` library is not suitable for massive concurrency.
- **Compression:** `requests` automatically handles `gzip` and `deflate` decoding; enable Brotli for additional compression support.

## Security Best Practices

- **Never hardcode credentials:** Use environment variables, secret managers, or encrypted configuration files.
- **Validate SSL certificates** in production: Always set `verify=True` (the default) and use trusted CA bundles.
- **Avoid sending sensitive data in URLs** (e.g., in query parameters); prefer the request body for POST/PUT.
- **Be cautious with redirects:** If your application handles sensitive data, consider disabling automatic redirects and manually validate the redirect location.
- **Use timeouts** to prevent denial‑of‑service scenarios in tests.

## Conclusion

The `requests` library provides a powerful, intuitive interface for HTTP communication, making it an essential component in any Python‑based automation testing framework. By following the practices outlined in this documentation—such as using sessions, handling errors gracefully, and incorporating robust assertions—test engineers can build reliable, maintainable, and scalable test suites. Whether you are testing REST APIs, downloading files, or simulating complex user interactions, `requests` offers the flexibility and performance required for professional‑grade automation.

For further details, consult the official `requests` documentation and explore advanced features like custom authentication, streaming uploads, and integration with popular testing frameworks like `pytest`.