from subprocess import run, PIPE
from omnitools import IS_WIN32
import shadowwalker
import threading
import requests
import time
import json


def ping(host):
    output = run("ping -{} 1{} {}".format(
        "n" if IS_WIN32 else "c",
        " -w 500" if IS_WIN32 else " -W 1",
        host
    ), shell=True, stdout=PIPE, stderr=PIPE, close_fds=not IS_WIN32)
    if IS_WIN32:
        try:
            # print(output.stdout.decode())
            # print(output.stdout.decode().splitlines()[2].split("ms")[0].split("=")[-1])
            return float(output.stdout.decode().splitlines()[2].split("ms")[0].split("=")[-1])
        except:
            return 999
    else:
        try:
            return float(output.stdout.decode().splitlines()[-1].split(" ")[-2].split("/")[0])
        except:
            return 999


def benchmark():
    sw = shadowwalker.ShadowWalker()
    bench = {}
    for i, proxy in enumerate(sw.proxies):
        sw.stop()
        time.sleep(1)
        p = threading.Thread(target=lambda: sw.start(proxy=proxy))
        p.daemon = True
        p.start()
        start = time.time()
        print(i + 1, len(sw.proxies))
        state = 0

        def job():
            nonlocal state
            r = requests.get("http://ipv4.download.thinkbroadband.com/10MB.zip", proxies={"all": sw.proxy}, timeout=5)
            if len(r.content) == 10 * 1024 * 1024:
                state = 1

        p2 = threading.Thread(target=job)
        p2.daemon = True
        p2.start()
        for j in range(0, 10):
            time.sleep(0.5)
            if state:
                break
        host = "{}:{}".format(proxy["server"], proxy["port"])
        bench[host] = [state, time.time() - start]
        print(i + 1, len(sw.proxies), *bench[host])
        open("bench.json", "wb").write(json.dumps(dict(sorted(bench.items(), key=lambda x: x[1][1]))).encode())
        sw.stop()

