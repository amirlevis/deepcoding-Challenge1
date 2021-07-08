from typing import List
import re

from masks.seekers import BaseSeeker


class TextMasker:
    def __init__(self, seekers: List[BaseSeeker], mask_char='X'):
        self.seekers = seekers
        self.mask_char = mask_char
        print(self.seekers)

    def mask(self, text: str) -> str:
        seekers_matches = [[match for match in seeker.seek(text)] for seeker in self.seekers]

        for seeker_matches in seekers_matches:
            print(seeker_matches)
            text = self.replace_text(text, seeker_matches)

        return text

    def replace_text(self, text, matches):
        for match in matches:
            text = text.replace(text[match.span()[0]:match.span()[1]],
                                re.sub("[^-._]", "X", text[match.span()[0]:match.span()[1]]))

        #print(text)
        return text
