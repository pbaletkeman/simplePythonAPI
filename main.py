import requests
from requests.auth import HTTPDigestAuth
import argparse

params = {'key1': 'value1', 'key2': ['value2', 'value3']}
data = {'key1': 'value1', 'key2': ['value2', 'value3']}


def handle_results(url_params, form_data, verb="get", auth=""):
    sample_title: str = "get results"
    response = {}
    if verb == "post":
        response = requests.post('https://httpbin.org/put', params=url_params, data=form_data)
        sample_title = "post results:"
    if verb == "put":
        response = requests.put('https://httpbin.org/put', params=url_params, data=form_data)
        sample_title = "put results:"
    if verb == "delete":
        response = requests.delete('https://httpbin.org/delete', params=url_params, data=form_data)
        sample_title = "delete results:"
    if verb == "head":
        response = requests.head('https://httpbin.org/get', params=url_params, data=form_data)
        sample_title = "HEAD Results:"
    if verb == "options":
        response = requests.options('https://httpbin.org/get', params=url_params, data=form_data)
        sample_title = "Options Result:"
    if verb == "get":
        response = requests.get('https://httpbin.org/get', params=url_params, data=form_data)
        sample_title = "Get Result:"

    if auth == "basic":
        response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'), params=url_params, data=form_data)
        sample_title = " HTTP Basic Auth:"
    if auth == "digest":
        url = 'https://httpbin.org/digest-auth/auth/user/pass'
        response = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
        sample_title = "HTTP Digest Auth:"

    return sample_title, response


parser = argparse.ArgumentParser()
parser.add_argument("-verb", "--verb", help="HTTP Verb")
parser.add_argument("-payload", "--payload", help="'key1': 'value1'")
parser.add_argument("-data", "--data", help="'key2': 'value2'")
parser.add_argument("-auth", "--auth", help="Auth")

args = parser.parse_args()

print("---------------------------")
print("command line values:")
if args.verb:
    print("verb = " + args.verb)
if args.payload:
    print("payload = " + args.payload)
if args.data:
    print("data = " + args.data)
if args.auth:
    print("auth = " + args.auth)
print("---------------------------")

# install lib for http requests
# python -m pip install requests
# example command line
# python main.py -verb get --auth basic -payload {'name':'pete'} -data {'city':'toronto'}

title, r = handle_results(args.payload, args.data, args.verb, args.auth)
print(title)
print("status")
print(r.status_code)
print("headers")
print(r.headers)
print("body")
print(r.text)
print("as json")
print(r.json())
