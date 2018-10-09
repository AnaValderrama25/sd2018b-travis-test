def get_user_info(username=None):
    logging.debug(username)
    logging.info("Here it is user_info")
    return {"user_info": username}

def get_commits_info(username=None, time_range=None):
    logging.debug(username, time_range)
    logging.info("Here it is commits_info")
    return [{'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]
def get_health():
    logging.info("Here it health")
    return {"message" : "OK"}
