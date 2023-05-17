STATUS_OK=200
STATUS_FAILED = 400


def data(data):
    dic = {}
    response = {}
    response['response_Data'] = data
    response['status_code'] = STATUS_OK
    dic['status'] = 1 
    dic['success'] = response
    return dic

def error(error_msg):
    dic = {}
    response = {}
    response['message'] = error_msg
    response['status_code'] = STATUS_FAILED
    dic['status'] = 0 
    dic['error'] = response
    return dic

def failed(error_msg):
    dic = {}
    response = {}
    response['message'] = error_msg
    response['status_code'] = STATUS_FAILED
    dic['status'] = 0 
    dic['failed'] = response
    return dic

def success(success_msg):
    dic = {}
    response = {}
    response['messsge'] = success_msg
    response['status_code'] = STATUS_OK
    dic['status'] = 1 
    dic['success'] = response
    return dic