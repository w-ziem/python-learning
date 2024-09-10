import logging
# import  logging.config

# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger('helper') #z configa


# logging.debug('DEBUG message')
# logging.info('INFO message')
# logging.warning('WARNING message')
# logging.error('ERROR message')
# logging.critical('CRITICAL message')



try:
    a = [1,2,3]
    val  = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)