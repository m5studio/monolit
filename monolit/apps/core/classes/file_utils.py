"""
    Some useful utilities to work with files
"""


class FileUtils:

    """ [ Convert bytes to readable formats ] """
    @staticmethod
    def format_bytes(bytes_num) -> str:
        sizes = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        dblbyte = bytes_num
        while (i < len(sizes) and  bytes_num >= 1024):
            # dblbyte = bytes_num / 1024.0
            dblbyte = bytes_num / float(1024)
            i = i + 1
            bytes_num = bytes_num / 1024
        return str(round(dblbyte, 2)) + " " + sizes[i]
