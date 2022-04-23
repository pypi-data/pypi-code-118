from omnitools import def_template, IS_WIN32, abs_dir
from subprocess import Popen, PIPE
from pathlib import Path
from .utils import ping
import threadwrapper
import threading
import requests
import random
import shutil
import yaml
import time
import json
import os


pkg_data_dir = os.path.join(abs_dir(__file__), "pkg_data")
SOURCE = "https://fq.lonxin.net/clash/proxies?type=ss"


class ShadowWalker:
    clash = None
    clash_port = 7890
    terminate = False

    @property
    def proxy(self):
        return "127.0.0.1:{}".format(self.clash_port)

    def __init__(
            self,
            clash_bin=os.path.join(pkg_data_dir, "clash.{}".format("exe" if IS_WIN32 else "bin")),
            exclude_country=["CN"],
            bench_file=os.path.join(pkg_data_dir, "bench.json"),
            proxies=None
    ):
        self.fast_proxy = [_[0] for _ in json.loads(open(bench_file, "rb").read().decode()).items() if _[1][0] and _[1][1] < 2.6]
        self.clash_bin = clash_bin
        self.exclude_country = exclude_country
        self.bench_file = bench_file
        self.proxies = proxies
        if not self.proxies:
            self.update_proxies()

    def clone(self):
        sw = ShadowWalker(
            proxies=self.proxies
        )
        sw.clash = None
        sw.clash_bin = self.clash_bin
        sw.exclude_country = self.exclude_country
        sw.bench_file = self.bench_file
        sw.clash_port = self.clash_port+10
        sw.fast_proxy = self.fast_proxy
        return sw

    def update_proxies(self):
        self.proxies = []
        for i in range(0, 10):
            try:
                print("\r", "fetching proxies, try {}/10".format(i+1), end="", flush=True)
                self.proxies = yaml.safe_load(requests.get(SOURCE, timeout=3).content.decode())["proxies"]
                break
            except:
                pass
        print("\r", end="", flush=True)
        self.test_latency(self.exclude_country)

    def start(self, quiet: bool = False, proxy: dict = None):
        if not self.proxies and not proxy:
            raise ValueError("empty proxies")
        if not proxy:
            if len(self.fast_proxy) > 1:
                proxies = self.fast_proxy
            else:
                proxies = self.proxies
            proxy = random.SystemRandom().choice(proxies)
            proxy = random.SystemRandom().choice(proxies)
        id = "{}_{}".format(proxy["server"], proxy["port"])
        config_fp = os.path.join(pkg_data_dir, "config_ss_{}_{}.yaml".format(self.clash_port, id))
        # os.makedirs(os.path.dirname(config_fp), exist_ok=True)
        # if os.path.isfile(config_fp):
        #     shutil.move(config_fp, config_fp+"."+str(int(time.time())))
        open(config_fp, "wb").write(('''\
port: {}
allow-lan: true
mode: rule
proxies:
  - name: "PROXY"
    type: ss
    server: "{}"
    port: {}
    cipher: {}
    password: "{}"
rules:
  - MATCH,PROXY
'''.format(
            self.clash_port,
            proxy["server"],
            proxy["port"],
            proxy["cipher"],
            proxy["password"],
        )).encode())
        print("clash using", proxy)
        print("starting clash")
        if not quiet:
            self.clash = Popen([self.clash_bin, "-f", config_fp], close_fds=not IS_WIN32)
        else:
            self.clash = Popen([self.clash_bin, "-f", config_fp], stdout=PIPE, stderr=PIPE, close_fds=not IS_WIN32)
        while not self.terminate:
            time.sleep(1)
        self.terminate = False

    def stop(self):
        if self.clash:
            print("clash terminating")
            self.terminate = True
            self.clash.terminate()
            print("clash terminated")
            self.clash = None

    def test_latency(self, exclude_country):
        print("clash testing latency, please wait")
        tw = threadwrapper.ThreadWrapper(threading.Semaphore(2**4))
        self.proxies = [_ for _ in self.proxies if _["country"][-2:] not in exclude_country]
        for i, proxy in enumerate(self.proxies):
            def job(i, proxy):
                print("\r", i+1, len(self.proxies), "pinging", proxy["server"], end="", flush=True)
                pings = [999]
                for i in range(0, 5):
                    p = ping(proxy["server"])
                    pings.append(p)
                    if p < 999:
                        break
                proxy["ping"] = min(pings)
                print("\r", i+1, len(self.proxies), "pinging", proxy["server"], proxy["ping"], end="", flush=True)
            tw.add(job=def_template(job, i, proxy))
        tw.wait()
        self.proxies = [_ for _ in self.proxies if _["ping"] <= 171]
        self.proxies = sorted(self.proxies, key=lambda x: x["ping"])
        self.fast_proxy = [_ for _ in self.proxies if "{}:{}".format(_["server"], _["port"]) in self.fast_proxy]
        print("\r", end="", flush=True)
        # print("\r", self.proxies)




