from oslo_service import service
from oslo_log import log as logging
from oslo_config import cfg

from myservice.service import MyService
from myservice.config import register_opts, CONF

def main():

    # Register logging options FIRST
    logging.register_options(CONF)

    # Register service options
    register_opts()

    # Parse configuration
    CONF(
        default_config_files=['myservice.conf']
    )

    # Setup logging AFTER parsing
    logging.setup(CONF, "myservice")

    # Launch service
    launcher = service.launch(CONF, MyService())
    launcher.wait()

if __name__ == "__main__":
    main()
