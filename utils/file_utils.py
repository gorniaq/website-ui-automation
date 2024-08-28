import os
import time
import logging


class FileUtils:

    @staticmethod
    def get_download_dir():
        """
        Returns the path to the Downloads directory based on the operating system.
        Returns:
            str: The path to the Downloads directory.
        """
        if os.name == 'nt':  # Windows
            return os.path.expanduser('~\\Downloads')
        else:  # Linux, macOS
            return os.path.expanduser('~/Downloads')

    @staticmethod
    def verify_file_download(expected_file_name):
        """
        Verify that the expected file has been downloaded to the default download directory.
        Args:
            expected_file_name (str): The name of the file expected to be downloaded.
        Raises:
            AssertionError: If the expected file is not found within the timeout period.
        """
        file_found = False
        # Record the start time of the verification
        start_time = time.time()
        # Get the path to the download directory
        download_dir = FileUtils.get_download_dir()

        # Wait up to 60 seconds for the file to appear in the download directory
        while time.time() - start_time < 60:
            # List all files in the download directory
            files = os.listdir(download_dir)
            for file in files:
                # Check if there is a file with a .pdf extension and the expected file name
                if file.endswith(".pdf") and expected_file_name in file:
                    logging.info(f"Downloaded file found: {file}")
                    file_found = True
                    break
            if file_found:
                break

        return file_found
