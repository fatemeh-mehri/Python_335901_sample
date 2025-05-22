import re

part_1 = 11
part_2 = "B"
part_3 = 123
part_4 = 11

def plate_generator(part_1, part_2, part_3, part_4):
    return f"{part_1}{part_2}{part_3}-iran{part_4}"

def plate_validator(plate):
    return bool(re.match(r"^\d{2}[a-z]\d{3}-iran\d{2}$", plate, re.I))


plate = plate_generator(part_1, part_2, part_3, part_4)
print(plate_validator(plate))


