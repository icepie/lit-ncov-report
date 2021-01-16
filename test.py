from lnr.user import litUesr

test = litUesr("B19070404", "xxxxxx")
if test.is_logined:
    print(test.info)