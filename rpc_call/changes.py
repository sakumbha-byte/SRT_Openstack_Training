#added this in nova/nova/compute/rpcapi.py
def sync_hello(self, ctxt, instance, message):
    version = '6.5'
    cctxt = self.router.client(ctxt).prepare(
        server=_compute_host(None, instance),
        version=version)
    return cctxt.call(ctxt, 'sync_hello',
                      instance=instance,
                      message=message)

def async_notify(self, ctxt, instance, message):
    version = '6.5'
    cctxt = self.router.client(ctxt).prepare(
        server=_compute_host(None, instance),
        version=version)
    cctxt.cast(ctxt, 'async_notify',
               instance=instance,
               message=message)




#added this in nova/nova/compute/manager.py
def sync_hello(self, context, instance, message):
    LOG.info("SYNC HELLO received on compute: %s", message)
    return "Reply from compute"

def async_notify(self, context, instance, message):
    LOG.info("ASYNC HELLO received on compute: %s", message)
