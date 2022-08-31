def to_dict(res:str):
    res_dict = {}
    resquest = res.split("&")
    resquest.pop()
    for res in resquest:
        res_dict[res.split("=")[0]] = res.split("=")[1].replace("+"," ")

    return res_dict