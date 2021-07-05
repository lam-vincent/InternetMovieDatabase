def conversionHeureMinute(duree_minute):
    heure = duree_minute//60
    minute = duree_minute % 60
    return f"{heure}h{minute}"


def afficherCategories(categories):
    res = []
    for i in range(len(categories)):
        res.append(categories[i].name)
        res.append(", ")
    if len(res) >= 1:
        res.pop()
    if len(categories) > 1:
        res[len(res)-2] = " & "
    return "".join(res)
