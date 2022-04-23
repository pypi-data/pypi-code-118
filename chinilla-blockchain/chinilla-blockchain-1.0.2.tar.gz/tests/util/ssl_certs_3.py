from typing import Dict, Tuple

SSL_TEST_PRIVATE_CA_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUeLxDdxR+RmiMMvvCxRfsQJAL7vUwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMB4XDTIyMDMyMzE3MjkyM1oXDTMyMDMy
MDE3MjkyM1owRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8G
A1UECwwYT3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEA0Bvshi5y4VEw+k32NOOMFZJaraLoJx5N1WOJDYGqSDPe
7ICPjz4IWDQN+yPrFv+ms+es3Ys8WOKEOMWR8U9mAxG21t+n8LH7NAMlCRNscBZ/
Si04bqfrBc3adznorQLtShOpYxEfRdu7kpHo6+D+4Av96qMpMLsPKiZWjjy9O3ai
oNzymj0mwlZ/1gaxpvfmvuqNNR9Kog8o7crLbp/x0ZPiU+Q0y6Kj4saZwu5Nq2cO
JqLn6ex8w576/UOAN4u28S3m2pVgoYkqGqJSXORUqZj38Ro0zAYywIHjiIfhLp5a
dhqDyf/IUCawltEzdXoOp3irYaV0SmAB8+e2ILZJawIDAQABoxMwETAPBgNVHRMB
Af8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQAchOBNfaAIoP97Lmyk/S4Hu94I
bGqj/BT6/q+UnWYcIt3UO6/d9a6WO7xtSPKiuObip8M6UQYVKQC8YecnAvXFwI6Q
r4z2TdGx2MjsxfQSNX0BYASlv5EWd3LYJs+Ayi2lxh+3XLSH+BK/7R1nL1MaN161
vAN2rGOo5J1niWyixyGK/jrKTtsRTxDcpFeIYdk1r/qGiY5uxwg6ny0JYHXYhSNm
AyADKnZoXw/kb6+mEHJHZaTR1JpNHkQ7azhNYyVMUseCi+5vYuzA2OoxSgBegSj+
1fRUZI+j46hkr5Qspw9P++dDLzEGgarbxruRf6VsosU3sSYxq6LC+a9UHXNG
-----END CERTIFICATE-----
"""

SSL_TEST_PRIVATE_CA_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA0Bvshi5y4VEw+k32NOOMFZJaraLoJx5N1WOJDYGqSDPe7ICP
jz4IWDQN+yPrFv+ms+es3Ys8WOKEOMWR8U9mAxG21t+n8LH7NAMlCRNscBZ/Si04
bqfrBc3adznorQLtShOpYxEfRdu7kpHo6+D+4Av96qMpMLsPKiZWjjy9O3aioNzy
mj0mwlZ/1gaxpvfmvuqNNR9Kog8o7crLbp/x0ZPiU+Q0y6Kj4saZwu5Nq2cOJqLn
6ex8w576/UOAN4u28S3m2pVgoYkqGqJSXORUqZj38Ro0zAYywIHjiIfhLp5adhqD
yf/IUCawltEzdXoOp3irYaV0SmAB8+e2ILZJawIDAQABAoIBAQCDVHvpGbrpsiEk
dLqhGdA3dMrAtQOoXBlmRpAg8+kP85wEyATQsqb1crQ3/qzHMMJ02glfLhUBSsGC
SjwVerO30CAAbdg/rzIF2s4uchGGksv1daAdRN6uJQBvKR5KwIQasVm96PpBTa+L
iYTiBnUR0r+EqT6/P+0L/nG1BWOt98bITaxO5Cn2mXGP1ZZ8iA9RBx1pxMAUDG4d
5Y4+Xt8YMP8OfEeVIFO/djRTh0OSTugSGwjnJReF+clX19+dJ/aBXOUHrLdNCV8c
9GjqHDEy6rXIb9N8UY6nVVvzbC/ypY6k2VtDhnWUYaLcpuHekmrONJRKXc0lKR6w
8FDACpvhAoGBAOi72c+PH0FjT2pyVQLc/Ht5UDt0jvsGPEa+EvYYC+ZFEViXj98+
KGxtIrc6Jab3Si/eCMS+qPAO3F8wC1J+qHq34g6B2v2SH3d5KOWXZwMFkEcM3psO
xBawVtH5suhTK86Lq/qi2EE5yT0NNlM+NM8zyhYtm/w8kjnly/5J53DTAoGBAOTp
3+mvSyah3pBTDHLlLUw92baOAQRMR+7DHOmtsyVwzbZXzES1IVMt02ZH5FNN2nk7
8XUldTNUkvnHPrGVogI3d8DlWctfh7ri0T9SgydudIOP9ETmdr379uepAHQavE8q
fyxi5o1Ypp69rPWZWmicTbiNyhAoTqFhauA7XCYJAoGAayDlLuSLl5a2HKKKPSop
0lBSPTv3ANeq8UlXAw6ok5NhW61QXYuIIfjOjRbn9AZKkOQclyvIKdA9YleELrH8
rZhtJw5hFm2nrGAKEjzx/vMVqY7j/O38FxGOtVLCJqz6MjYasOE6uDN4TXECe6jb
uDD3qePOtHnROXNsxh2Qul8CgYAq87tA9NRMDmldeUfHszrZqG1WdLS6IroIkfG1
4xLPPqhKw5Sfe8EiA2I8Odcczmnk/5th2MJx/DeLyJf56FK6yb+doStFHsqwBWkv
0YKsfmw8V2GFIB09rq54b1yXbIDS9e1g3bnW4cB53qs6dijhohpvO6OjfnyqiUXt
hxXWSQKBgA//yaex8PP/QQNzTYVgFGLmy+TuI7rbrVtVRs1tUzpitzL66Cd4qdL5
qKeMxbohv6aeXDYQweemm5QFvrP63syIyphe/ZPwF5q7V5ZtFwUVwXYW96hwRdVk
lA+tw7ba6RnXdDI+i2PoHfmdP89WJWeucidP8VcmhY0RiAYpG/vd
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUFhEfo/xtdcjm/XhkbuouJaZUBEAwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDQEygAVJgviM/8f0wuEsmCJoiNJ3gvrX8EckcllVXeyg23
iXiIadXqtCdPOXQlJHw2fZ838o/WuJkI9TsrtUkG3e+VEJKku3GtDez7gDufVZd9
e7jmqbO1mMwvpbFwEUzR9IumsxiOqDVAzSJIJGnWKhiOLYkXdKI4D+dyniEMKVFk
Y1TcI1huQngH+dBYujHlJZ4USOB+xVv5LfgrKYiZyHdKmRchIdhcjft5b7gBp38z
helydqA+mEU8zFqL5iwpNOALmije5IQKDrVHThIVmlg+G96DakoVBcpEqttfHb0N
E/oX3v0yAeV6IJ94VwCsSzndHt/KEG5PjsqQ60KHAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB63tKOcuBjL8tjnIlDozpm
t+LRcNiubKRc/rhTBYIoO6cTMN61ITe2FvogzNAPR/wmsaDO/sqG1oEHrrnJ7hXi
zNVj3GC7XYlqXvoRsCTdqoZE4ATPVZkJqhDx+/5IruWo1Q7F3nPzjLcS3mpwu2xc
Tl2HBEwCX2gTuG6lB5DUztrgGLNh27pqRLoGW4fzmVtHD/z54SFsQvPw0flYMRtc
qA/4eoWLvQNGoqsfA2F+eFTlXiPr/jp3jFVJvqixlwEN1DJkTi7hfMTEty7xrlZq
dZUmYxygqt4sy0AMbwCbemYJmvONlW8lN5GYo5NjB0BaMYsGMrehY2XHZg2npy+U
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA0BMoAFSYL4jP/H9MLhLJgiaIjSd4L61/BHJHJZVV3soNt4l4
iGnV6rQnTzl0JSR8Nn2fN/KP1riZCPU7K7VJBt3vlRCSpLtxrQ3s+4A7n1WXfXu4
5qmztZjML6WxcBFM0fSLprMYjqg1QM0iSCRp1ioYji2JF3SiOA/ncp4hDClRZGNU
3CNYbkJ4B/nQWLox5SWeFEjgfsVb+S34KymImch3SpkXISHYXI37eW+4Aad/M4Xp
cnagPphFPMxai+YsKTTgC5oo3uSECg61R04SFZpYPhveg2pKFQXKRKrbXx29DRP6
F979MgHleiCfeFcArEs53R7fyhBuT47KkOtChwIDAQABAoIBAE6dPjrJu2oSPcq/
ac/qhznmRydVp0IUQe4zIxBfGL+BBae3h9O6cPkpMcTsBybVXxzTX6mquo+81Q0e
YknER6ARkCh4x3731x40KbpoG566nu7pJNX5fg15eoPyDVUzJBwbUfwcpIWZpe0i
0/X/1AD3jKmDKM204mleEOssNX47G7z5GlLY73hRN93+LAFmiVzIRsNAmkgEOVKV
NI7kj4Eax+1i6LfU5EeSi5XbqaEopWyxuUg/WtNFJzaTtVSnZMqUvMS7R0b3hWqL
KeJCe+H5JXn/GUUiHUcKaFW4yTXLEGMOSXrxevEUt/+PwEKByVIa3Y3ljVh4eHMg
eSykGAkCgYEA6WiLDxSPmSYzQRHkD968bztk0x/XSEbCoJdS8msGjwApJ7eZbLBz
hW+4k/HhIPez0atU2TBm6XR3YauWxtu+p93KjvqieMHgudZ95+4hK3jkUTpnN4Lx
MNfZsEsUpiZ34kv8sjJxr56gWPBdMUdyAorRqeQGYua3Ddg6nLFXbZUCgYEA5Dbk
PewvLZLX7lbN7Y7r+uSLIOq2CuQLMirLuDKooaQFLdjhbxZqpQ1UlLIb7V66PVTW
TJCWr9M3btWMwUSvWquyCJi0ppwCRB3JOiO66eUqUwjT6gv8jXy9HDJLRc8jHjbF
Xvr+g2IxPr7tpVClBIq+NJnP0vAhPN0DGVGM0KsCgYAEo/53y0nbmqXUOl3VbvFC
KOUlSXHHTxjZhoiwpy4XM8KdtonHXm69jW4XCu0V8bbSiVyDgPHa3GTvPTEfPQk6
Xy+CzjriucAVEc2pCdQBAENR1h5tPR48gV4joiqD7yndBvO8O0KFYlr/ya+gpjH/
GPF4Nj9mQf4LuWvY57G8TQKBgQCAfZNmdeteKnZfIAqTvUuKGFFpOB1E5n6TQVsw
G32sfK/Zz2ml5SYoReggTGPC8vnC/FgoBaSB3FcylRPJ4UUltNPpWSklQWNZPLgG
fwWHGVsKI0dFWHhapSfIj1yoMmbgZRAdWQ4hpRB69n7Q/CXc98z9yrgjWMYuAXX0
NGEnPwKBgDpMnmFVf9YqtIrjb2dfUFXi/xRM/0C5/fKOxLdMAqelQrHUCzkfjnq5
sRf+TU0gV63g0vmDkrHPDew7NAr8m/cehPgELvtBvouEbGNQOuvNDunVwLU6vaIh
OqtmlgNu99SfZUJUg8pIOD2oAJKSSg+iw11bnPuKJxPyWd9HtMZl
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUO/5znSza9Dx7FlysyCyStw2FDwQwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDFUvDaklLh3JqASKA1I6H/cULbcPCiXDy5CTtXJUzSRc8Q
ckjI4pepWm2/qPKkmiW+6V3irdc1sGF5ICB0mh41UAu5338+0nuQ2n6LWChL4OG7
JNU4uBIbf5PXmlZhj8BHAfpAi0rvXIdlEUyVhDnjfnOnYK/2Eivh5gOvnmoHA9EA
BI1KCvhIdv9H4Vdrl+iFTL42hPe1X4TBRcg7HuFVZ14kzxWQ4x9Ep/tzzq8eaLSM
rlrRmBlrXMgN66ib65deEbuGPxVdHwY4OkR7hxal41ON6sduZ7d5ypHWGUwrT0eY
Pga4/b10/trBHGlk7cFmLmqTDVEtPMgrHFrtM4YJAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAk17NlkhSre6JbKzlUdYB4
GOddsueSKsnathkvevXLM5Q2zhY1GKdeT6chlflcgLs1q810LwyAvVD/A5k3jOZM
YxR9mQMAARuk1qZsxeYfu1ARZWEU77HJj2foWw0r5+1FmT5vCPZoqnINElXHMbuy
DtgYUjAS/31pqHtFKrqFAV3IruQyosYoVOFmKb419s+7ST6u+FQZpiouKKnSpqfc
0K9+O4pcCvPgcrj8rTK5cxLeIYd7LwL9grxE9DrIJhsaoKUkwM4+tiimr+7OSYov
byhFnXiLH9MEZgJXtV9jwQJideTpcI7rdVFVc4+tEP9A5Prru6asNC2UsXbg4kZy
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAxVLw2pJS4dyagEigNSOh/3FC23Dwolw8uQk7VyVM0kXPEHJI
yOKXqVptv6jypJolvuld4q3XNbBheSAgdJoeNVALud9/PtJ7kNp+i1goS+DhuyTV
OLgSG3+T15pWYY/ARwH6QItK71yHZRFMlYQ5435zp2Cv9hIr4eYDr55qBwPRAASN
Sgr4SHb/R+FXa5fohUy+NoT3tV+EwUXIOx7hVWdeJM8VkOMfRKf7c86vHmi0jK5a
0ZgZa1zIDeuom+uXXhG7hj8VXR8GODpEe4cWpeNTjerHbme3ecqR1hlMK09HmD4G
uP29dP7awRxpZO3BZi5qkw1RLTzIKxxa7TOGCQIDAQABAoIBADJ/m2wUbmmnD1Mt
QvLWf6rjzXxjVvH2MQQZvLn8rcBSZT+MP9xJQQ7yOYwHLLG7UVWeW4ybeKwgy5E4
C5ZLqtdx+M5EyEfHjh/wCtqWYRmqH5rJPlgZo2iuKaPPt7OYGlkRxH2oKDFBuNTA
rJzHDhmOTwLS17VdySUyvFbBb9kDSQwaH04yRhsGoMuy+qmBc75eOCl6FtOFHtJ4
7EjdnpRp6L6lKU/pMflVx3kwepAjGul+xZXhkXdfyLfGsAVsZQwePiq8aMZ/S/Gj
yqrCMQ+EqeTb57SSXWK9XYrOIsQZSJjuqiOOYgqKofv7HqJlmC1cLhgoMG5o0jP2
bTKvOxECgYEA/0ythY6A5KxT06gdYltsMlIcuamVw5EjoDpf8oyBwD6cbUm8Mb2t
VOtPbbHxx4NqGSn/uxT8UgmOGZ4C04CwmgWmMmODCT/c9LBHNbWOTiy4OLIJdcUv
01x1tYZvdbe1FYKxga+hR+UnKJT1t0m5UjKjhXnIYGR+weXpm2hco2sCgYEAxd2K
ggTm/xNtDHNxjygKik4FfEhGcgafnpCrm6dCGyLAe5+T9YOt6owGTS2AiJiG5PJR
GmJxyJa44je/r1+LLVN8SmsLXTX74UizjoVNaCoy9Ze3Xb4RNsPYXe0wIgCi+hBP
PEmFZvSxlxXpHP0ppknCxI08wBWXH6goSkcrDVsCgYAx/69gH7eIkWNdaWhP0f3P
oRs1FUxaX7ttbuFJnFDw+JIkKTOtPiuLHQaSQi5K16bYxMvrtMFxw6NLyxFcoLB1
ibOx3KFWF2bLmRZpI2R6VPHDUMLfiL3EFDCNW4XKtS7GxrDC6EWa0fsoTHwO6GZd
/cLeqiofDq9wg/mLURYLfwKBgQCcywLAJ1xZUy59yFl7pLI9iLgmFSvlncQNJf0m
+jKTSEWZcQoRash9bXps3BrXo255rF+CdfJOjslxUdYPBbpHL7n1SsAVm/q+Ohs3
XADMA2ygWxpOKZiAek9RluwmdbSwTg5L6sLQpCS6Yf15IFBJ2neBw54ZZMJ9roZG
3gCKswKBgGRoPW6/tJRuf/OfVM9szhruhNa1tUJre2RrKnXzp4P27nfLHKUuHFoc
A0NXSDu8b1WDFHi2d/GIQm/ldiShGqx8HLY4fgBKTMLZ6nJXZ4uhv98xjOYy4jdI
X3HwYl1ukULFfhMVlS4qF6dQS2FF2ZxbkVwKYCjFrtyEJOjYcce5
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUBN4qin5jD3jO3rKq1yvO8YTCOM8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCkLFKcf8jK2dB0dVNFO8ULxmS+4939oXH/TSF7JiNmUxGI
WkPyUSgHQOatbhAK7Z91ZnmWyVrnGzXjccvW64uLLrLFA5mL4q0iiwroxPnaP0qv
w5ZnZmDgH/SPrzt5yw8ndagkfpxLekG0Pwbh4Coffg1VgEw/gqjv//moUTSQB66i
daNHd4bN0KVDXmycUdqI2ER5iqnDnb6Fi4DTQXSkwd29t/mRaHcQLrwiV58YqsBF
YcpE70UWgV7j+e5qYUlzJ0P6Te8QU1pjqigWoAuJNptq7E9wenSJ+7RZB1c+R+48
bBuQpoX+UVQfTHIeJ2NSKiMN8deLUhPj+fQrCp+1AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAccb5ZaUOWhp4FAwQ4iTfo
5RHaPGD770BgpIvl5yKAmfAN04iF6GgcCvZP69m5lFlNuQNaz0kOTIY8cNvrksHF
OYNbm7aHHdCGKs8sjdXxrJrL07MwRsN+XdWIDECGQBIHmvcOeY3HLdxcGr1lSpuP
xdT79hYrYeMBaHF3RVItts6fNVBGFmA9hf6/cDEIRt6TDbfBy+PCIRQO3OxKa+ch
sIemO+3tJsyB6xJz+iG7lO8QCI3qtn02XoGM82WMjgJVorWMzTSoMIP9UWMECoDw
Q9zy6Fqy4cOWT2qduWD/7r+5e2jmI22wEU9LW3QlNt9XziVBGqnZEiKfOdnf3XdB
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEApCxSnH/IytnQdHVTRTvFC8ZkvuPd/aFx/00heyYjZlMRiFpD
8lEoB0DmrW4QCu2fdWZ5lsla5xs143HL1uuLiy6yxQOZi+KtIosK6MT52j9Kr8OW
Z2Zg4B/0j687ecsPJ3WoJH6cS3pBtD8G4eAqH34NVYBMP4Ko7//5qFE0kAeuonWj
R3eGzdClQ15snFHaiNhEeYqpw52+hYuA00F0pMHdvbf5kWh3EC68IlefGKrARWHK
RO9FFoFe4/nuamFJcydD+k3vEFNaY6ooFqALiTabauxPcHp0ifu0WQdXPkfuPGwb
kKaF/lFUH0xyHidjUiojDfHXi1IT4/n0KwqftQIDAQABAoIBADLetP5fLgWE9m2P
iSzTt1vNrpvjmX6kjuEvsicpiyCCrtUUOyeTdBbDSncEup3YQWesSBKr86nWqZz/
Ps0qkUOgRa58ThClPUaN1OSJXG3+3JKXxTvm4i+wVyRKhOBZRinQ8DfWr3FHwaIr
QWOuBP9bHKCYr4eiYdxz8ZTxDJtv9trGCajRnTv/zENoAHC3Jb9g4SPZ+bCNP54n
gBEwY9c9tP9DKtGDMS0wfLO3La/VDO4Ft0KGMMur5hyNzi6xA0v+HJmaQS3h5nkO
H3MbDQBDbuvjpAk4IlYKExFsiXbT3v+M1Fq3G1z/32Gucx9AraMngdOOyoxe2NvZ
KgtD4wUCgYEA0lwkaXW64p+NE2hEorqBadCDyKmHnYhKjzG5/PuoOxlBsAwtx7Ce
fJ40C1yu4OTANufR7VXWOgH1eaO5lCEe+VhX1NyVb5otuJrnAzKQ8da3lEIOLPcb
fDkGS9LKdEWSIeA7gIRdi0S+EFHbBqgg2hsWO4LVAc/6N9OlPNnfmQsCgYEAx8rd
AEw0mqE/UWvofI60b3pceDkcWtOZef2WqkVLYRvWjh72S2KSmhbJxB7aAQrSgvka
9aCHS616yo6tai07evd7VCRNmPzozRnG1NlwIZW/eFL0JYOXuuH0C6Iqi6q/VLtY
iBfz7114IYGA8Nqj9GKRfZXFGuBZ0sbSetNhoj8CgYAf1NuZrbv64QPbBPMl4K0G
kwvuCGFCIEaQBolLU9VwI/FBr4YZ6osA9nuPoJXB6DuB03B7xnplSriXkIPbe2uR
daHMzxg5zA3RGneMj1FJlyEuaRR2D2p0ULi4Lox+LazgPWsjlmQFWACevZQ0HKrj
9idWGAUdghgt7HPbkmh4YwKBgDvzGkdplmtDsS0sVPFzHJ9Ktw54DJMQZUAeoKPs
8QZthP7WOY87P8QuzFIl88JWTf5w4u8LQS2rG2pGT7DJa8ylEAOadRJP6UcJ0giy
Shw5w99F/O54wwGXpVQMT/nivVCeep0zmsWbZV2gb2FWKdY98WwekatT4IAHmsay
QNyfAoGAVetKQkO9H3VvM8dloVF/Bh5ui6uKlYO/zNop01ClUH3KBc3WwdVXCasq
BEsJ0HiuHTU5N3UPicvLddCdxkAJKTQkwqOFqcuHAv6HR6RFBWaWN/iz0a78Q1Bh
gwCYEHjiPevWb3rLufd26SWtG/tIsrIEjx3BttKDRqqngLKSUvE=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUU/+7JgmNQiwRivfB+ypu3OtSTJEwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDT/HGxRGnq6IATEXgdHTrT88mmY+JRNzeBnD9Uh3uwBkai
kJam31eY3oxEsQWVZRJ+Qsynr+VBgxFquNBnHmQ27JOqAH800oM1CC0bq4Z8ac6X
O1SjCdUQdaqpjScUNfxWgk6gG3e9KiuHcvyOezdIvPb5Z8Lgz1Wk53IiUpjOBRrL
jvBYVebvpAog12q8Flbf3Myu27ZsL3lUhVWpfl91sEQ7rEz3ollxl52Mz2JA1B2+
TzaU/iDctTQnRCk75RqDmVshnKXKXGNnClwZXtIea4mfVVJB4mJhwGvgsLRRj7eg
BM6E+jzBfz181Cr0PrhpzGJnfuOtEepby5F71GbPAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQA5+/o35BCJRvrfMIp311Xv
ybio+Yq7Jpp4wDOT+6XlpGMMIHGtDw3fYXhZeXDLJQ144reDOnLWBEN7of1M0NHu
Y5ccTVeYaepZnvncyXtgokDtPZjegXj96zs1IDr5JU4F3x7xw3+zppTAZCgGQ4A9
rMwwFjsm+fbjITR9T5fLppUSW1aTCSii3i0VBzGyXZlLDuCqdOLYCOX6WFtx7j3y
jQYZlqXqv5idx1BiEJT4vqC2N8elpmPsZ0TIR7xIFft5HvlU/U+aCO4NRetJaRj9
JK9D6Jt3shpKLbyJOfa7foY6LBf+qS5MpC3kTnfoeVNpI6DHKWKE6d5+au48ARy5
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0/xxsURp6uiAExF4HR060/PJpmPiUTc3gZw/VId7sAZGopCW
pt9XmN6MRLEFlWUSfkLMp6/lQYMRarjQZx5kNuyTqgB/NNKDNQgtG6uGfGnOlztU
ownVEHWqqY0nFDX8VoJOoBt3vSorh3L8jns3SLz2+WfC4M9VpOdyIlKYzgUay47w
WFXm76QKINdqvBZW39zMrtu2bC95VIVVqX5fdbBEO6xM96JZcZedjM9iQNQdvk82
lP4g3LU0J0QpO+Uag5lbIZylylxjZwpcGV7SHmuJn1VSQeJiYcBr4LC0UY+3oATO
hPo8wX89fNQq9D64acxiZ37jrRHqW8uRe9RmzwIDAQABAoIBAQCbj8xq1paXcQjT
dWVckB+kfGlFNlVVXhzYey2qPUYSFXjuQQac7JbesqnimrlLOYGJsEF46MZm/eTh
GUCt+4p1F8UA4x52R+lLGHXpsUSethKJvltMzaFSU9bqV5AO79L+NN+39JA4++I3
orUdZeRa93iR64gB64Sg38tMzqodvB/9vD1CgD/UFT/dy/FjMkg3UMU0oBZ0Zgjd
WRZUePFIiMQ+/VtEq2PVuFfwPqyeKEy6DUgd1wVliQNomgqoUhxc4lPFr1KhWvAE
q1Z8+H0Pd+uYzNTOUJWhhH1pLpinOu7V+AhtXWEhe0QXpoBELlCiqB5lMamTfg6j
hY6wJV+pAoGBAP6WFITgdZHTrOtOMiflKW14kyuEXcPmUo3V6L+esH6r85JRAspb
ceJulRsf/KlTZzh3wRRUb7xTNE/S8/w2WSoVuMbsmY3hs96oXByAhHS9SSMaQ8ms
2+SjxpSerPr6qGOxg9bzm0s2z3b+ZcgJrZ+bKtrKPvacpZItKO/BbW7jAoGBANUp
zbhCcOzbKvNvRWc2BIMFy+x1PzW2ebq2XtyxETnqBVxW+iGbzBdiE/cpPn+P6Tch
kiFnuOaul5Q0N+KzIa1q8MtwTKPPZcQQc3Rv4xw96tldja3ZCnOo5WlW2UuJgacK
XXtQ2KQegTj15dytPhR+41v4GksjFnI5gPvb7SAlAoGBAPjHW+HFHd6UxQNj9Gs7
6tHI47fAr4gBiGaFw92Mitgd2/T9KQbpeU5V1WseRN6KW/G4RHtDT7Tucc4XTMkH
qvYPJ/NrvVoCVqycRPatN8KEPfYJcnifbHnu+Ny+ejb/vpE9JKJmhzhmpTGYw4lI
u9ud27DVtdVzmfBQJRK1J+UVAoGAFw+Is/BsKxOi1+cnyPytDEeqQhCFIBh3nt1v
8cwuIufQYKcANHaYY8c2hbyuiDpXbqFxH7AK7tngiCYGDb53XD1/g2LIx8f+KHHn
K6eXGE0ShSV72FzspoqVFwpQQ73CiwGyD081wLuUG0du8KrFVo5Lpn12yr4nBYB3
Fcg7JQkCgYBLRw82I1NXVnqODF47PHuAuyNKY/ZT76zRY7UuVpraXrqY3Vc7j6kz
0ZrV5NxAxbZMpJVGEfc6B8YIQz3np3P5s5ME4+bbIzOBQcmIJXLWeMq+oZhTBcTO
u300qymEVtlVqhWGtHlFbxSPtV+d1BFCptUShuE5BpvqUiyRIZHokA==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUbgDpFoeaeAbCjZcmf9YI/M3IB1IwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC4vhXYgLWi/5xCrTP3efRW65MPn/vzynsCul7dya5vmTiO
BZV2BkzUBRfZygARIUy7z9VsX22c4I/xRtJUkjAtDaSw02bnlL0BZSjZg8DYWjZO
woO++FNweJ2SxvaPQypDCyRQuiIMGBcsqMX89owC2y0cQtYbB8kA90WXNeaSXXzB
WTpPd0pRDx+VOs60hGIfH5y6S/MkgDPHLkXYCGMqRK0vBbKr9yWq7YNkFmgGd6oV
qAspX0ykx3KOiubBO9WV9pw6Tn6Bzm+5yD2E4p+wmR6r25MEHExB8mzULoD3wQWE
1xRQDZ2dF9dr0CXSnDlOpCf3LcHX0z1NJzG93/M/AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQC7rOkhmH/14hXD8dFxw7fv
MBE07KvCbbYxoupD3pUIHO27Nuwy1ZtcppHB1yLztFVy1gk4u5HfRPkliVrsUlCy
IQ6JiWl11TU9vPQHU6ZxAVYrmS4UhxKjOVQWJ9ZXHcQWamNZS31uCfEpG1AvLcQp
rP441aWGVl9pn4DvYCcrGA9iOIh4t4+IP9KdcehXwf5aIip6j7FR7lRgoS65xx18
aekW99yqzJtyqtx+UCn64a9lGFlCvzdUvh1N8qtv5O1FGC0u5erCkTpdR4mwbljh
Wl7fa/81yeoV1PM6sHrp3mEK1qY5yElHIEKlsoJvnoy0GRJXY+bhfEcZVEDvl9rW
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAuL4V2IC1ov+cQq0z93n0VuuTD5/788p7Arpe3cmub5k4jgWV
dgZM1AUX2coAESFMu8/VbF9tnOCP8UbSVJIwLQ2ksNNm55S9AWUo2YPA2Fo2TsKD
vvhTcHidksb2j0MqQwskULoiDBgXLKjF/PaMAtstHELWGwfJAPdFlzXmkl18wVk6
T3dKUQ8flTrOtIRiHx+cukvzJIAzxy5F2AhjKkStLwWyq/clqu2DZBZoBneqFagL
KV9MpMdyjormwTvVlfacOk5+gc5vucg9hOKfsJkeq9uTBBxMQfJs1C6A98EFhNcU
UA2dnRfXa9Al0pw5TqQn9y3B19M9TScxvd/zPwIDAQABAoIBAQCzrr4Uq2r+tFpJ
R6jppMYP3GRWqCYoAeIOzzIByW1NwdsN10R9XLdQ5/tAqoXSI288pHJSS6aTFJ8r
7tQXyW/uAf0Styq5RyNlvfwzQ0BHrcZwaCQ3k9Oj6sxnu/iHcq4iMy4JDmCbHrs7
hpO67BlVldOUTzVraPEJbXdUEOrHo1fMtWwb78sIYYTItX8a/rP5wuJs1EaQiVHR
Db/NoGpJX9fdriLweRgi7pvdRo2So1ZoC/95fQNFstx8KdMXTj8QKHnXV5LOndMq
5X8EmtACBU/Bjcrjij0YAh1g44NRQN4jmGWEJZjLdTsyoE5tI7rsCt1QGqPs7gWT
7JX0rNghAoGBAPWfjVQkn0ZTer7672frYhATzHypX9wW+SvUMS3id4hqKjch9Q2w
Z+t0lrpKSOtKghNBzrFms8CPhuAy417BmmuA6HRFaqp3Ac0uAyA1NN8QaPNeHf1/
+Uub1uNdaN8pA4W8qKvRMb7dVJQ2gjbcr/ALpwQx9T3M9Xxy9hCyoGkpAoGBAMCM
GaIYczaeMV+jTkUSYdISC1rttJjFxEKuMWvNwajapl05kHw/fTt/UXcEsy+SBMQk
ArQHx1w7NGbkBNaffE+zyPcUjlKwHoix45Tnqwj4VIha9rNVxPDZIeas+pzhcmgo
KHWy1wflDIgBkeIWQr8Y/QWWvt+Qq3oD1MPlOD4nAoGAScL1bTxmPHdbWDkBZkLQ
uyVG9nTi3bRkdZ4OesoUvXmsXcwrzEWan6HuldkzFr3UXDYZ/TprZrtzdKazk0Qu
vHQE2s3x32lHuDdGJwjzbL1/1v3/oZ4p3mPZX4QwtzuY3DOwr5BuEPRkrvHDnvgd
Ocg2CtN542pGmm3nqVILTCkCgYB0X7jWaaSo7C+3OAKEaLnKt7E5QdYXR+B41MN1
/qP/pDdMvRAAqHbOUQMxxhtusvhCe+lOWi06J2ZikYoDFd2SZn0eKMRkYaHyyGFe
jC6pez3MM/5LIZmoX/PHceD+lJwLK8pYaMDiOqO6SAid9wpcaYPzrsqqYMvjMRGV
XKMDnQKBgQDdmgTf1Ga4rBBXlc01bhQCz+TVD5eoKG2jy04eMxX94CagK4r2YFeh
DnF5ARyYEZBE3GZfXRVR9qyW4YxWzW3k+nloAE3WqKbWYbmLqjZdKd+ppAhXpgfG
7FPIfDJX2VcARnCR0CkxXF6f/6eNKg0lKfkuEA5q83Cp9HQCVXj+3Q==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUcSw+1Ww+zDNNx/vNquiiebp0nRAwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCj34tYd0hFq2vNzARK5oT3ZU9MX0GNLidDDBPpDkXEYZnR
yVqdLe61OWuU1dY7Imdoc72HCDQLEd3bV2dux2jE3ktHP0zELRIucyhBJvx5zl68
ZO004prWYH84O1GlTHsz/OQZeTyN8detpOgEmjZYJnPOWoMW063r5YAxfZ5BRdlx
MTmnJjLIxX2q60RjoVZXNtl5DOOxnYdGX6w5L6KXMr/A/65AePP1RYW6ugkQwcKA
+PsAbDz9T7qDmgu9gHcDtGUg30ua6kLgHPx3ZrL5RI9KxfP9l/r3TEXg1XhlVyv9
ogb12SQHitHR9HFcs2y1CraEw7HGTTfn1wqbqtzFAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB4Z7WQTY5irFfCZzVsLjpa
ntAiAe/EdaGbx/12Hy07efLQ29D7eMWOvjjlDUjAZFDefH6SPB3bZXY5rhY1qHnC
7l3Fut2SqToPy4/8m895GNOtvPJQJgw3nUijKA4k+tSdN9XZz39sDYGKzHPMuAk4
D0S6MWIrT00zEUMJMUoFfCF7W1II5phrlAZTczdEiXo3fn6nSgsDXGgZS6Y4QXh/
5HCPCuI/F1qZWK3eVdrrQaB7u2LLo3+qfku7unZ7+/EgomRL27pMukrL/N2kGU0U
7P8mpcs7j+Sn9POI9h2fSbB4IElbHP1AM/mTfLc38bKQNt1bnXzMKfhnOWHshBrm
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAo9+LWHdIRatrzcwESuaE92VPTF9BjS4nQwwT6Q5FxGGZ0cla
nS3utTlrlNXWOyJnaHO9hwg0CxHd21dnbsdoxN5LRz9MxC0SLnMoQSb8ec5evGTt
NOKa1mB/ODtRpUx7M/zkGXk8jfHXraToBJo2WCZzzlqDFtOt6+WAMX2eQUXZcTE5
pyYyyMV9qutEY6FWVzbZeQzjsZ2HRl+sOS+ilzK/wP+uQHjz9UWFuroJEMHCgPj7
AGw8/U+6g5oLvYB3A7RlIN9LmupC4Bz8d2ay+USPSsXz/Zf690xF4NV4ZVcr/aIG
9dkkB4rR0fRxXLNstQq2hMOxxk0359cKm6rcxQIDAQABAoIBAQCFaZo9hKcPKVcT
7bPU8sVv0Ef16lsowFlwiWWwSFFeZwNeuuoNqvZ7Deta+Zh2/jRn4kp7o58TIBGZ
4BeyJaBTHpL0x0ENOZBixpgQKthDplKUWCqR8qaSP29zbT+0LobjNVDSuFQnT6wC
j43hKVdy/qMrbZ7pt54Rvf9Wy2lKw3CSLuN9nijyzRdI3Y7Qgp7j5mbYTodagBEw
rZUNxZgZ1Drtl1cGOpFzDhYfIgOBgBTMcfDJh7QHgrGNBEqdOTngBN8TcrK0jGT6
4Tzxra7yhmyJmCa5nzk/I3ZZ3DMdVG70I9earH/MukI1rH4BmLLKFjy7XGWRs13c
EKe46T3hAoGBAM+RSuQbNZBY6QTQ5b0ppG8C1b+LT1+UOFlWnywNNgB3yc51zTcn
TNF+YkNRb0q3VDcdYWxzMrU0F/30UEPqx3QguXZ4YYmAAlE4G9j3OlbX59CAEmnp
+aWRq9sAxdzzQ+vGn7iTWkDPdgf8jsSm0BYP/NdKk57wS8j1+PPc2GG5AoGBAMoc
Phx8XMUwfkCZeWNnaLHZGMbVJz4lC82GlaaLfdqR2fitxZSB9YAyNe3SE3FlThi8
sW1D7CxuGqQRKtql8XlpZhik9gGYtd+vricF2UiO3c2OKTg5FPiHanh8WtYCER6A
QwdATKjIUyE5wS9Cnv96xg0DISlcwliOFbV4x8ltAoGBALMqDYPRvK1pIVGn4vYh
0K6FuuzIGe49aVor+96xVJCY1VfhtQ5LXPJjbfv/edn7XrToJmTPFtD0M1VgojvN
lvY1HQEWrdJa7SUgEmF4HSJC4PTG554GeReiIr4575BlZpZIbyuJ/Vh9+rqwFKfH
+Uth53QKClwhvLitIIOWeCv5AoGAedR2eFNa1J67rBMXgh0mlfZIoiqA4kwQhk53
TRJOxf8fRnDxZejE5QbfTUFR6Qvo/K5ZwYStC8c/FeEnVO+s1MP9ACQICsRT9cd/
khRLexprh2oHXNXD12BBhOlpFBHg4eLtBKT00NUYjzGyStu83kHSuqtFRRqeKCVV
3rM0sy0CgYB5QvJ4/TSqWhVodM6DVxSnYzoF77E3t2umW440Hu8grLsDJrA8SBMZ
0WKME6fXcbNm3p4eYZ+2sPiLpVf6w2JlykY+sDa+S1MtBAkgHwJqTIpQDd0egSvs
kgCFy+t4irJ+X3Oou+pERFHP/cMiQGAMvstgpz76/4CQdTsAejQsMQ==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_HARVESTER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUcr5lcnpo87wW1R4tGOd5W3U3m7MwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDFYItZq3rmZTSdcJK7m0sPbVSyexV4mIVkR1JLSYDkRUfC
xWqPB2ZY1sc6a+Tns/0qVOEddjfD8j5GrRU1g9VluSnKp2bg9NgQkqTEuyLDPF9C
iP1JOQudPSPQTeSwyOk2bQQ4LP/nRZXzZ+NnAEEHTkTD7D6LvFTGrIEShLIqxHdY
5EeFXF3zTpp6LOQYii91joqN6i4BUbbMr6MoRIgVUZeEdmKPHkyaIg2LJ+HiqrNw
xc8Yg1ksRBYAKBbPptLsIPXp0T5ja1SUEUkyDaFclzZnAfQhB57+0VuA4/pIJcLV
9p1avjw1PyrHqV48AGB/NqWA/+4kXEkZ+DrrY1D7AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBIvNub05nXZoxHcysNf39o
DudZ8wmn1urJpYQQUhFfZ7eGyTTgNiEI9Mz+kVK9f+BR6ylw5yDGpIC2BY2uDdR3
r+y6bs2loQzfIMWAOEsx86zMG1XmYj8zQ7pjZ/AOInu/Cy/w6AwNIt7U3B8+nZEA
qPatVOMPh0yWJ3CGjY3lP9mjhREyUBwBsUOq813JYXLsq/euFm5HPVptYf70Ms2Q
3qkSmyZFozJbW2/wqsb083kJ3djkVliqSDVQ2TnQCi8PT/9uE8LfMTrnWbVZlTO3
hxByAQAco0fiTQ7BN74FuhzqBLBadcnQ6HnWe87E/0OI9co3+vJR1H6xHSebJ9pu
-----END CERTIFICATE-----
"""

