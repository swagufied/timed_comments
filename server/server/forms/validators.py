from server.utils.generic_utils import validate_host_from_url
from wtforms import ValidationError

def accepted_URL_hosts(form, field):
    print(field.data.strip())
    if not validate_host_from_url(field.data.strip()):
        raise ValidationError('You are attempting to make a comment on an unsupported site.')
    print ('url host validated')
