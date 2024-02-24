import csv

dataP = [["id", "f_name", "l_name", "fam", "b_date", "b_place", "d_date", "d_place"]]
dataF = []
id, f_name, l_name, p_fam, b_date, b_place, d_date, d_place = (
    None,
    None,
    None,
    [],
    None,
    None,
    None,
    None,
)
prev_head = None
fam = None

with open("tree.ged", "r") as gedcom_file:
    for line in gedcom_file:
        line = line.strip()
        level = int(line[0])
        head = line[2:6].strip()
        value = line[6:].strip()

        if level == 0 and line[-4:] == "INDI":
            if id:
                dataP.append(
                    [id, f_name, l_name, p_fam, b_date, b_place, d_date, d_place]
                )
            id, f_name, l_name, p_fam, b_date, b_place, d_date, d_place = (
                None,
                None,
                None,
                [],
                None,
                None,
                None,
                None,
            )
            id = line[3:-6]

        elif level == 0 and line[-3:] == "FAM":
            fam = line[3:5]

        elif level == 1:
            if head == "SEX":
                sex = value
            elif head in ["NAME", "BIRT", "DEAT"]:
                prev_head = head
            elif head[0:3] == "FAM":
                p_fam.append(value[1:-1])
            elif fam and head in ["HUSB", "WIFE", "CHIL"]:
                dataF.append([fam, head, value[1:-1]])
            else:
                prev_head = None

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

with open("people.csv", "w", newline="") as csvfileP:
    csvwriter = csv.writer(csvfileP)
    csvwriter.writerows(dataP)

with open("families.csv", "w", newline="") as csvfileF:
    csvwriter = csv.writer(csvfileF)
    csvwriter.writerows(dataF)
# print(data)
