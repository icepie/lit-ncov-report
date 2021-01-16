# the platform url
hostname = 'http://hmgr.sec.lit.edu.cn/wms'

# the main api
endpoints = {
    'lg': hostname + '/healthyLogin',
    'lr': hostname + '/lastHealthyRecord',
    'ar': hostname + '/addHealthyRecord',
    'gi': hostname +'/getInstructor',
    'fp': hostname + '/familys/personal',
    'tp': hostname + '/trips/personal'
}