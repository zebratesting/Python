"""Logging means tracking the event or steps during the execution of program or software

LogLevel

============================
Critical,
Error,
Debug,
INFO,
Warning

By default info and debug logs won't be printed in console need to use basicConfig

We can use filename to save the logs the specific file
"""

#To get the logs we need to import logging module



import logging

logging.basicConfig(filename="test.log",level=logging.DEBUG)

logging.info("This is info logging")
logging.error("This is a error log")
logging.debug("This is debug log")
logging.warning("This is warning log")
logging.critical("This is a critical log")







