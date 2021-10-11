"""
Writing the test case to print the error message along with time format
"""

import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',filename="test1.log",datefmt='%d/%m/%y %I:%M:%S %p %A',level=logging.DEBUG,filemode="w")

logging.info("This is info logging")
logging.error("This is a error log")
logging.debug("This is debug log")
logging.warning("This is warning log")
logging.critical("This is a critical log")