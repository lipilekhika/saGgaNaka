from .kry import get_type
from typing import Union
import json
from requests import post, get
import subprocess as sub
from .file import write_bin


def minify_json(val: Union[dict, str]):
    """`val` is JSON Text or Object"""
    if get_type(val) == "str":
        val = json.loads(val)
    return json.dumps(val, ensure_ascii=False, separators=(",", ":"))


def minify_js(val: str, mode=1) -> str:
    if mode == 1:
        req = post(
            "https://www.toptal.com/developers/javascript-minifier/api/raw",
            data={"input": val},
        )
        if req.status_code == 200:
            return req.text
        print("some error in css minifier", req.status_code)
        req.close()
        return val
    if mode == 2:
        p = sub.Popen(
            "terser", stderr=sub.STDOUT, stdout=sub.PIPE, stdin=sub.PIPE, shell=True
        )
        return p.communicate(bytes(val, "utf-8"))[0][:-1].decode("utf-8")


def minify_css(val: str) -> str:
    req = post(
        "https://www.toptal.com/developers/cssminifier/api/raw",
        data={"input": val},
    )
    if req.status_code == 200:
        return req.text
    print("some error in css minifier", req.status_code)
    req.close()
    return val


def minify_html(val: str) -> str:
    req = post(
        "https://www.toptal.com/developers/html-minifier/raw",
        data={"input": val},
    )
    if req.status_code == 200:
        return req.text
    print("some error in html minifier", req.status_code)
    req.close()
    return val


def download_file(url: str, path=None):
    r = get(url, allow_redirects=True)
    if path == None:
        return r.content
    else:
        write_bin(path, r.content)


def generate_pydantic_data_model(val: dict, basemodel=False) -> str:
    res = post(
        "https://kr4ckp.deta.dev/",
        json={
            "data": minify_json(val),
            "options": {"forceOptional": False, "snakeCased": False},
        },
    ).json()["model"][36:]
    if not basemodel:
        res = res.replace(
            "from pydantic import BaseModel",
            "from pydantic.dataclasses import dataclass",
        )
        res = res.replace("(BaseModel)", "()")
        res = res.replace("\nclass ", "@dataclass\nclass ")
    return res
