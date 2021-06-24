# the platform url
host = "http://hmgr.sec.lit.edu.cn"
muyunhost = host + "/web"
mainhost = host + "/wms"

# the main api
endpoints = {
    "login": mainhost + "/healthyLogin",
    "lastRecord": mainhost + "/lastHealthyRecord",
    "firstRecord": mainhost + "/addHealthyRecord",
    "secondRecord": mainhost + "/addTwoHealthyRecord",
    "thirdRecord": mainhost + "/addThreeHealthyRecord",
    "getInstructor": mainhost + "/getInstructor",
    "getFamilys": mainhost + "/familys/personal",
    "getTrips": mainhost + "/trips/personal",
    "getImportantCity": mainhost + "/teamImportantCity",
    "queryRecord": mainhost + "/healthyRecordByUser",
    "password": mainhost + "/password",
    "unHealthyCount": mainhost + "/dataV/countUnHealthy",
    "reportCount": mainhost + "/healthyReportCount",
    "accessCertificateCount": mainhost + "/dataV/countAccessCertificate",
    "isInTeamCityCount": mainhost + "/dataV/countIsInTeamCity"
}


identitys = {
    "student": "1000401",
    "teacher": "1000402",
    "other": "1000405"
}