def calculate_total(data,t_type):
    total=0
    for row in data:
        if row[2]==t_type:
            total+=float(row[0])
    return total
def calculate_category(data):
    a={}
    for row in data:
        if row[2]=="expense":
            category=row[1]
            amount=float(row[0])
            if category in a:
                a[category]+=amount
            else:
                a[category]=amount
    return a
    