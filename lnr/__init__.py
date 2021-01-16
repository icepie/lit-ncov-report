# the platform url
hostname = 'http://hmgr.sec.lit.edu.cn/wms'

# the main api
endpoints = {
    'lg': hostname + '/healthyLogin',
    'lr': hostname + '/lastHealthyRecord',
    'firstRecord': hostname + '/addHealthyRecord',
    'secondRecord': hostname + '/addTwoHealthyRecord',
    'thirdRecord': hostname + '/addThreeHealthyRecord',
    'gi': hostname + '/getInstructor',
    'fp': hostname + '/familys/personal',
    'tp': hostname + '/trips/personal',
    'ti': hostname + '/teamImportantCity'
}

# healthyRecordId=9037871&temperature=36.3&temperatureNormal=0
