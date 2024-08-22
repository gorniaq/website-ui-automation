import logging

logging.basicConfig(
    # Set the logging level to INFO. This means that INFO, WARNING, ERROR, and CRITICAL messages will be logged.
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Specify the format for the log messages
)

# Create a logger object
# Get a logger instance for the current module. __name__ is the name of the module where the logger is used.
logger = logging.getLogger(__name__)
