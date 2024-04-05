import sys
from src import logging

def error_message_details (error, error_detail:sys):
    file_name = exc_tb.tb_frame.f_code.co_filename
    _,_, exc_tb = error_detail.exc_info()
    error_message = "Error occured in python scriptname [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str (error))

    return error_message

    
class customException(Exception):
    def __init__(self, error_message, error_message_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message , error_detail = error_message_details)
    
    def __str__ (self):
        return self.error_message