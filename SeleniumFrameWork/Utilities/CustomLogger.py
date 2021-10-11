import inspect
import logging

def customLogger():
    #1.This is use to get the class/method name from where this cutomLogger method is called
    logName=inspect.stack()[1][3]

    #2.Create the logging object and pass the logName in it
    logger=logging.getLogger(logName)

    #3.Set the loglevel
    logger.setLevel(logging.DEBUG)

    #4.Create the filehandler to save the logs in the file
    fileHandler=logging.FileHandler("../reports/test.log",mode="a")

    #5.set the loglevel for fileHandler
    fileHandler.setLevel(logging.DEBUG)

    #6.Create the formatter in which format do you like to save logs
    formatter=logging.Formatter('%(asctime)s - %(name)s :%(levelname)s :%(message)s :',datefmt='%d/%m/%y %I:%M:%S %p %A')

    #7.Set the formatter to fileHandler
    fileHandler.setFormatter(formatter)

    #8.Add file handler to loggin
    logger.addHandler(fileHandler)

    #9. Finally return the logging object
    return logger