SSL_TEST_HARVESTER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAxWCLWat65mU0nXCSu5tLD21UsnsVeJiFZEdSS0mA5EVHwsVq
jwdmWNbHOmvk57P9KlThHXY3w/I+Rq0VNYPVZbkpyqdm4PTYEJKkxLsiwzxfQoj9
STkLnT0j0E3ksMjpNm0EOCz/50WV82fjZwBBB05Ew+w+i7xUxqyBEoSyKsR3WORH
hVxd806aeizkGIovdY6KjeouAVG2zK+jKESIFVGXhHZijx5MmiINiyfh4qqzcMXP
GINZLEQWACgWz6bS7CD16dE+Y2tUlBFJMg2hXJc2ZwH0IQee/tFbgOP6SCXC1fad
Wr48NT8qx6lePABgfzalgP/uJFxJGfg662NQ+wIDAQABAoIBAE67ShrEukt5B1nd
88n+EhzfQa/IRTJLtLnhcUQy18U2lX9t/Cl9jCfX1LTLIQ4Dz/K41OtJosj4sjrD
A/jK0662A6Ogzvrg7+b8d9k5xI4YYO9Lca1poeZg4w5OY/DY054wMkSuPo3kRgJH
6H/HrCjb4bY9YF2hDDgLy5i1cdR4wsWlVCV2NkLQSYifPQxGHY4jcDGbyUNhY0wZ
Nene3YvzbYLaJJtISX29K/k6Pfatteu8gu0AqzxNLJa51gPyrNFjmlj4hLhtR/Ty
75T6lIAciLkW0nswCb3ZgRh9xGgASyK9rqtrEVqW+mG4TCVd45aK1s83EBxs3RFO
RcZzmnECgYEA4SaQpH0F3WU7aQMBw6T+jQrSwJnNlES2ugyDSrLX7Exu1tVgrz4y
HzArBg1xHyKnHQmaLrlMPowcDhCtBO+YC+j+gGak9UbaeJbR4vcVuv2gHDQ1Wqd1
wvxoV1FnCNNta/TwKKoQfEZasTEq294i9krbpWh8sqR61dEsKDAV/OcCgYEA4GvK
Az9jh3VkXv4Vlgvoc3fnnhx/NEXzd51TcBFp81zD3zH1GJ37bUMK2jm2JFW1PYK0
AyVEJUA+MWEISt7lOrjI1s6HZk3Xsh0Qqdv/WPA9OrG3eJxPH4Bo/M1HWVG72oWD
tbjoOViXYKYd212hKTdUCMqGaW6i0kWIajFUVM0CgYBw2TOGPmPCJAszBx7LQNeV
OeeIQY6Y0hgECGGF/z3aYjTr2Ocs7q+QkkP+NJ6OTIAWPcnZwWZFs1QceJ8/6hb7
YTyufsQPbAP0jSOF7vIlVxn5CPH1DhooMPrbSSGres1NXudAenzozRqH1Wz15tD/
QWX18fkOUQKASOco/XEH4QKBgByDtZQ6DqRcdxdWw1lgQ/W/6278gfEbXjb5h2t6
2vJv+/c0+sZY9GRKm2tk3864ESIypDquFn2BLyXJBWu17HxMlEAu16dZBqn75W0f
pc8gHzeA8yXg/nCrOSu9zW3845h9VGHXj7IRnpJKKQsBV4PMIuJHEVL+GrQK361W
fTeVAoGASnt6kmfgDED1kdDZGRMgb0GvyAVObjLRBu9eRX8nQEKKpFydBmdDM1+Q
coUvrLhjqLb81znytV8Erb2Luq1xzlnZrWK3uXuPJW7T/m+DL+Oa2+e8pgRq2/Xi
QJbqzpOmiuAeJzdT9us1UALoXHxdzAw/oSC9Xq3j66O1vArAm9A=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUPDgBpxOAo73yMiUGMFNbK0SvFvwwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyM1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDDT7pUEKAS2A96fkLb1IfDbHZCpOTUgKk7+uNQXTKarZv0
yys2/K/StPGJ3+mFlN1+dqubVHUILhPUpfFNHH3zintDsCjwu1GPKRuqgPla9ZAb
zBft+KKm2CewqvVotYOcfIAUqZMmfWuyxZFL/ITJqnJKHqYU3yO8pNO3k9c9tKVe
AVLlarcHJitjSkKz+s+3XRJYC/x6BsguRiNGSPVPAM/jV9PGhaQqlhWtQT0/kcEs
MRICpIPiPd01bX9NWbSoEbCVN2mBBxPi7fV4V2Y+xkdjj0QtkLmJJTnatNNK9UjK
5npRqHyw1ogyguno10Jx6e5vd+3hWiJlBOzpqiT1AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB5xd/q0Z5SfPECusnXmAwF
X48KLYhjc1/483R1gz2Vy1XNPWzDDs9I8MWD02BWr0dMMuhV6iPFmmQcJ76ejJD0
NMtBpjDFfCknFuMavbog9ikPEXhL3EtzXP3jC+xsdvYwi35hkBgGs5hnAkheKklp
cjRurmsBAHJBlEsUc2C6kxq8FXcLM+WzJJYOitzE+fpyxrmeOIfpUd8Vwiu90Ta0
/w1mGD5vlXBTiFCwLEc2fVR7OPm3QxKvJ+eUdLTh+X4VgJ5vvdiqCodgAeqDZw/Z
x4hOnAEktgEqadUz5t7fJzxuWWpNTL8OQLJgW1cE/Kt/P8F9IQ5rC7PS+XU+Ds7U
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAw0+6VBCgEtgPen5C29SHw2x2QqTk1ICpO/rjUF0ymq2b9Msr
Nvyv0rTxid/phZTdfnarm1R1CC4T1KXxTRx984p7Q7Ao8LtRjykbqoD5WvWQG8wX
7fiiptgnsKr1aLWDnHyAFKmTJn1rssWRS/yEyapySh6mFN8jvKTTt5PXPbSlXgFS
5Wq3ByYrY0pCs/rPt10SWAv8egbILkYjRkj1TwDP41fTxoWkKpYVrUE9P5HBLDES
AqSD4j3dNW1/TVm0qBGwlTdpgQcT4u31eFdmPsZHY49ELZC5iSU52rTTSvVIyuZ6
Uah8sNaIMoLp6NdCcenub3ft4VoiZQTs6aok9QIDAQABAoIBAQCO9vlJN7I0mPsb
ividuYB3SBl4xwLJmjRGt2tVFCNKnfIeyekkIusArXpwlfp10XYgb/VFihjwl+nk
KmPrMgPwFVoNPhF5xWP6Cvk5YZclQcLu1gJeKzXEM006QKnKr7NbBLcsaMRR1FTV
U1D78iexBpcKMk0X0g5ys6RWKF3Rx/PqdcDnH71hlZFKUVaKVeXvPdAF+Jo2D7Rv
a3PktRMjB1c3JtVI5wGvvkIs50n2pZsIkh88qhwZRurvJiY/mUSyi2CgnIkLJLQO
kziMr8gOPOmRzy1sDY3fUYaoI3cnQ2va0zqLg8GkQDfLg3UbirFYXchaRPkoYRSw
fPGpnXsBAoGBAPvFlKjzh4Anob4CgYNgKnZHTeDHEY5iGQECbcFWnv9TJ/PapRUC
MOPjW8c/SxZdz8neBt+pyl57nVrwvOWO4Q6ccJr1a+1a6Lc/BxL+wUw6fCxjfQN6
s3VLKkrALxgmbWjhAOACDOs9Uj4O1lhLxbhPStaSAMh7nc7OAOubi20FAoGBAMaX
aYz+zF8lQnQUzO0zg+4VbS7bR5KfjLoMXF4B+TJ/n21oJUjKSPRTcBZmvSSxu2Hv
8Dj4guxTVezxis+h/6NFf0xrPD7zxqKNMZ71bszR0qfNzEkMix4inj10gUCPhgA9
k8buLFm3pIAJ9NeiEIKgZT4H9TItItLCfQC8i9sxAoGAX69Ah1E+XwMw4jC7nf1P
RfJlc5bUYkN/8zVEFyVfefPVjES9VpWllQZUXA3+8HoovTSHcjtqMKxUKjqx36CE
gfQMi6fYI7XYGcR3YM23EsxrYsdQvKDGUT6GzS/q9gesrx5MIdZFqKV+ex1Scu4h
L6Ha9F86svbgC7eY+/H6dC0CgYAODRaFyF1zefJqvjIFsnhqNw/jmdZFlI5jd45t
hFw6a3c/SXgh31YsG1855okJeJ3WfyCTF1pEGF1jB3AX4tFwnvEz2f6IQb1TMQRK
x/jP+ySZhOEoZf/N4QsrM/wVMlJ739992so+itTTzmCJhUj/xROEwRFjPHhTSzmG
/NA0cQKBgEE19gpbOu7f+6/mBWrS6AR7eGjZ7M2wRap7Eoh9M2VV/ou3tV8Z4bHW
qcLBFa2HW3E/Qgh2jz2q+aWrRKlbJfzH/EtoQpwkUeKaDnONK5O6V/kR1VNBnUrB
0+C+ngvuEff4uTk3zmaCc+a04HXWXhuzSuG9LA4V7twmgNo9AlSs
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUIDNyJc/WIgjFdIWtYp9/dZyhDFwwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC/em2gGo4JEdff7eRAMG3two7JlNvEzuTn95dcxWo3Pydz
OJ83gPrGCM93zBvxsCOppyER+c34D9toxAvu5N7S/68eGOPlvbqS1aUJtMRXIoGg
ghIlz1w97VOmQ2DS4PZX1Yw+563ah0T/kmKvrJ6Ti8MOqvJ28GNnDObBP1hSfezu
/iRbiaGJUF0wRULFaPX8uNnOT8oxDXzsyBRKmZLN/O3bwbpX3hzIK2D7BBpqUza0
AuO4/zemr3J21QFu4rD/Wbd5/zX4uxSOAIXbT2haDT5KZEUYQv2jXbHY6+tzpMRC
v+Bb3yAeFGt6K44fzqi0fj1pzoHZQ7pgqKwRKA0tAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBuL8MMR6mTzcL/0OOWVnQ1
phT2S9L1l6VmsZYK0/+kUNRphtglqiUg8TuHDUvXY6Bq5r+NY9De6ZhJMhsVYt5A
XRkBjEwIPLC5+JZi8iv9uip5qyqsfrt706zGz1NfVIk6pS97Nssj4d2WkdB8BrD9
fnngf6tnQJX4K7fhE/NWcE6YMSBA4GG/JvpH9ouJx4aN77zF6PKyX+iO3GDHXqNH
BAdEbHgr4pUPZuUg6c2x4T20NKnMNkx7C3Tx7tp2w49VamUwnwvm7vuzjajd2st0
q2O+l3iNwRuvzL+KaDhqexf3shDSCxuYSaInne2XmCiJjVW7QRfQmyA1LiUk/vfP
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAv3ptoBqOCRHX3+3kQDBt7cKOyZTbxM7k5/eXXMVqNz8nczif
N4D6xgjPd8wb8bAjqachEfnN+A/baMQL7uTe0v+vHhjj5b26ktWlCbTEVyKBoIIS
Jc9cPe1TpkNg0uD2V9WMPuet2odE/5Jir6yek4vDDqrydvBjZwzmwT9YUn3s7v4k
W4mhiVBdMEVCxWj1/LjZzk/KMQ187MgUSpmSzfzt28G6V94cyCtg+wQaalM2tALj
uP83pq9ydtUBbuKw/1m3ef81+LsUjgCF209oWg0+SmRFGEL9o12x2Ovrc6TEQr/g
W98gHhRreiuOH86otH49ac6B2UO6YKisESgNLQIDAQABAoIBAB8r4h7XU9ocIoWc
57SfbbXwH2inqCNg/xjYULbUmJcH2/dA94KEp86Hbqb0/nOZFiUvRQ31GdfRVQm4
KK0qay/0WeDPcoJbIb13tFdhKzl4L5wesK+hE0YtlZmSjHeoEdJ4vE0dUEssDEqC
3Tf2JRamAQopQDGmrrf+/K3nDwzWlRr+UcQF6Muw75vBvYVkfkCiImiV8oGlXRJ0
CP8+0XPOmgcSmDcGM/qWxjDNZNoKt5SBx83xMticdUTvUKBIvDmSMj2VxTsMPbcy
elEncnbiG//Smz/tU8sggtrwhIv7zCZP02TJBFSNmE+orZFmHXAIBsDfW+27vN8w
75B/ES0CgYEA4d+9mpNDtxcphunjnoegwLDB7OApGY5SACCvt2HXQiWXl9DvPSU5
tAreJdMV6OOTkTwFTGQhOEP0uSd1iDrm0DUvtUjgrPd5JyVAlMyMpc4z8fEoB+jk
lDoXOmqnP1t9w/GJB7YX2KI8qWsT/qvNGCa6XNBEFlp0fVzOzLJARr8CgYEA2QRG
vBEtTTGi4fe+A8Lhb2izc4YHhMJQBZJceSTxO2hN+BxSzltyf/7QMyC98sUGfOmG
bPzISZT9uFdA0ZXZjaoe+boa5HQJf1WxfAUlAOy50eetd+90+TmQ/qFePS23Im9m
dXyR0O+eiKhMfMJnkf1s8xQB2Lec9G7AloMlcxMCgYEAsoW6P+/g91bRNZaqluOv
hFywCV5qXY6E9SDggNpN3jQECrPSQsunPcvRJKgfiwBD4+hCb8w8DVJ4m9a6KEAV
qb4/xNKi8VJvaSciUfkRuQKvP6xQ7V9/OkBnl34wTf0r+7Btk7CyTEB+HZFKLmDv
KwWBClZ5WgmIRIUT1emUr9UCgYAJMhYxN+UchULqok3J6QMWbnBUL9S3umgbpFUI
yRjztHrBTanwlo1mgQyfbf6+f7zDpD2O9rMh8w9BNWlIuDnMt+2yFUG4dnZEkAQC
RlGIFX/WNiPylhH10YukToAoxXwiGGhWCB5BpTWpgsAi9TXgSMXKEwn0/erHrL26
Yvo+QwKBgEI2e6WELLT2ebBK/x9pxj8w0IevV0oHg3Msod20iw1omrkCyge/Tt1+
ABTK7xhmMPLJHD8ZiMl8sjEKTx8PkAZoKdfZV0Qr+BIhMneO3QTLcdZiuIbjb9Mo
3QvOzzxKKksub2JjN/VORKTqMuuSDQLeEBtv+sRGtkTHJrFtnqwo
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_CRAWLER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUMqlg7Aqc99ifdKynHggljrPnQjIwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDr7NWQ0b8tQSlXzaa41vexl0Zc3WrfF8aw4mEaMcXM6lkO
hX5QLZpuTCs0RGwLXVAuqEcbQqA7GIbhq/ch4c9PSkh+yBUOB8SHx3UanMe9sH7S
80rZCX+8HFMVMce5mMEPIRA7WmGRPf7+Fh0yHMAaIsaqDbI5f9DqLdWE+FsrFrdC
kp0RYTYQsYEl3YEPJfcYbfrX3I9GxKLSUX1iKsMlyohrFSlw/t2LlG1jeuxd5oLR
L79QY35LkCAsofDK/lThovM0qqnescGx4feZsLMCL4rv0td2GWNhA+4UofhTdul0
zRcaDZVrNEhCJk0RNf4wXtidqJN90Sf3dvIjx1qDAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCWj0tol4kMluTkz+sGjfpU
xTnbVkoJhaOVI3tdK5+Z8WkCS/IlFLFoHX1I5CoAtFDUTCrp1tU/5e0BzA2VfLME
B3+qgLQF1+Z2Qy+OBTRToUuOSg0n7qSQdG5zIsspKwRl+iobFKaxqw8j218/NKaa
+RJTdhRRrmrokiBxpz5AJK1WnLjYe65N/ZdfxHYoBMDtzrkCrPsoZQpHaUf/9K0p
v0tv8s4nr2NcAZrQeALoTvR0oJ5QlmRxfHY6xC170dLV9KHJTbV/FXXFmFQL1WkI
L74vcnYPvpD8tdY3kD8AXUFoYNb3sjjjmM5QS1pYva9PQUiuHqr8MAqAF4sHvnLF
-----END CERTIFICATE-----
"""

SSL_TEST_CRAWLER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA6+zVkNG/LUEpV82muNb3sZdGXN1q3xfGsOJhGjHFzOpZDoV+
UC2abkwrNERsC11QLqhHG0KgOxiG4av3IeHPT0pIfsgVDgfEh8d1GpzHvbB+0vNK
2Ql/vBxTFTHHuZjBDyEQO1phkT3+/hYdMhzAGiLGqg2yOX/Q6i3VhPhbKxa3QpKd
EWE2ELGBJd2BDyX3GG3619yPRsSi0lF9YirDJcqIaxUpcP7di5RtY3rsXeaC0S+/
UGN+S5AgLKHwyv5U4aLzNKqp3rHBseH3mbCzAi+K79LXdhljYQPuFKH4U3bpdM0X
Gg2VazRIQiZNETX+MF7YnaiTfdEn93byI8dagwIDAQABAoIBADXUNrIxOSZxLKas
9HJOEfvCITrFBkJaoWnwbOlWG+RyP9mRWc2fahHqbR0i02gQZWAP4xF0NSzmnrfU
zbE8XVmhAEN1EWC/Ivc76hslVGmSYI1vF0/H3A4mhEpcrk5JbRsvlw2DxKkn9Qsy
Ln0llCsibiOUtmpqIFeeF46cP+jneMayLw4CCWoOSDPHcVLcdcD47qfkTJKlG83s
AVhALyiTbLSnKLj0tkAeIMiCecQbFQDdp5scemRgaRscQ1dGi1qaX7Zj1LqIxZBL
wQ/cqEKOZSx4apzv7U6U8WSZ248jUXTxBM6RxToAnYMITv8T/pDaB6QepvOB1E80
Re7yNuECgYEA+RUVa4So6gYBYoXLFNvgmX/YUDOCM0D2lbNmS2WVZjr6VHu3mGP/
TI6dFnJ94O8Fxssj2Ei4F48isXXT8vag3M3GHSbWzo5cREdWmXUUM2vQisWdjQHM
kRBLHOAAxJ0M/3h8uu5jbQeaKiKvB9OU92W7FAPFIUOzJ3UrMFXZ/zMCgYEA8no0
sXyKJovzlhtchIGDtQ5pd+IfsoPz6edd2G0Jp3r00YJPuhpyivb3s2oTc08oEquf
dE+OaHNYIGWYwbpg4eDq0Wsfu1xt75/nKSUlmILKltwyq4U5Cxye3P3+ly5/aCzK
XRokBgyzuIl6WgSnHD72R4jiCobNhcXcHPdfd3ECgYEAm1rXHVSEtlJAkt64J65s
i9D9bihyUN137y8R4nzdjgHDGOaBQH8+QNXCjLmkYaMziyYwmTnh+G/CR8UiCSxi
cNW3d38+A18vlTaZgOVRUDEyxRs0hTpWCTSMZNoiIH+EF+NiiIUfZmWTdixj1xHU
m+nLoVQoo/LBzx55bZBeg5kCgYEAz6w+6SxjHjSLQarZiFtstGtNhXHT+A7vnwub
4rswo5K5j57uLdRs+fwfljhpxD6tcaAwB2wD6g2wEr8xH+tDAvKh6w62tL+rIKpx
T1oTYxXR8XdSpniJrKysm1Wm8VDPqieCgk7bP5stagXFFsgZYCXExOvFvYJLECGw
LdbomuECgYEAkiL1w+snhDZaGUfmA41JbMiAp+fWf6dgBfTieY2PLeB2PHOIQR6D
M3cX0bxsuFEqvTSer6/8Ocu+q5zAqEh5YxxRPiQ3zdqeYEMPGUWq+CGvtKY6IEN5
0ITdHQVmzbREwX9F5wiYXy0VzjhzMbXdTK8XpYfNm34B1tfTJRg9ZyA=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_DAEMON_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUO9NYo6D7Fn6nsq5uHYKUMvoi2dwwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQClBJSKiguayx4ifSydXnEMoDWK+HeUkK/38DBFn/psx0fp
joXEUFXWcDba1WH9RtExs7PYD2n4w4BPSQjz6yIh1oNWc2HOpyHl0Kk5pL68yxWp
3jFzAJQHJGgkeRdMH36lUQwEnQ3U8a6YNqd0j5qp24p2qyv9AGARvcrCgp8GeyS5
t6/tedqzzyujUNiOWzwdfCsdKo7Bv6VbPtx18b1EDQylQefSg3yxLXDgZEPlFPkM
91/B/p2Om5p2Xi1ybITT7dgexHqqVo6bPzL7mYUZKSZ+dYZIb36mTxY7GWDf8ifE
kMO6+/8Wetwn+hw5ap4mzsAJGZU1a0lUOsQa+T1pAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCqtpCsF7eS40VB/wdjpn2o
jxGRfet1uP4QIAA3cNwGG4eWu4xW5lBk4duE6DXZYkD30qZYjHEsIPkefEc4sni0
O3IDSeomhw8Ek/GCgPdk47JF0tJEKRIe4hjMGKI3H0Gmczqp6F78QJNUvn5n/nBH
9WWefV6sMsBLJ56CKRoakwYJzti0aSbAaaT1f/iwctTTxg7Jg4begI7XJyxTvs36
hwnNCv0+XSol4rerpLVaMm2IKbzfpCHygqxUQ/erch3NJ7mRLQgT/biYM1atPLAF
b1BApc+IIrwDbDMeZd9DG/Ov1Kbns+3Lg5H1eNXhCf1DW9HQNu0Z3XzbARmxxQM6
-----END CERTIFICATE-----
"""

