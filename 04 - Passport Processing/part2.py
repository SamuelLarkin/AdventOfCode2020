#!/usr/bin/env  python3

import re

from part1 import passport_gen
from part1 import valid_passport as all_fields_present


"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

def valid_birth_year(year: int) -> bool:
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    """
    return 1920 <= year <= 2002


def valid_issue_year(year: int) -> bool:
    """
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    """
    return 2010 <= year <= 2020


def valid_expiration_year(year: int) -> bool:
    """
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    """
    return 2020 <= year <= 2030


def valide_height(height: str) -> bool:
    """
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    if height.endswith('cm'):
        return 150 <= int(height[:-2]) <= 193
    elif height.endswith('in'):
        return 59 <= int(height[:-2]) <= 76
    else:
        return False


def valid_hair_color(color: str) -> bool:
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    return re.match(r'^#[0-9a-f]{6}$', color) is not None


def valid_eye_color(color: str) -> bool:
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    return color in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def valid_pid(pid: str) -> bool:
    """
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    return re.match(r'^[0-9]{9}$', pid) is not None



def valid_passport(passport: dict) -> bool:
    """
    All field except cid are present
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    return \
            all_fields_present(passport) \
            and valid_birth_year(int(passport['byr'])) \
            and valid_issue_year(int(passport['iyr'])) \
            and valid_expiration_year(int(passport['eyr'])) \
            and valide_height(passport['hgt']) \
            and valid_hair_color(passport['hcl']) \
            and valid_eye_color(passport['ecl']) \
            and valid_pid(passport['pid'])





if __name__ == '__main__':
    passports = list(passport_gen())
    print(len(passports))
    print(passports[-1])

    num_valid = len(list(filter(valid_passport, passports)))

    # 188
    print(f'Answer: {num_valid}')
