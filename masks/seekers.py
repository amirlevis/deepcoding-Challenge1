from typing import Generator
import re
import pandas as pd

CSV_FILENAME = 'names.csv'
CHUNK_SIZE = 10 ** 6

class BaseSeeker:

    def seek(self, text: str):
        raise NotImplementedError("Must be implemented in derived classes")

    def validate(self):
        raise NotImplementedError("Must be implemented in derived classes")


class NameSeeker(BaseSeeker):


    def __init__(self):
        #self.df = pd.read_csv(CSV_FILENAME, usecols=['firstname'])

        with pd.read_csv(CSV_FILENAME, chunksize=CHUNK_SIZE) as reader:
            for chunk in reader:
                print(chunk)
                self.df = chunk

        #print('a', self.df.memory_usage())
        self.regex = re.compile((
            "[A-Za-z]{2,25}([A-Za-z]{2,25})?"), re.UNICODE)

    def seek(self, text: str) -> Generator[str, None, None]:
        for match in self.regex.finditer(text):
            name = match.group().strip()
            if (self.df['firstname'] == name).any():
                yield match

    def validate(self):
        pass


class SSNSeeker(BaseSeeker):
    def __init__(self):
        self.regex = re.compile((
            r"[0-9][0-9][0-9]"  # first three digits
            r"[\-._ ]"  # separator
            r"[0-9][0-9]"  # next two digits
            r"[\-._ ]"  # separator
            r"[0-9][0-9][0-9][0-9]"  # last four digits
        )
            , re.VERBOSE)

    def seek(self, text: str) -> Generator[str, None, None]:
        for match in self.regex.finditer(text):
            ssn = match.group().strip()
            yield match

    def validate(self, ssn) -> bool:
        return True