SSL_TEST_DAEMON_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEApQSUiooLmsseIn0snV5xDKA1ivh3lJCv9/AwRZ/6bMdH6Y6F
xFBV1nA22tVh/UbRMbOz2A9p+MOAT0kI8+siIdaDVnNhzqch5dCpOaS+vMsVqd4x
cwCUByRoJHkXTB9+pVEMBJ0N1PGumDandI+aqduKdqsr/QBgEb3KwoKfBnskubev
7Xnas88ro1DYjls8HXwrHSqOwb+lWz7cdfG9RA0MpUHn0oN8sS1w4GRD5RT5DPdf
wf6djpuadl4tcmyE0+3YHsR6qlaOmz8y+5mFGSkmfnWGSG9+pk8WOxlg3/InxJDD
uvv/FnrcJ/ocOWqeJs7ACRmVNWtJVDrEGvk9aQIDAQABAoIBAB80a4Z7LlCaQluR
QiOMHWKe1SEvdSVx6uS+1dIEu41gbdfbrK3/5wuC8syU90+22Y5FhifAWnDBP30+
uWOuviiZ8QIjFYbHkiBsQeP1pF/9I16Y9s7heByVpN/oyiAKAJ/wYI5qyJfREAwW
obnoAf5G1rs0CUBxlrkkI7h+jOXji6E9EetW7kHI9owvZRgNMEEW2d/46Fh7zeph
00h8S6/AcsaeG0d5Wr7Dtpur28RSNUfiXJ1jccaQTgSQlE/CtTuD6T3CEbdPjIuL
xInR+ITVusVQmaouh1VZ72ciHFckgHMlzBJnUJmCN6iLEEKHtEwJ4Op5UjR77kxa
63dGc4ECgYEA2k2L0FEsRJnXmvYSh7LLuT6AH/FsCQ6sS7SMw3ATZBRuVFFEoLlk
2FHOXSrSsAZDumSFCK8NK09aGZOmZfJXi8C8BEvGTlbYQA4T2kAqkB3kc3jpq7D6
r2WuVv0JDSveJHxj13ljfEpaPkpqG/u2pr5QF2XfV8e8oguIwzpW7VECgYEAwYN6
fXYnLEhLttOqko7LQ9yrNtfR7uA/u8Rn0p44qA2DRuEjzgmCvZJH7wPJUkK22oMG
G9XcFW+SDZT5U3F6JnQSebSPF3R0yXptV+oWMAXRoNe+Ei8C6vn0k9dOXsp5Msd6
dswiEIxSf9smwiz4wdmwxev0jOuACRaOhMm06JkCgYEAmNzCMX4VtHfRjPYQZasi
krWcPEHud60pot1r0BKz0VmpJCvAFZeccQlfqseovo+0b1mh+kGxxAkNu2kzlKGN
AhRU0+FHnGWdicURy7sw0rfL17vsTEhiUd2upcULyIhWRlBADYs3ybm61XGAOdYZ
wUr0hF3Wdf4sLYBMJQC+C/ECgYBtEjlZO95qhDlAzF8pChkhn+BVIiIuvPDPWa2X
Nh0DA9LJgZ6XxB6P0UKAQqcXmYjM8urfh5Pr9R3iT+SUFrLdt7CuLoo0kyw8X6f/
1G47FRyJxvBX+W1wmgAz0DhZD1BuwaaSDQ7qOt1JOXHIImb3hEax2APX5ekdtjwQ
NkykiQKBgQCvrWTglqks5qiSAprEJduXZDuE8RUpyikfRgyTht9/yJ1ZLroj3g0w
ichdRSbSmj6F3dfUDYKZWEfFA8idT9nGDvvr4YVmuVmalc2AHDun1+SiY61ktGYE
jWBtNKr00MGo1LojGaaNp9Ru6w5o8Ae7vsbW1lknomm05kcELEPjFQ==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_INTRODUCER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUKrZllgClUfhW5LVCxMSaWdpORVUwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCxiqJHT5HiXBr1CxICYNvxLMEOaxEV+k98RIt1zrjrcfCk
GlQX8Y4nqF2gn/7s0wgW2lkPAjTnFH9r29lFzTx6sVqGuTal5efJiUqDxMYmWkuw
hVXcqSc0ocxKtL5hRikp+UifMW6YUQr0XDBrszSvVZRKiRtcwGBX7CUJ3pR40HxH
hdzF3K0XnqtymKa/Dz7egwpAms8EH16ndvNgt0Oy74iLLqbLSYIMqtRe99V7kClM
QpDpzQX47iQyxL047xpS0nArTgOfE2wCL+4lWa220O9TZf7Mon3XtX7SJb71lEkj
iNsQ++9S0vzM0BcWGeV+Y7H0MqBmbI0sYLltHG4dAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBWXFmtsc6tZu5VmqMEjOZ4
sPaf2yJgEDaPv70R8SiopJSXHNbn14+ksehjdLa4Z3R2QhzCicVMnhvovtXeXUi3
HuOnF6X5Xrk92wfw+1WW8DUsCLFFAjXggRxU5PDbXNafMSoP8005Jt7ai9S02JD2
yrbE1tgvCm4HYoliURCXh9//w1fen6D3WddcHuCHLYad5bHnplOgvtFobJaG3FEA
Px3wWmlv2hH22gQf+zGHkwVOd8Z+G9eSCl+wABRGUm4ef3n94DoqE1GqWJ02fHBT
hv3YRFiVH8A7AtBWyY3sdH5tgaO9uCwNiQ0gL64UyKS49F8jT5ChVTxidKyoQbWB
-----END CERTIFICATE-----
"""

SSL_TEST_INTRODUCER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAsYqiR0+R4lwa9QsSAmDb8SzBDmsRFfpPfESLdc6463HwpBpU
F/GOJ6hdoJ/+7NMIFtpZDwI05xR/a9vZRc08erFahrk2peXnyYlKg8TGJlpLsIVV
3KknNKHMSrS+YUYpKflInzFumFEK9Fwwa7M0r1WUSokbXMBgV+wlCd6UeNB8R4Xc
xdytF56rcpimvw8+3oMKQJrPBB9ep3bzYLdDsu+Iiy6my0mCDKrUXvfVe5ApTEKQ
6c0F+O4kMsS9OO8aUtJwK04DnxNsAi/uJVmtttDvU2X+zKJ917V+0iW+9ZRJI4jb
EPvvUtL8zNAXFhnlfmOx9DKgZmyNLGC5bRxuHQIDAQABAoIBAAvvnBVbPh2Pv6g1
xFIwnNjL/3ausAlgOLPMD+wtp7T8hgciVgD+FmaIJTNFTmgxj9updk9SAKiAckiY
ETVmJOjCv6lLDmd822ZrOn09X2z4qRoG/MzG+oHJVui22g3EH8RYpA8/zYWj/S6M
fBzhgWtAP6X7LcHAlTmUALF3K1gr309YpV+X1YiwyREU6mzc72ELXC6ZUWcn3jnr
AH4J3UEeWS4eQZs612WJC8TMs502jO5eoDS+qoev/lt/a0WCHrBz/DEwTE4/zIRN
FyN3FrYu+73ROsnUCxzMM76y6ff6N0Mg0d0z/PrC9QvjzDqJGQOSxMerWqTrwNvc
SmSVnMECgYEA5hAMxfHodOKUKfkxYfCcb1qx4Pjj7Uo/g34PJDuFWzJ002mb6Znj
xEwdWh7FDANwywojSSvXSryFyK54RR8yLjrUmtBzxiiRi8uUREseX6MxiBO/ZeQC
t+Gd/VJ9PpTVsrn/X4xmsozXBBKxzcqHKB7GwDPSZjzA4HFgAQkQqCkCgYEAxY6+
4vyOPfypuJAuPZ1Uswu78M6Km4K4JlviJj0czMm2L+7TBDljurV8yNB/dVd1lYS7
xnE2u3KlIVPaqNpTR78OLkzDYIZr3lkk0XI2/sA0f7iuHY20DfWqtM8asT+dg2SJ
E4NQM27zRHGOplsvD9cVqTbH+u5iA3ElT2gc5NUCgYEAqQQzjhzJjU2EUk3LdMuC
8d/sfH39XS/F94Fd+F1t/HDWGRcmPvkatvTAP5wJYWkJrXDWOYRm13Ymxyc+HnHr
uMDpvo7T70mQm+ZFF+Mj/ljzI6h2XZGkWZj8K8Y1Uwue733r2jNYo2YK9OgTDj/z
CYuKslugABI0FO/V+wzA2vkCgYBj/sC3+8WzsnPlq3T8UupQRhw24xRdamjzYYay
fDRbo63HzUaZ2MKV+s7ShlY9eqtVpv20kBF4B6t1lxASb4+/vQDchpZOATwQK2br
bLhRcdAg5cWbx+HfPv3MzxdfqCd+HiET819g6UPQ3PmrUnQbvG6GW+gVJxwNSfPs
oXIekQKBgGbtSfX6kZFV3T7DzbR/5WGw/48KoJQelQsyxIxxygTTbuGJ6UmTf8DD
VO5VhdMozGozRn91daoIT7usaqlY+tOcSAtwvj1EL2MoshcSk9JAzC6eAW8ZY6+d
GqmLP29tn8eIkavwWpCe0sinVGfXoqdMHgzDenUHeXShPqVGWGKT
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_PRIVATE_CA_CERT_AND_KEY_3: Tuple[bytes, bytes] = (SSL_TEST_PRIVATE_CA_CRT, SSL_TEST_PRIVATE_CA_KEY)

SSL_TEST_NODE_CERTS_AND_KEYS_3: Dict[str, Dict[str, Dict[str, bytes]]] = {
    "full_node": {
        "private": {"crt": SSL_TEST_FULLNODE_PRIVATE_CRT, "key": SSL_TEST_FULLNODE_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FULLNODE_PUBLIC_CRT, "key": SSL_TEST_FULLNODE_PUBLIC_KEY},
    },
    "wallet": {
        "private": {"crt": SSL_TEST_WALLET_PRIVATE_CRT, "key": SSL_TEST_WALLET_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_WALLET_PUBLIC_CRT, "key": SSL_TEST_WALLET_PUBLIC_KEY},
    },
    "farmer": {
        "private": {"crt": SSL_TEST_FARMER_PRIVATE_CRT, "key": SSL_TEST_FARMER_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FARMER_PUBLIC_CRT, "key": SSL_TEST_FARMER_PUBLIC_KEY},
    },
    "harvester": {
        "private": {"crt": SSL_TEST_HARVESTER_PRIVATE_CRT, "key": SSL_TEST_HARVESTER_PRIVATE_KEY},
    },
    "timelord": {
        "private": {"crt": SSL_TEST_TIMELORD_PRIVATE_CRT, "key": SSL_TEST_TIMELORD_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_TIMELORD_PUBLIC_CRT, "key": SSL_TEST_TIMELORD_PUBLIC_KEY},
    },
    "crawler": {
        "private": {"crt": SSL_TEST_CRAWLER_PRIVATE_CRT, "key": SSL_TEST_CRAWLER_PRIVATE_KEY},
    },
    "daemon": {
        "private": {"crt": SSL_TEST_DAEMON_PRIVATE_CRT, "key": SSL_TEST_DAEMON_PRIVATE_KEY},
    },
    "introducer": {
        "public": {"crt": SSL_TEST_INTRODUCER_PUBLIC_CRT, "key": SSL_TEST_INTRODUCER_PUBLIC_KEY},
    },
}
