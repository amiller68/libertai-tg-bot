import logging

# Define the logger
LOGGER_NAME = __name__

# TODO: Replace with a more observable solution that utilizes proper tracing and spans
# TODO: Figure out a solution that lets me utilize different logging formats in different contexts

# Custom Chat Log Formatter
# Used to trace events that span the handling of a message within a chat
class ChatLogFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, 'chat_id'): 
            record.chat_id = record.chat_id
        
        if hasattr(record, 'message_id'):
            record.message_id = record.message_id

        return super().format(record)

class Logger:
    logger: logging.Logger
    
    def __init__(self, log_path=None, debug=False):
        '''
        Initialize a new Log instance
        - log_path - where to send output. If `None` logs are sent to the console
        - debug - whether to set debug level 
        '''

        # Create the logger
        logger = logging.getLogger(LOGGER_NAME)
        # Set the log formatter
        formatter = ChatFormatter('%(asctime)s - %(name)s - %(levelname)s - %(chat_id)s - %(message_id)s - %(message)s')

        # Set our debug mode
        if debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

        # Set where to send logs
        if log_path:
            handler = logging.FileHandler(log_path)
            handler.setFormatter(formatter)
        else: 
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
        
        
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(handler)

        self.logger = logger

    def debug(self, message, chat_id=None, message_id=None)
        extra = {}
        if chat_id:
            extra['chat_id'] = chat_id
        if message_id:
            extra['message_id'] = message_id

        self.logger.debug(message, extra=extra)
    
    def info(self, message, chat_id=None, message_id=None)
        extra = {}
        if chat_id:
            extra['chat_id'] = chat_id
        if message_id:
            extra['message_id'] = message_id

        self.logger.info(message, extra=extra)

    def error(self, message, chat_id=None, message_id=None)
        extra = {}
        if chat_id:
            extra['chat_id'] = chat_id
        if message_id:
            extra['message_id'] = message_id

        self.logger.error(message, extra=extra)