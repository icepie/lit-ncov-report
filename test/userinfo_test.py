from litncov.user import litUesr

testme = litUesr("B19070404", "xxxxxx")
if testme.is_logged:
    print(testme.info)
    print(testme.get_last_record())
    print(testme.get_instructor())
    print(testme.get_familys())
    print(testme.get_trips())
    print(testme.get_important_city())
    if not testme.is_record_today(1):
        print(testme.first_record(mode="last", rtimes=1))
    if not testme.is_record_today(2):
        print(testme.second_record(mode="manual", temperature=36.6))
    if not testme.is_record_today(3):
        print(testme.third_record(mode="random"))
