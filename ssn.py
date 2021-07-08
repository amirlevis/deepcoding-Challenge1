import re


def mask_ssn(text):
    ssn_regex = re.compile(r'(\d\d\d)-(\d\d)-(\d\d\d\d)|(\d\d\d\d\d\d\d\d\d)')
    for word in text.split(' '):
        # print(word)
        mo = ssn_regex.search(word)
        if mo is not None:
            print(mo.groups())
        print(mo)


def validate_ssn(ssn):
    pass
