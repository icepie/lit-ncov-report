# the platform url
hostname = "http://hmgr.sec.lit.edu.cn/wms"

# the main api
endpoints = {
    "login": hostname + "/healthyLogin",
    "lastRecord": hostname + "/lastHealthyRecord",
    "firstRecord": hostname + "/addHealthyRecord",
    "secondRecord": hostname + "/addTwoHealthyRecord",
    "thirdRecord": hostname + "/addThreeHealthyRecord",
    "getInstructor": hostname + "/getInstructor",
    "getFamilys": hostname + "/familys/personal",
    "getTrips": hostname + "/trips/personal",
    "getImportantCity": hostname + "/teamImportantCity",
    "queryRecord": hostname + "/healthyRecordByUser",
    "password": hostname + "/password",
    "unHealthyCount": hostname + "/dataV/countUnHealthy",
    "reportCount": hostname + "/healthyReportCount",
    "accessCertificateCount": hostname + "/dataV/countAccessCertificate",
    "isInTeamCityCount": hostname + "/dataV/countIsInTeamCity"
}


identitys = {
    "student": "1000401",
    "teacher": "1000402",
    "other": "1000405"
}