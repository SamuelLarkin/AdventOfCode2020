#!/usr/bin/env  python3

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

PASSPORT_FIELDS = frozenset(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))


def passport_gen():
    with open('input', 'r') as f:
        passport = dict()
        for l in f:
            l = l.strip()
            if l == '':
                yield passport
                passport = dict()
            else:
                #passport.update( { k: v for e in l.strip().split() for k, v in e.split(':') } )
                for e in l.split():
                    k, v = e.split(':')
                    passport.update({k: v})

    yield passport



def valid_passport(passport: dict) -> bool:
    return len(set(passport.keys()) & PASSPORT_FIELDS) == len(PASSPORT_FIELDS)





if __name__ == '__main__':
    passports = list(passport_gen())
    print(len(passports))
    print(passports[-1])

    num_valid = len(list(filter(valid_passport, passports)))

    # 239
    print(f'Answer: {num_valid}')
