from oslo_log import log as logging
from myservice.config import CONF

LOG = logging.getLogger(__name__)

def simple_app(environ, start_response):
    LOG.info("API request received")

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)

    message = CONF.greeting
    return [message.encode()]
