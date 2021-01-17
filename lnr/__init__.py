# the platform url
hostname = 'http://hmgr.sec.lit.edu.cn/wms'

# the main api
endpoints = {
    'login': hostname + '/healthyLogin',
    'lastRecord': hostname + '/lastHealthyRecord',
    'firstRecord': hostname + '/addHealthyRecord',
    'secondRecord': hostname + '/addTwoHealthyRecord',
    'thirdRecord': hostname + '/addThreeHealthyRecord',
    'getInstructor': hostname + '/getInstructor',
    'getFamilys': hostname + '/familys/personal',
    'getTrips': hostname + '/trips/personal',
    'getImportantCity': hostname + '/teamImportantCity'
}

# healthyRecordId=9037871&temperature=36.3&temperatureNormal=0
