import re, os, sys


def slugify(s):
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")


def ParseKV(Line):
    D = {}
    for p in Line.split(";"):
        if p == "": continue
        if "=" in p:
            k = p.split("=")[0]; v = p.split("=")[1]
            D[k.strip()] = v.strip()
        else:
            pass
    return D
