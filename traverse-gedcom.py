data = []
id, f_name, l_name, b_date, b_place, d_date, d_place = (
    None,
    None,
    None,
    None,
    None,
    None,
    None,
)
prev_head = None

with open("tree.ged", "r") as gedcom_file:
    for line in gedcom_file:
        line = line.strip()
        level = int(line[0])
        head = line[2:6].strip()
        value = line[6:].strip()

        if level == 0 and line[-4:] == "INDI":
            if id:
                data.append([id, f_name, l_name, b_date, b_place, d_date, d_place])
            id, f_name, l_name, b_date, b_place, d_date, d_place = (
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            )
            id = line[3:-6]

        elif level == 1:
            if head == "SEX":
                sex = value
            elif head in ["NAME", "BIRT", "DEAT"]:
                prev_head = head

        elif level == 2:
            if prev_head == "NAME":
                if head == "GIVN":
                    f_name = value
                elif head == "SURN":
                    l_name = value
            elif prev_head == "BIRT":
                if head == "DATE":
                    b_date = value
                elif head == "PLAC":
                    b_place = value
            elif prev_head == "DEAT":
                if head == "DATE":
                    d_date = value
                elif head == "PLAC":
                    d_place = value


print(data)
