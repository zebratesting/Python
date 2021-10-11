import logging
import PythonLogging.CustomLogger as  cl

class CustomLoggerDemo():
    log=cl.customLogger()

    def metodOne(self):
        self.log.critical("This is Critical")
        self.log.debug("This is debug")
        self.log.error("This is error")
        self.log.warning("This is Warning")
        self.log.info("This is info")

    def methodTwo(self):
        m2=cl.customLogger()
        m2.critical("Critical")
        m2.info("info")
        m2.debug("Debug")
        m2.warning("warning")
        m2.error("error")


cld=CustomLoggerDemo()
cld.metodOne()
cld.methodTwo()