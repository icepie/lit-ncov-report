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
}
