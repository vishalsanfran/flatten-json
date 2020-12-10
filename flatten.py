#!/usr/bin/env python
import json
import sys

# Recursive backtracking implementation to flatten a json

def flatten(obj):
    res = {}
    rec(obj, "", res)
    return res

def rec(obj, cur, res):
    if len(cur) > 0 and len(obj) == 0:
        res[cur] = None

    for k, v in obj.items():
        new_key = k if len(cur) == 0 else cur+'.'+k
        if type(v) == dict:
            rec(v, new_key, res)
        else:
            res[new_key] = v

if __name__ == '__main__':
    data = sys.stdin.read()
    print(flatten(json.loads(data)))