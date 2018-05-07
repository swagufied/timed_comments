from server.constants import accepted_URL_hosts

def remove_substrings_in_string(input_string, substrings):
    for substring in substrings:
        input_string = input_string.replace(substring, '')
    return input_string


def determine_host_from_url(url):
    url = remove_substrings_in_string(url, ['http://','https://'])
    split_url = url.split('.')
    print(split_url)
    return split_url[1]

def validate_host_from_url(url):
    try:
        print(accepted_URL_hosts)
        return determine_host_from_url(url) in accepted_URL_hosts
    except Exception as e:
        print(e)
        return False
