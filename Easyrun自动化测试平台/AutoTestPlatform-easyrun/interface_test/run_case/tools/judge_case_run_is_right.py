# coding=utf-8

def judge_case_run_is_right(expect_response,actual_response):
    if expect_response == actual_response:
        return 1
    else:
        return 0