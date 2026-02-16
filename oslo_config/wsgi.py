from oslo_log import log as logging
from myservice.config import register_opts, CONF
from myservice.api import simple_app

# Register logging + service options
logging.register_options(CONF)
register_opts()

# Parse config
CONF(default_config_files=['myservice.conf'])

# Setup logging
logging.setup(CONF, "myservice")

application = simple_app
