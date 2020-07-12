from flask import request


def query_param(name): return request.args.get(name)
