from SeleniumFrameWork.Base.BasePage import BaseClass

class ContactForm(BaseClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
