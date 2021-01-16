from lnr.user import litUesr

testme = litUesr("B19070404", "xxxxxx")
if testme.is_logined:
    print(testme.info)
    print(testme.get_last_record())
    print(testme.get_instructor())
    print(testme.get_familys())
    print(testme.get_trips())
    print(testme.get_important_city())
    print(testme.first_record(mode='manual', times=1))
    print(testme.second_record(mode='manual', temperature=36.6))
    print(testme.third_record(mode='random'))