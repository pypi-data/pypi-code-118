from typing import Dict, Tuple

SSL_TEST_PRIVATE_CA_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUXU/nGxb+rZck2qIMztmDWKDZCBcwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMB4XDTIyMDMyMzE3MjkyNloXDTMyMDMy
MDE3MjkyNlowRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8G
A1UECwwYT3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAm8r7ngBPSkz0U2XxFwI0gT3xt/yqKTI0AZiSicyyMNo0
oSHZHRVzIfzu/c+cI2SPFHA0n9ZaswiztWje38uzRjEqD30EmF1By54A6c5pDJgV
MVd6LXafbv7tWxSLdyLPJkoa8gcqAtR1tOFXRHRtKNa6g2thyU87/V/UXJ9+C4eQ
mmpq3goVzkA7ZRx0FbdXwijAGLcL5ZWStUPTaWjR+V3ApxUZYy8JV3tWybEm5FDK
JJOvdd0bJQgT5WTCYRKNYsXyjcRP2ypi/Ry2M1oQLBbqCIldrvvIyoUodbkV3Yc7
AFhg4gUKc/O6zcIO/3PXKgFOAMLangjIBwWc9yyNXwIDAQABoxMwETAPBgNVHRMB
Af8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQCILSP1KclF/iLlNb7w2bE1hZ5/
IJcWsZJSec7vlZkF3AGxrUc2XzdT53gooZqpg5YIdMYqDZqCfPphvUbqGELbImfH
D7sWhD8jU0FsKc5ho6+Uwmj2I5H+xnSVSF8qEbSBk8nasAac+bXQ6cakqkG/cbO0
9HBBHTd6V25KCeyvYN0kyuYMyT7GBfzOBmhyx5zf2L3oqoqVKAokbmC/9cvBXMUX
+1BWyowMjBVH5C5frOymcTF7b3ZlMuibFdl01lVa76QjVno/QMZ2bqnLaqDJA306
f7vTyuGSYJSoXnEh0UJ4IR2ct0F+6JvuTCL4p/b97C4Au+Lq9jt+2sGV9CAs
-----END CERTIFICATE-----
"""

SSL_TEST_PRIVATE_CA_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAm8r7ngBPSkz0U2XxFwI0gT3xt/yqKTI0AZiSicyyMNo0oSHZ
HRVzIfzu/c+cI2SPFHA0n9ZaswiztWje38uzRjEqD30EmF1By54A6c5pDJgVMVd6
LXafbv7tWxSLdyLPJkoa8gcqAtR1tOFXRHRtKNa6g2thyU87/V/UXJ9+C4eQmmpq
3goVzkA7ZRx0FbdXwijAGLcL5ZWStUPTaWjR+V3ApxUZYy8JV3tWybEm5FDKJJOv
dd0bJQgT5WTCYRKNYsXyjcRP2ypi/Ry2M1oQLBbqCIldrvvIyoUodbkV3Yc7AFhg
4gUKc/O6zcIO/3PXKgFOAMLangjIBwWc9yyNXwIDAQABAoIBAHLTHbbrhYU+yMl7
FkGeF3K2ZCT2LbhlTx1qBX9ZBnCpMycb2njsKUqAsOkTDoKriCVJOhAgngLcxA9N
9w69hSmT7OszeqKOAYOAti2dO6HTqbMPRXaiuonFjM2Xi99IIaOX9Noz24vwabzi
ZT6IDTiPYzKff5gvNQjfi5ak2vLFVowAQH1Mf3dh86jvhD9PpLvYiUL2tb3w514c
LhUQtrk9YMhOMmCMKH8HxvU/8IsGhLNOwuOiQ2O6tXLfld+udt93n0JyshzRNcyl
I231KlThxK3BiXku2plE/qw7K3sW01amaVa7trfWxrOv7XQF8u4OOcLO7Wx1O1LY
gfbrAhkCgYEAzmZsCeTMTGJxNbkj/Zy5rU/+wyn5sFl6xfzXj64X0Ri6C8AKNBI7
o1T4zSp8aUGHAg1SAW5OGWC5vVgACrIfIWoFpg5Rx9l1EkyZVczX0tbjLabQeA7j
4rHGrKLK38HFtf7lyHXoGVj55nvlxri9t9X02clBqz2WzJREiaYbFzUCgYEAwTs+
th+yhJIwLIqqSeK6tPgK9Ofp4M3Qf8LD7yOZD8qmVdRlz8H2aJhbchyLGnaj0JJS
lH93sU81wZ4Lo3Uowb1uq+qdz/nuf2My6zFwG28+ww6KHnkss7XGvGQjLLBtLiol
j83Pi5lkKcsypf0psnKV8cKYpXooIod2MyU+YMMCgYBxWh6LcHQinw29i2gQqDnw
zLYFSNAv4XRjt3BLIDlERGgoe9cescS+9rONOYAJ7krO/bHDx2hs14oqSmH7fcdK
+ocPo12We/6nhhnP3SfKSumI8Mwco1DT9v49YUo5iJmkUdCwPtCw2wSjZ/fRIzRN
+dr2oGjIOpLO176sOeU24QKBgE2k3rgT2InIrC7ZsT9rKZbaLJzoK2Q3j1YnDtAi
v7hGt7u5Uwe+aqLwxZ3+ti52CbEfeqtM5O2MZI9eUFLoGu5uje/qoGsXhKwPUkCL
Zv6/HrsGNp20FzBHFIpSuoeUhOqN6PX1vzXa9xKMIdfs+DpKLNIuXWPwx/vH7sjy
aDQ9AoGAUad/5kDcK/FwSklNenqITWn9c/OFecb6Z6u+F7TPirleXPbhNQ0oXUW8
pVVnLpzWWWpu9amxlS/4a4t7/lTEyYaT6rsjJr5ZBvDrIBwFc3zvXWYxbY9hnCRP
LQfRJRhurOJYEByEDjyiXRA9WPHcIhpKVGN8DGyjx/gvJjfTQR8=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUPIoys/kxRUAxhIW+huwsgqplVZ0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCpDfVovOj9fLjpheYdKVwV5V3hN/bUxqlYAW3s+zFU9Bpg
+SnI+5XuTW6SLpiPjx/5kZJsztqxI/Nr7BuTpHUOfbaCHkoJGBAcAkPdnOma8lH7
bpZ8CpVjONeHqmTvsDP2dgCg8QW6nqVksEHMtkOFadTifIODxdWJtsB4KjzKlV1U
aiF0hUIJmbvX08bArrzrsX5EgM3pQV6vgo1wYWM/X9zRjAd0xJDbhVqOsQpK4AJS
zAAfqCwxNf04EHhRFD35Uam4NiBOzR3T8rB4XGcpMBYLPC6reLHtOmxneJ081NWh
ZgVDhxPg8/30Bs3OhNhT9ZlfBJZvPW8ReT/JzHXtAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQA4hi9UEfJtPMsTjpI08Pdp
AMNa1ybci7kDVaMfcvKvMDcOtoCEt5K1t3fGWrYojfgnJnSRJLTSZIa7IdBbyZG7
e5ClNLzw6bCqiQ55mgyAFMFM0VUaYu39zRK5X6fA2qWXFYVbOGAbEgU8sFuOmBid
MjkEQKL561tiibAkVJucp0hLf1xzoH4dJZqFWyFiThH8RTUq4Gd4atH0pzk01Ts3
VbQyinIqEU/gwLAawnOGtdMYdFPNtll0F+lP1+h5AZYtsTcfilm18D9Th4/rfQay
Ob1SSSdL7MXqy0pR9sF/BiXTeXauOK6Y5DooJ32y68yrNKL+TfbEzcPSfqiaK3Tm
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAqQ31aLzo/Xy46YXmHSlcFeVd4Tf21MapWAFt7PsxVPQaYPkp
yPuV7k1uki6Yj48f+ZGSbM7asSPza+wbk6R1Dn22gh5KCRgQHAJD3ZzpmvJR+26W
fAqVYzjXh6pk77Az9nYAoPEFup6lZLBBzLZDhWnU4nyDg8XVibbAeCo8ypVdVGoh
dIVCCZm719PGwK6867F+RIDN6UFer4KNcGFjP1/c0YwHdMSQ24VajrEKSuACUswA
H6gsMTX9OBB4URQ9+VGpuDYgTs0d0/KweFxnKTAWCzwuq3ix7TpsZ3idPNTVoWYF
Q4cT4PP99AbNzoTYU/WZXwSWbz1vEXk/ycx17QIDAQABAoIBACP1aCHjLNveT6a8
aHoDdibiJtnlAYe4ygSCKVOjCpc7ZPEDjrPFb9rEdaR6bND8bJy1LiQey72qG/j0
u9jnvk5axxtePfk5ORP8F1toKPhgWrfUigXQan40dQPSZq3lGOhvqSqSmdlcLWoB
Y72bdzlFjZavTXoV9pnYWZA1y8B7NFnaGfaBHfc1iNJ89cwLV2QhADaYb7tKIooZ
nlPyI4n/uF08+UmKzKEpwtDsxJxssa/J71YrQS274r13yEyYKGhsoVEhWrfD+d4t
BlBWHwFfXQLPVgRQ3du3pvMqAMAMNZEb0k20WeHcaAybRGaEIe6ltqOGH2m6j5uT
k7fYr7ECgYEA1fExK3+VrKKCVSkpRpky0bbLgwS+YJU89kPBurdpVBMxYh9XuGNx
xPYL6trKE5rfSXFP+sz8Vqi7WOEXCFzFx6ZHiBokaVdSWG1Avk16lB30Uu5y/r2W
BmfezbribDM9oQLYLlUd7tAxGU+/SIciREHpfelq+ejLmeWKHdWdVpMCgYEAyknC
2B8w4PwSoDMBB0xD9FM6q/7iaXChpa4n8yl/YLVEZlSrCyWFz0awPHQTOvszE0xf
UJ16HYDktMT3tyC9cDd5UHN89zi75edEMPLmPnLD6K7QOVaVR3X6PUqA0SM1spM3
UTXWFxFhYTUTtudK6rMSseDCxGpY+r4hPmR+UX8CgYEAlNevyL6DyE5rdIolgEt3
MrYFEosLVDCf8Akl0BxoeCi+M7Dwm4T8EvbHRcafzlHyRKtD5I4WhMfxR52aI6Q/
qW4C2Cqv6GXrEUA5SeynekL4x3XDpX0K0jwTo3gArRxdJRbQhjOLlqlbb2uu/eue
KHTe2E27slCGzfQHSkhipWcCgYEAiUS0a2P/Dyz+lqcFs6YVFt7DmaNEkLhVeNBN
W7x1K3LWD3q09sNnodgeD2fVBNkhN59Drrit/QdSKzjdv+7/nf6G3AkCa+Cb4M6m
f3DUvNu0BVlbAw22DuAIBz9fWovCDIPJrdoShWTN5+DUl/Er7UfHD92tTQu9hakv
dd9LuJECgYEA1L3P0JKDoqkgSBEwsHbyScv2qo23xKZsTqdY09Cz0iG8wMkajRdb
QkWj15kmqYjhl/gpgmWfnB4xRmzIhKiI+k2AvVmiS9ttYgdqPwYJdauq4ON/H5hA
dXPyLob4mYRF76KcYeJeVyjRPXwtbojJQ/FFGZSKsuO2toathK+vBM4=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUJ/ehUeJz6rFUOj2Sq6rL4SW0Wf0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCyjDKG7d7fU8ZdpnD0Ba5S3/F6FXpTvUBqxSRWOO9yI4tQ
hSqOJIP9x8u0aFhgmgMN8Rig3JZ6KfvCeQ1qO1xkcuZ1o3FoOOYkhZoj5OKjFQDk
6g+cOSrvUe4QtIaPxlfNhtV0peVQuKQGSOakEyC7Z5amZL7Ypwjbt6Wr/N5gZ2Be
2+UnoCOxYTVvUmOWl11Bre9eQZXYIM1D2oYht62HvGEMhoZD0NSoRsEiHPiJ5Hhi
ci+U/oO2XP9NrKK3LKr9A8NzWB6oHXqw7qidCQqGumY0zhE4MarACVzqJG6kCB4/
cL1I3eSjDT6iEUWwn1OLFc/sdTaB50LNfEI0DeL/AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCfYRU1NbezmtNTU1hvOHLn
Dcw1qrUujyl6XSE4kNPooKreJLQwtlV5EV1h9APIk11jrieiEkxo9IYVRzadyrrf
3Dh4x2KFn+R/m+ybHWTICcBL2FvvHuvVx/ilFraM3e+Kv/s+pQRs3YvQuCYduBTq
SXz12aZO5ttTmG7LK2WcX5OgwC1kmSw9Km2DFb8zu/cNv/VQkRujsG0doVVrqxHa
4/CkSlTBNCBJO2Brhtbpx4F6kKfK6u26i9pW6HHgvctpC5PORTeGofPVM26Hpsap
6mHfYpFu1jIr1MhQcWZss369DEwsSy2nr5/3R4zIDWMlBXEKd8p3ey/wjUk6dD+p
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAsowyhu3e31PGXaZw9AWuUt/xehV6U71AasUkVjjvciOLUIUq
jiSD/cfLtGhYYJoDDfEYoNyWein7wnkNajtcZHLmdaNxaDjmJIWaI+TioxUA5OoP
nDkq71HuELSGj8ZXzYbVdKXlULikBkjmpBMgu2eWpmS+2KcI27elq/zeYGdgXtvl
J6AjsWE1b1JjlpddQa3vXkGV2CDNQ9qGIbeth7xhDIaGQ9DUqEbBIhz4ieR4YnIv
lP6Dtlz/Tayityyq/QPDc1geqB16sO6onQkKhrpmNM4RODGqwAlc6iRupAgeP3C9
SN3kow0+ohFFsJ9TixXP7HU2gedCzXxCNA3i/wIDAQABAoIBAAxh3qsu2fMA+1PJ
VDIIJtPGhheiX65pBIujCmcUYb63qlS2N4JOE/1Imt7zEZX5eFbCLqQRSDpGqRgO
jxib70dkFIl6AUZqE8PapBrzJ6iJr1swxE5gRJL+SpVL/7z+014EiM8jJikX9QAe
lCgyz2VPxMnbWMTrqJicPtgTnFRxGR9KQncVKOyrfWNm6e8r10iMfhvx1HIUJGEI
V0AGsTpfjRc1ATDXvuKJ9iGQuAvhCOrfn75Q7kK1yxKgYoC8DXieIRRirIhoOSdG
nv1FWD7r9D2z7DWq7AVQgPLAuh3ulyE3y+gvDMZcEpYlHtr5h9qbvhSkB3UCfJav
KmU8AukCgYEA6bpcB7FZq9jRhCVcDOK2MiBUfs83IQ8z3/jiYTsrXfqrXDZcvrCG
JzMXbqB/BaE6bA6NQMLgwIiXkTLj4pyrtARlaU5XBUb3KQ2y+xkWvA2n1IVSJopE
dGClmIvDT3usUItcDzSr3uazfQSmjVHkpLW5gTtUK8dwJ34EaXZcnrUCgYEAw4/A
CKT9hqtO+JpvQDlT4NCXTfM/YVuQeIUc9xZQwp7guMEXkGKEbTsCVjGzCVleBR+J
ibg5jgcSjVd6OaXECXbsUufnpQGULbrnD89KmJUch5DyQwVklX5IbzCa3OGvuamN
Uo0ELPi9gxTJkpH2vFgAoHSEOdB942z/IuY5V2MCgYEAhXh/r4DulTz2wIDZJR6e
LtfZiKTqdX2KAR/Onvm8FSndi4YbxmVl5qK9gdYzU1Kz2xsgPNhMooYeD7PBARq4
zs8n3k/3T7Mr14zUJaI5ImCl863CsPGKj+7VAdzmRtB4IXLDuoc4ksypuP3b4p3e
dNS1v3/S3EFC4bqL6HHICHUCgYB7w4oA7ooUpG4CH5qwxpcy/FAFYSCHeO9hlrzS
EylhQjNuOaW0FuVAS8wayLFKBWjfTSo6IoEqRYeUM/yCZ0o9wymk/mc3olwo5NQ+
yS2oixXXJgBsMgmKIrWsyNH5YEtZ8NgjmmM+It2tC4bWX9ILOJaM9bCI9k31lJGT
gKhhiQKBgQCJOyZqyxQXD00jxxAzF8b8EPnculpWG0jvT40jYxoRzrx/+oI1KO2Q
6QFtyBjBibf+wDuXfNDjsahoX8EB3yQX+ofG4fCJ9WG3aNcgR8enPfejKoCzwRNf
o/6JFcAVoVo7l+lwcFJ4r8d1KXbP9Qt7doZSgmGrUSTvBTEWz+j3Ig==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUfnFEiDBphxztIz9efqOLOpYjA6YwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDkLNTI9jghjYaXRMvt/3oFVDZ8FUraVUU718V8vW5NF4Or
I7HYi7EgS4BnRh9CfU8r+mkPxPTYJ7kgjKOcdNGw1ARCiIIl95gw6ymjcXZ7isLC
F+79kJNQSKq6lQvrPoKoQpfy8dgjRaGY7gH3DeX/Oi/QFd3N0C5ZGpyzE7+VmONg
gzoGk5MyLbBCcKcOsBQUqOR7p2bEYXDDP/xl7+u3R2rhWVsp/E9W0eJJmtiVwYrJ
y6sbzcWBxjCM3Rv4NZs9tTH19EHWDJM4whHgnEiB7eXz03+0tELhnwkrrm+a0qC2
uVqzG9HZ2/hVY0VmPyPVprAihsAPLyJlnpArCs4ZAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBUBe8jhAQgvnojPHIVbZTy
HyzRwfN8bx6sRGMzRWR1nFuSgeYz9ngzanf6adVCh7K7O8O1dZwdaPPZB9RKPKUH
0oPYPwhSyvmT6so2Xr/YB5Yx/KbrSK7dMlbxQ+9ct9saKkaioVfo7OvgOY3fFg9k
Qs0RwtRpE1TjaSJw7ScwlaUR7GYUrcIBuCKROcZJPTQaVSM537SOFQXqUn0M7Wfu
QM4545j1aULGnDzbP72fpk/icndS8ArmvAW3JpIe+HFk9IxBuzUh4HKHzO3Dny0l
rKOiVmeztN+a8mipfJRTveuZs/QykCugYkafg+nB9GOTjyBwZzTD6IfW1LO3UZLt
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA5CzUyPY4IY2Gl0TL7f96BVQ2fBVK2lVFO9fFfL1uTReDqyOx
2IuxIEuAZ0YfQn1PK/ppD8T02Ce5IIyjnHTRsNQEQoiCJfeYMOspo3F2e4rCwhfu
/ZCTUEiqupUL6z6CqEKX8vHYI0WhmO4B9w3l/zov0BXdzdAuWRqcsxO/lZjjYIM6
BpOTMi2wQnCnDrAUFKjke6dmxGFwwz/8Ze/rt0dq4VlbKfxPVtHiSZrYlcGKycur
G83FgcYwjN0b+DWbPbUx9fRB1gyTOMIR4JxIge3l89N/tLRC4Z8JK65vmtKgtrla
sxvR2dv4VWNFZj8j1aawIobADy8iZZ6QKwrOGQIDAQABAoIBAAK9cxSyuDvW6j3Y
yqYiAkIcH8dfrhVvHrS4Q5va3n84gBFHDXSvQMJFhdY3plpzDMdXa3mQAOyzlWqJ
pdFUKcx4z1BJOV7hWUeFG2vmCekz4mDYTrtmyA4XwU0aSxlZF9KTciWtt828oVMn
0Ig594AYH8jc6lv1Wwkg467W1t8iABEthulRcdZq/xXVqT8q9uq2BYqsXaSN4oFG
Zg7LnCXFt/XfuIFs++mI7NZQuF5v2EnKWaDCWhpVMWvUiA+17r2mr+Qrbol+TdGX
WHZqRld9Fj1XzPLgxlqfn6AMLlgivTp3NrgLAkvNZ/aipq63KIfWys2p9DbavhBg
jJHYWl0CgYEA/fo2zXk7IAOvjKxenrDiqY4KWduD+Ww9EpStKuoauOcrbO27p1CY
nRDK4SRAUO+AI7OQY0TZHwLuv2/pyHZ8bvvJSHrecS8PUhV3mJhOVupl5JxaHtYv
EEf0+L+irdNTXUAvOCKi7KIB5mCaXGhdSw+raxj++Pt2QaAqOclKH3cCgYEA5f4D
h+0wY5zRkuOSKzpHC6Xd49plCDTW7jtKfx+PR9UIPIoAd0xhon20QsaDnl5MOf2g
ojvNAqdn8uUERr3nN3PgWcBEGd2wYq0ooGUD24yoTASDXgvTMNggYybStFbrymPa
vvF+9yuWfKLwKpSKlxEEfnbnxtBm7rg+W3VLgu8CgYB39fZqqQdXQMZrUINEu1Hk
OlYDSV8VsZ1LKHR+n6LNkUr+oW+QQM5E6ciZ/RBv6iABPPBHIx7WugDg5VBsQiLW
HRFercJhfZPj9oXNyqq9/OrxxzP9+rayHvrDf2isZ/OpSQbEof+Ie6EgGqLuYNEo
Ahe6d0z/d27M4oTvVHcxUwKBgF/Q1lm/iARH5cujQVb+/XAt1uZBKwwjL1Oqodua
I1ASwU6vU4hf6uEOK5YSK+1DbdBPCKft7/fmFFlN7d0m6nfgr5vUjMqV4BEMALvp
uZSy4b5htvTsSjy0HbIRD4EQIUV9GjmoVHPW1efw3ctvfNl4vn2NPfxHAEr9uQTT
NfVDAoGBALk5KL5Q6pAbxqaJw2e33I2Y7sVwKYcRynFdgi4oAcspQdt/22h2cBwO
l23240xCSSbf39fhrDJCZ3v2lWOGQMvdEq1i+9btj0FwhJPmcLGMOIIls0ycWYIw
/mrdq5dl5C17E1WfbzE1SMBsCeLFkaWa4l37KxN1o7Ck3Sl5W2tv
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUIYvyPYsDrigeLVIkFXsvpHrP/F4wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCpwUvZ+07XGeclurl24s5mocAP/pmlUQU50unzsPRWarrt
4DIjFX4CUErlCnwGKff6sXkSNzJOCNQ4NQXIJ5imbEvx7d5V80z/5Phus2JsY4uf
IZ/LidOk4tSlUpLDuYURCziqy4fljEY4M58zfgCBHz2aBsLE6LJ7/WZSI6LcXcs6
p9UkVY74uSfnFjVN7W7ivNutdv/vo2qsWPHojn35yYV2JEBje5LMtw+7SDJ8ljMc
kkVh+67msxiLlmxhZadA1eTf31kyceW3PcXA2rGqTMIcdb7REjOhA4kPgKV9R3lA
C0wqWEvufnkh2FuiOjI0mcYguRdvRJQooqMDr8KhAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQC3nE/WNyDiL0+UqIamE2ER
Xii4bQkuOfIFQKn13ciD3hxBI25sDS1T7ssAk/XvKxgMij7jx7vtRV2vJg905c53
2+QxDkkCOO1wrYsvJfCNJ5yz2JkO0eXG1RLmIViixLoyipjEDwSwPM7SpK2LngsL
teV/CKkQAmdOIXB6e3KMv7DvBHboGmm/cv3JrKdLxcQd80HigqNR29nPAJhBx4T2
VZneCNnrErYn+OsaM1TdlyIoTF15Aq5fJY5hfK3v5xLv7JP6X5XqXTVh8Bua/A9B
7pWnFtxNcMr2NbC5Jfmu2Zgc7xTcB1M0bRVSLO4ytMFnBvm451K3Awhz25CRF5zg
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAqcFL2ftO1xnnJbq5duLOZqHAD/6ZpVEFOdLp87D0Vmq67eAy
IxV+AlBK5Qp8Bin3+rF5EjcyTgjUODUFyCeYpmxL8e3eVfNM/+T4brNibGOLnyGf
y4nTpOLUpVKSw7mFEQs4qsuH5YxGODOfM34AgR89mgbCxOiye/1mUiOi3F3LOqfV
JFWO+Lkn5xY1Te1u4rzbrXb/76NqrFjx6I59+cmFdiRAY3uSzLcPu0gyfJYzHJJF
Yfuu5rMYi5ZsYWWnQNXk399ZMnHltz3FwNqxqkzCHHW+0RIzoQOJD4ClfUd5QAtM
KlhL7n55IdhbojoyNJnGILkXb0SUKKKjA6/CoQIDAQABAoIBAGhbdWb3UJt5yBjw
to14lwyPCYSLrybrLPxERiDSuxLZIDuWZRweXU3M0I4HqQEdEd6i9dwV5K4GTXiU
WA6ZEQXWc8Wxxsot/TsfJv7e9nXNqIrWX+b/vwWRkMplfeYnCb/VlyugXdXnK0/n
pEpCfsriSruCxn/I0djZieqbD8bKPaCNkHUqcQsgibxC22qYF5U8ShGfuqc8X/Vs
df245Gcrh0QhCf/pTau4qPi+E473LtcM6bKjSR7EJGCCQCQXf63+TP6G8b/PI7oI
ZoCVEImrtEFI0rdC6u7F6KWCwc1PNhE549TkzkC7L+NpnP6EGroRcPzXgAzz/5iB
+Yju3AUCgYEA3SWRPsO3E4Tzvld5YvIFG9Fte6oIrkpwJJ2NfCVtoe0a7YOQJ5hj
N2qNGjMszhQF7ieG5IsBwvU/cAfTp1SNh8C86ScRwZsQ/IK4iKOVY84u+qCLxZG9
4m1ZJi0Zwuo0i2Gs+T/wbF88SQAErVPdDf46hAQVu4mUs/019/RMTPcCgYEAxIJE
9aIhYa0p+RuIQw1kpCMsFr6zM6384aOV+zjvF/FcHvsFajcJWev+qG22OHAYRGjF
6RzJ7KRMel+dYMyrkdHwPA1DFxtXTnge7zg6P0xFVxysBw+GBIXJb6DGNqhkT1tP
KaQOOPOwQypJjzVXPknaSStiA6EwiULxltRK/ycCgYAdH9B0GqRmvrC3FaAX5tXD
Zx5rFeaUxZrlR5aVjfxVQfu04gm/HTOb3b19gNXawgpR5gS+3ou52ECliXJXbCxD
f5+heRK+k6R2DOUuoZSQE1xeh3xA5cPDKTF/dJsa72tCG/gCz2fjbdtrpcP3676G
FEAymLMgAquB1Mwhvpu52wKBgBc7X3O6yz+E/WVZ/+4Nc0yEa/30ZbNCapcyg9TD
kmC+RCnVe3pnL0/WOrEm51gcyIGt8Vfx811qvy/ohe6fw9jlfQVcfAYLUXMReHbH
qvs4xSnbVesvxqRaPMpZs5VaqyFGpkFCB/xrsvb91Nx9becLTCdCXcAYGmjf5Tfz
uToZAoGAMYalPv6XvJBf3CvlvEeBGiXDfaV4O+3t1kevtbSgrrV6pW5sy/WwUco8
V7Q7wLdRDi+sghPqhxXqLnIyp8chU5LMOwEU3m2kw3pH9ApZKLmaUbcid5pS+4rd
G5puMkmYGwaZRBY2HGOXMA0kdYXiPw2y/jdH+Oz9DvWd2tVL8YI=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUSORAd4kBPC4fSPqHEQskE72Yt1kwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDLIIgg1ILQGtE9Rkza0ieGUNn6wDssvm0fkcpIZXhrYbow
ClydjwDMQrLHF295ZgfkqDEmD5MUeJTxBNznDlZtkvBIRjPN+M7ZnlGJCUTc9jex
U0a/KxrK6ygsaWNzQ8eNaTNOAR/l6j/kuAUC4vKoYKGzLCW45LlKVB9xQDWinpov
nXpA6S5UUI6YxqeriHr2IiLtXSZmqb1lqftTGXenvdnHrJEmer4iYjXHAfMhq+5/
yHCZmpy4IAX39zwAWA9FnYieGSE8KyEqZW4HfF1Fe3V9C6nsZ2gVL1k0sgAgJ8oW
3CtM8tljHCmyxxD9EHSjJAkSnY3OqU5P2+XMbNcJAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAijxQXc6ndCfyUhP7DmFCr
OR3jfPd7Bvc5M306CepT4ZGxXrjgy5idkKS8PAdSTMFJ/h3ShkGatgnb/OoOqiMh
YV78dx0wr4/sdEauPHODkQXmtPj+u2Al9ZyYflTLeiMV7JOn8H4oEE+r0Ra3o89P
F9+GOd/jnF8BpO5GUDN0nN22tNid5kIepMNVG0L3iDMGSDMzcXbGE49a8FPc4CfK
24Fd6BZ2YsUM4NWQ97lfGKtCsnZkChwNVkSkVXP38Zvz5H+sHaMyWQ+hiNBlB7Up
OrNw0uq/jvNv5IGwx/JEuYuXXfPd5CvPesk43ycsBvbjyYFSOsdzU55jEcivPQNW
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAyyCIINSC0BrRPUZM2tInhlDZ+sA7LL5tH5HKSGV4a2G6MApc
nY8AzEKyxxdveWYH5KgxJg+TFHiU8QTc5w5WbZLwSEYzzfjO2Z5RiQlE3PY3sVNG
vysayusoLGljc0PHjWkzTgEf5eo/5LgFAuLyqGChsywluOS5SlQfcUA1op6aL516
QOkuVFCOmManq4h69iIi7V0mZqm9Zan7Uxl3p73Zx6yRJnq+ImI1xwHzIavuf8hw
mZqcuCAF9/c8AFgPRZ2InhkhPCshKmVuB3xdRXt1fQup7GdoFS9ZNLIAICfKFtwr
TPLZYxwpsscQ/RB0oyQJEp2NzqlOT9vlzGzXCQIDAQABAoIBAHEcRnFxpP5ZUJa8
ZOOdDuFeeGOHU+xQhdeEiY3S40F4hANoYbZjAWC862yuAicpx89uUSAOoCpQEzA7
Mv9/HmWZ4y972DEkEZtg66pRfQVGHjEiXEzrpdnFJPPGI9j1r1Nxd15Chg6zaKzm
Q/QdiF52oNRzCvZwdzWKro+T38oTZLaYF/GvHZ29ikO2v/txEhY0E6Ox8PjUEuaE
CH+SoCqAkrpyT5ue+Zq76M1mB5krnLQEfoyHWSKykeQ9svSSrlpa8sJvAufSG5xS
xgqh56i3pGsGrwP5QLC6j6sK1hnknvs7U07HFZ00WNON5bYQTqd11n0denPC1xHn
l/O4AxkCgYEA9i61oB6TbS2KK7RAKRXiF7uIKZgWBv4yv/ynsf7d65gkfG0XZyuP
UB2yCn5fn5dLvweHbK7NnzmfqqiwNQYM5JbPld/eqzVs8s3B1M2rWTLugfZZ8NeE
W4P/mYwdpSpdQiSgBwdlolAtIZcbQwfujEXTUK6ZjDaYsHsIuW5CdLcCgYEA0zpE
ePAZ6KAC89a6IDvErllaegPhY30jIuEf7JFBAan9o+4cmzp4WXsaLkbjeSjnI1Yu
czUorTraK7OCLp+tphSxbpoE8T5OtH8xB4gTFGmm4lz2UFv5ObNpA9+rrb6Jf0p6
x9CyClTKF1vsDTtWQvEg+kDisE+tNdLtHYBM0j8CgYAw6XTinFCUR5EFP+njf9qM
9pCGGxZ9SzIQHQXAgq/a6D6PjikxMWFm/I9sMFGVZr0A9mD8wfpOoWdMw/lGf64+
GIyj7XfTMmk0EJdrTXW24jyrC6QxCtDcUeyNuF4He9RNmPNGkjyqNB3TZ69d8Qx/
SDxE8nvFdO9/WOKR3QtNHwKBgGQhO/JEh1Oh/qROhv7etlab3ur2SfLakDxpkbOY
C8PZLHZ4WrEvH3vzgi6rxgtaW2+B3BUa/wRXYLLUroKhiTSwnIe8lVky2yZvIPPc
CodjqgumW9EuOE+k/8QpVH3RU+a2jMuJ38xL81ztY1HGbhbfrW1UMuG3c3mPWn3g
owoLAoGBAOjm/N882BzVt1wK50hYf6ywdD8RA1UJg0T8XN4meoruG0nxHo0LJG+q
ot0B638GSG9ESBbAeYxQZ8zqgH5y1DS/O7xmLnHNck7Eu7DblJeQc496/yKW7Uci
cGosIckRRVM0Dekivt3fxdIvct9UonKUJsAxoZsf+fnmMj1QTMai
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUPNbZirLECcLXWjdq7AF5vdOX4UowDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCVE9/KTj19nPrT0DaIRmLQBhJCvvMsJnY8Fa8R0hfM+g41
jHKzvriwD0yArxbdj+eKr00ZWM9PCG/TpnUkW33PSya+VQ4iADUTcD36F/5p0sfe
psu1+tUf7MdMGERrRnNwG/xTAo47whrJ7QoIYWjhtiOREjImBjWXRgatT4uLuNsj
wguPTFQklEH53mxunBago7qJLwJTFVJ+hrxMuHAwYHxhdNKA18oVKVcg1zE3JTwH
wcY/n8kvUXK6L8GJ3Cororn53ej4KBUbvrsAs6AXtpwUUQy/H0s1ZkuF7r1nmUH/
zGvzrPTMnFvtRA3yyXxpjG2mJvx0svwqVAVV0HpDAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCPL//viWfMURAJWiGJZSNH
uy1UWUkt/Ga5zIdr+22nHPEXTE6H4+TbDKomVa7xJebZ/Pr0zG4Y41wk/l65Qq4C
5FBNiGoLTO3T+6aSCF7iwUoWRW3leCL29TZrX3AG+R3CnYJnJtGpH+vmqb4lp10c
duCxdd/1Foe3V2Hc1QhFRwd3uG9wYJ1VL4ifjghT03Kp8UcPDYY3w4A3/QEjVMsl
A0pgj34t7oiT/K54bWtkWphbDu5jX8JP8+A01CXS9njXU1OXEnRKq/x2OhIFEAKS
eKywXcUoqfNpX0qmTKSahTslCZu3kUtOgyHQMOJIceot1AZ2hgzDmmEL3+DD2gZ9
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAlRPfyk49fZz609A2iEZi0AYSQr7zLCZ2PBWvEdIXzPoONYxy
s764sA9MgK8W3Y/niq9NGVjPTwhv06Z1JFt9z0smvlUOIgA1E3A9+hf+adLH3qbL
tfrVH+zHTBhEa0ZzcBv8UwKOO8Iaye0KCGFo4bYjkRIyJgY1l0YGrU+Li7jbI8IL
j0xUJJRB+d5sbpwWoKO6iS8CUxVSfoa8TLhwMGB8YXTSgNfKFSlXINcxNyU8B8HG
P5/JL1Fyui/BidwqK6K5+d3o+CgVG767ALOgF7acFFEMvx9LNWZLhe69Z5lB/8xr
86z0zJxb7UQN8sl8aYxtpib8dLL8KlQFVdB6QwIDAQABAoIBABW+c1rXtKJYvkEc
0odn9MuwxwMTRPbAmWhEJWftA+my41WuKaDMBbYwVRFD+IrSjYwt64nx6TL24RC2
68kkyyHsLTd/wnL1Isi2C2QqEcKvqtVv8LCXaHSinaMcuwYGnZnRiyk0aziOJEgl
mdwFET4yyddEFypyp2hsH1cyDgGP+O+8P4JKAVMSrtCCM/+5a0fj/Z2TUIEUDkzT
OCIY+GsKDwE88VPErSfzx6gZPWpPkQMI9evhGDKhwvUuBNgKal7oeSRbzxQ5Ihj4
crACs07FTRrrEB3TG22cPk+gdMvM6nEbrXybIjLM8XzOpmw6M5RQdwYeO+O8+4en
YrH0KhECgYEAxniu226jcNCbl9D2UHEm31fIs6esyEz3IJKB1ZC2FAjQJdZ0Y2oy
KRAIxDBFHY96yL82vKXloT1b0LsBtsTFJLrqLGtiuoxLgUxNtU7s4r0aX0GjpStW
Dk0ncrInwxlh3uYcpM2Hj4qjNam0UrttDr1/177tOwaPdER11TkiRDsCgYEAwEn9
HSb3XecbMD9Sap8ER7hIwxU5im/VopDzHqvpOb2a8TIQMV2rk48htZIkt0yVf7hv
X7Sx/FpaZOJPfa+ND6KeQKw1noajEeSHxLz13aOnFlUtSHzNTUcqk2oNSx+0lP4n
C3W5BJR0fsgtcFAd5lxEajwIxdmPnKm4T2j06ZkCgYEApE7k8+T0ikEpjtYAFTiX
5e7WyWTXNjwBm4Wu1w+mrY9eQvT4BhW00SnlGAaeMYrHK8qhliwBnysdCADJunXM
gEv98ig05Buhprl029UrZ8sGOjYtNGBcLhrRvbKgGHS7Ab2fmRBOWhd8ZsDH+HYS
I1HetM3ruCIGQUssAgn6xGECgYEAke2UsbMIt7LT52Gm4lObo/IvBh3tdSo6Lw1h
9Dzy2mcSV0lvEIfN1kYhhvJJ+vGb4znNDAzNpn3LbBRzzyaTHvKCtwH6DzyONN4C
S0Q8MuAnxcMOgpx0EdmYbhdlz0VYfloCt6e3qcogPrccBMhIaLJNGXJGFiBt5K7I
uTsl4sECgYAmsWXL22XeKAwv2JutLK5Hz/xn5BmzFDGBLvu0+FVml0aocYVVyQS2
mzs2kRoJdLEDfcxibawQimTuCs53PkoKVNHB2JzFS8HNHdcFHaCb19ZO0NoSDbst
sSu4qj9TPFACKOKsfRpSIWoeHN/ps24ost1vE183ARVTsm8KTHgEJw==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_HARVESTER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUa0HzW3fH6O0kNO3yGndcTG3+kX0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNloYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCtlD5CM6r5C3//rZwWLmMHcIO3lDFfdSwrvONmMhwlkIDU
/FgLr20ZS6ny7DPSRVuU3jijL00Q6XZqpmmzsoN+RU6VITNuam/gB30E/WfF2yds
ifWtVpE9wM51V1SigEtAIviooNR/CrfXxaljw1wmReWjCAUP4MWJBBFGUymWpBlF
vEo+7VWZ5B4bfstRTZaFWRln/otMh8v3SOaJSmNafsDnulq1JXJz/i2hFfPjgfbo
rGp8bfCWpNmEzJSn+CY7aAyW9eKKR+unWzM7+PEnI2l+5rrq54BfxpMdfAFHlMK4
NpIrJNmnjMLm1VQpm2/RFxI3LP+IDedCJmWpXbRpAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBc3mZ5yN9pXLT/0Io6Ql2k
SxPSZc68538f/gjpnlXDxApiP0sk2RvAL3C3E3RCH1KeP0wjcRnOwE3J+BTaisGW
BbSQjQMnGm/zKtkwBaSIIjkKXSRCACEzneTMxPwEqCUgAWJMJ2/vzgmbZcQ7TxHQ
UZpOnDhjknCLmxxEk3cGk6+1SIAO9NQF4z4fL5grfQup6sBeyN+srl0WnUFWfBIi
d/pZHcUCKL+FmUrp6eCKGAFGQiM9TyJ62H4Cs/J0bR9e1asLOwSAunTB8+JnQa18
ug0LdcWQLjcoIMaZk5XIn2wlmFIsTqVXS5i2Os7w8tb/XtdxL+2Qi+Hk0oBmGffx
-----END CERTIFICATE-----
"""

SSL_TEST_HARVESTER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEArZQ+QjOq+Qt//62cFi5jB3CDt5QxX3UsK7zjZjIcJZCA1PxY
C69tGUup8uwz0kVblN44oy9NEOl2aqZps7KDfkVOlSEzbmpv4Ad9BP1nxdsnbIn1
rVaRPcDOdVdUooBLQCL4qKDUfwq318WpY8NcJkXlowgFD+DFiQQRRlMplqQZRbxK
Pu1VmeQeG37LUU2WhVkZZ/6LTIfL90jmiUpjWn7A57patSVyc/4toRXz44H26Kxq
fG3wlqTZhMyUp/gmO2gMlvXiikfrp1szO/jxJyNpfua66ueAX8aTHXwBR5TCuDaS
KyTZp4zC5tVUKZtv0RcSNyz/iA3nQiZlqV20aQIDAQABAoIBAAhgnjydt8O7TVsu
qtjbNkZWpNTIXzWnNxGJVURKaNdbSQx+fVVbCx3sa/BgfAPK+yeNLhiaINMPIXr2
OyXEGNqQR8Gkz5Glq26ZjeweutJuyFFRuzy5b9sWIiDBrUEGhhs7VNr2oCrdfo/4
Zzt8Y0cpmnKq4Wupwn7hZmAJhXlSr9deWrWUfzEbgzuqtMgIIVI9VWqW+wxCs82H
WxzD5crc6g9U4eo541wOx3eSn3Ni75Hotnkx1Vgs1Od/ivloYHAISDcbZB89C+c6
FQtEiOphj0xU0V377e5RNNnjj6HXwdRti95YpQf21cGol2JRngR/w+o2AQuSO8E5
TqiC2wECgYEA10jKJkWfGBcEd5s3SpP4j9mFrvVKAOeP1XDqwvs6uD52CkF9k2O9
+Ja7O9QVxKI7Jt6fHISkrMY1srms/VGw/9R2lxBMHRgrsyZZUIjPSU09qwU5IORw
4Zv52zWqG6MQZu1dUsFRBsu5ibVbdzTic8G9v4V/U+fa2uz6cgLiTEkCgYEAzmhA
PL7acIhmtGhTxNPrnnoUB8sizfTP0E3xTytmTjbtr+lrNz5RvOIv9owp8hEWqMxG
ag9lBdERQnJhrW++ivjkprQZmyVzS9NR/XYXG0W/FSqYLZZX3xa/bmh5eRM0qcyu
AQVDfAvUs+7Wc0LTV6t931zIhTcz/jZ98wR85yECgYEAzKDGbKxedVJjj6B8ZKnT
aD/U3qEOD2ALClEDBAQyIzBTmJn5V6BF0MTNASgs7LNbUC3oxP2bXRIltlTghgQh
Hnp/okT+Y+U2nFlGKdNwW/dMN4OGcqpQVVGho2gV4aEUFRFnVCKl9rSsDaXRY7Rj
zq2Hw0SL62AFWXRI9Reiq+kCgYAFqnjw8fA/HI9tLlv2UDbsj79TA3F+I9U8i5cv
LCrPxNQ7evXVe2F1BOR6KRjRq0Rq98iLCsckJLwLjeY+g43AdNqZ9OGrD5kdoLxk
b8RsnDqFkzjAL5tT5WT12+pRt4Q/kP3Jy2Ix2oVJNyot2czBYFTBN+PNPFmyBb7p
V9sx4QKBgQDWEIRplbm9f0NnTBaZ68qMtEt7nXMqEv3vjalTeriB+X9GJKDKz4Ym
slr2WOPJSgmZApbz3B8EJmbKYys6gE1z0dN3Pl763YU5EhM6kezEX2C5HfL4iSFW
Obkbg7hMBYQk0faEyd6dReIZwVHD7WAf+zCvh9ZG6l4ic1wQs5kYfg==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUfogbG84aJo97wy3P0ZHAkXShqO0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyN1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCxBstxYtPbm7eb1iRbL4SZCF0xIueUH/gZ5nfj3Tbo9DIn
QcHVbNkr5XxH5MBtQcT8bgF/tgBkj7uuFTymT2EpBrtTbdLCTsZ2eMQIABOQ4APZ
NKDiYb6g95JC7vdmuLfuB6VyvlMCZ/Ffyvow+PCgpT7ElNjMiLf7y6mcvzgNKSLN
JYqrJCf7vT0a4W+isck6/fD9J1RUhE0Xkts5wmpwJQGsRYme2hNy/PmCcEY9rqpi
YOxWWeyLbdZ4nI4OH652JwXKUTijqCZYc6+BoXfjwZGq05WK5NhBZVnlYMd5ZFab
DnXGR1WC9ysv1xkFqpSfPlwSZdZcJzBnXXwhJ4qrAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCYInnIgvKBvmX65bVLmhNt
cEUickmBTKOEG4i1yovVcDPIPLGH+3p4Oxng+N9zJh6n4SyCeOou30tRuNEunHOC
PmixRUxM04iNm5lLLdS8dd+kErpX+EYT20amgbnN0HNDRi7+EANXTm2ld9HD7skb
M6lABrsQQdmepdNz6609G0HO/I9rdUy1GaXlwd2th21VyzKmmq28nIT7KidBoQNG
MhTjsnNrZekjW/k3sJA9nEhyERmdsApb/TlUV6A4ttQZOqPV3ClkumqQn04jLEhg
dBNTzK0UEqdVXrPRpJBa/gSkSsCWXjMhwY60pHDsDmnOQH0kLQ5KzPU7IF3x+l3M
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAsQbLcWLT25u3m9YkWy+EmQhdMSLnlB/4GeZ349026PQyJ0HB
1WzZK+V8R+TAbUHE/G4Bf7YAZI+7rhU8pk9hKQa7U23Swk7GdnjECAATkOAD2TSg
4mG+oPeSQu73Zri37gelcr5TAmfxX8r6MPjwoKU+xJTYzIi3+8upnL84DSkizSWK
qyQn+709GuFvorHJOv3w/SdUVIRNF5LbOcJqcCUBrEWJntoTcvz5gnBGPa6qYmDs
Vlnsi23WeJyODh+udicFylE4o6gmWHOvgaF348GRqtOViuTYQWVZ5WDHeWRWmw51
xkdVgvcrL9cZBaqUnz5cEmXWXCcwZ118ISeKqwIDAQABAoIBAQCXksvK7+WaWYAi
rH5AnTUZmvHASrSiPaU+9/ibYCPN3pi6yDDhPuvMDBgXrqOcaP3zbXVXFkzLzc3S
xlhBxiHY8OygCJ62xKBlfA3NE9Os7kIdTlSawTpptNDFArtOdsb1xhJBZvjITJt9
e9ww5lWSFyrhQtlGd6GgtMcrcQbbLHqP1bKKSwPIYI4V6OjxBRK2QPahgrudPdNp
C9C9GWCO5bVary0uKfbXvgHhUOrqC2ogtmnOY41KilofbxCRX7Mc7uLzR2SALKEz
FpTt/CThsWt4IeUUvxSOWtpUa+qIZ2U9zRZZUxIwXx9I84/K3unbk7REHG4RHspG
itgQTD/xAoGBAOCHw1v7K+xNRrDbdce5X6+jJFdVb4NNXkkWPzqD7PuGEdL6LUuG
lm75CAXx0YZtXATog93Fz1ZDBH96tLPzI3qxIEdoU2i+iPWFv9q+SMA7IHNqc8V1
AL1XUFWnJlfTUGihvlHGEODLIZ0k9JpMPwDIdrxp/kaqJGkJ46Ue55BvAoGBAMnW
k7m7fI2aIfRaiuAUsDfaNAk73N/M3XmA85h+h+o3+hI8OYv7kCnK6ahD6vHygpD7
eLJQgD3XPEpKswgP+uUt5p4cBAkt4gGR1sSVSEMrc7OJMF7CTYC+c9U/SRqG34V1
eYvCorVpbFp7GbY3WbDJwJbtPnukaWlVVPvwTQ+FAoGBAMS7UBp1DnxDDXCDKkTw
kP2k9X+sNUQX80gYvRf5ZhjQ1SdF25A0gfUEMNp8kni1s439aSVVYCEWIYfNLS4L
GQg00LKgn4zEfd6a7YqtdbMxW3KlUIEvzpEYQyR5i6giWG8FYWvnHvzIH1DAg636
pq15+EeIm6qxA6whZRxV4tHzAoGAJnp/4zK5Bg3SV1FDlICdL6irru74prnZpyZM
SlAk/SP6yqsslWE6FJ2YefmousNu3ND0K5ppOGDmH4uqIelZ/YMIqi/RHSbgJUh2
VzfWdOe9wQZwcEA+okKstoTAHQyFZF4G8/wBJPCaNY2uUyyuLqPn0V4dQVkQt4IL
F5SyPDkCgYEApt5A/pc42+/bxjxw85ENMO26eJJ9YObUgZUgi+BwR7BdzpmTfxfm
Ubbpg0q5RA4hFofkdqQkPxx9A3Q40e8BNGto2NHKf//jhBCvbZs0uv4akAv7fERy
0SMTECjuLplUvSyzUQ/evpXDRkN5CuH7eo+GuIJPPulPCs5+FUo5TOg=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUT43GvhVmx9CzguV2nwdektqBaZwwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyN1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDRiTszw1IkIr9n6KjMvgS/9I+p+La/NwfFPsIWkTE6cffr
LIi9H+yTMTM3tbNXM4JhvqdeN+c2mDAVjhoi+AAQH3gkpXitxD4ZjYzCCTtwd+q0
gpCKLPOmKxYjqCcNkmEc70g/QOs95HyDdvLL1G1sgMnhldGuc0a1HX0Te9nE7KkW
40Etk6lhEKEa9o9rEjAL84Z6kizKELOtjgd5wM3FaAMB/UIhf+kDxB5vtAhsKewb
2Uy8wMpXJW79cqfLxgjDhd7LEZwSba2Z+XRDD+B+NuC58cv8H8y6b69Rwjmya50X
K1gW5/aZA2+mo9NlSAMdlOM5ntgd2Cbh0zg4jDPTAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQC//83StmG2IlGISJqGVwSj
B+Jl/eodYO1iYuWtCfobI/WZEz7Noqtuth9U2Pjc/VDImy+w/x6XNPTTa0MgUnqi
/GHG1qRIefWrWp00C7fFbrJW1llYv/AFZfgYZB92Vr2X7RupnQOY2a/XwT8dzstU
ZPTNK5wV47MmUp+u7p2Q24ywS+GuQTK7IZnhQjP7ttKKBgdBp9evHuT4B3yl7qUK
JWb3nAreUSESWkumSXlted0sDQQ7ahilzHPkemRgJZotbQID9sV7WqHYMCRtZENX
53jFAQFtxj7mjjacvwWs45XgEGsr37LjCBHUHujVEccfGXN9+LRrpS6pKiyJeMg1
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA0Yk7M8NSJCK/Z+iozL4Ev/SPqfi2vzcHxT7CFpExOnH36yyI
vR/skzEzN7WzVzOCYb6nXjfnNpgwFY4aIvgAEB94JKV4rcQ+GY2Mwgk7cHfqtIKQ
iizzpisWI6gnDZJhHO9IP0DrPeR8g3byy9RtbIDJ4ZXRrnNGtR19E3vZxOypFuNB
LZOpYRChGvaPaxIwC/OGepIsyhCzrY4HecDNxWgDAf1CIX/pA8Qeb7QIbCnsG9lM
vMDKVyVu/XKny8YIw4XeyxGcEm2tmfl0Qw/gfjbgufHL/B/Mum+vUcI5smudFytY
Fuf2mQNvpqPTZUgDHZTjOZ7YHdgm4dM4OIwz0wIDAQABAoIBAB+9ILmTgXK1zLZp
mIAC3GdTHRvK76uBI20uN2oBripDLyFxSnkTR9t33WE35aV0yPATV/i+kQhE/yuU
rcLUO/Y1PhaW9fOkQR/PwB14FofPsj6LdGdprbJi3mSiSOAWZx1h5VindbqXTIEB
WH+lermvvGSuM+ev0GsIv3RfEzpvtHYynKTQ92PDmrbJS7/x7IQGl20UUyA6T9lg
PidOesZrMJQuJvqCWfqp/bTYuwQPneawUsV4vNUxuLcd4ZVNPDJG3/Q/YtwpoKu0
UDGH8DnMkqn7JVKvBonDhlARdtdJ6h7g2NmwPTSyKZmeNjwKy0Vl06bcY71PNRZB
8ET8PtECgYEA6dUyY/CkB5B46eD5Qpm2Kd0gsnCxaSvzvE1LC/2xIqeszKDjsjj6
rS1zz8Fr5qsyYN/b4Liq61AR+kUEHcPfAgRggq8Jy8965xBFDuqTCdtW6jADQ7VG
TrwDZMg/byBqQUbE7dScCl549xItUKh3WgyjZVbv6CogaJyrkq1S5ysCgYEA5WZi
utnrUfSedb11LQPCFQnJ8gnvnOUsnigeRaMxArIXj2qmADmQfZjIoDOfHoKEbRR5
/j2bHHuZTJ+2FWLI8cSCEAfuxTXCCj/SXU3BnzlawTheUQrvOddGWstUCh50VoHM
XPA8bT+9mfs75dXUNguuFHidfS0fr3tCCkzukfkCgYB378mj51dLJfhPBfz0A0Gj
YW+W9ySYbFndOMwIf3xu6RBB+TgxPvadAxZG9s/whdkWRVxTfIT2o6BE/UdqOQBW
2YXjIgLlTiuc/wRc7Ua0JJQFFNFn1kAUvG0FMY0P49F8X988mfPbga+MEv+5Ql/N
iXP508jEDW+IGOwMFOjT9wKBgHyePDApRe7FpndrroX/rqVjJfN4dlSTIsPgI2HN
H0jJmobsdrVUkCvKneJ5aI1YdbwUDZmRufulIUhA0teXTHYaPFWdGZbEd16+APdy
0CZBMA4bIxF/kSmoyq10G3lLxgNgi7ZJQ2pN4CAQHR/kI14gxjaUt2lS5A2eNegG
lutxAoGALG1JxRXI1G2QVqNXjveLI4BA9KKZlXymNPRYxHZwr9wkgr1OZUR6hzGf
GFzfciXBeiM5DgwCGzOsRmhEVWQY0AWtwNpkvdTo2+FG+wiehzSkMviiwi4wXDZs
ZPIOBDSJCDbdO4GS9MJR1HtSQ09uMVK2/DMEOUhmfY2fkd9+rcQ=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_CRAWLER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUaD0m6kjEe/kX8KV86Tm3JMOXw5gwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyN1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC6kaAaFDrrIxHCuID22AfMrV7fVrB9F5h0uQP5KSawigxJ
BHqs9gIjPi7ur9nFGxGFjh+cyFF7kkWbLOJpABEu6J1DC6+MPe67rnQjq3IEds8d
c4ToidqfP1/Pgl4uOfV0MJpYF77Vpc/P2SHApjRIl7wCPxBS50BZkPaXbobb5e9r
3QSFpyLsvs0jeu1xp4w7DBdJsiHY/Qh3ekvUAH3A/tC/kQ97K9ZndgIQflW+OO89
FwWS9pKLXkYbKejhbaQ5D6wP2xcvY4C093B8kpaeMA9DCW8tUATGGTYaN6MUhNt9
d0LQZ0R58uolJW2o2Qv45TokYoHlsuGbDcc11ijDAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCaugeA7XZuF/JeC6T/cDGq
c5Y5pEBuhvNHj6aESm2FvuRIgXS6djo1YZF0McTiLVOtnUqDBSl1h/VH1e4n8zj3
MAVMPfXbAByexDGjbEIo0/aLmcUAAy3h/HQYmkX+Ge5Bm0MCszSbM/YqMPV30rSz
Gq/KfB8s8QQb7T2sS10VTlIBL54AjEgnyunR3vPjx0rqfnFRHdQoD7MdUwOEq3qE
6FFzpmp/fUaValfF9FS8w4vDq13LUY7OhphmW8mJHJ6e7GcUxFPLKs1oNpsMMPJz
wd4te+SB/dQ8CH1o3xvvFirUiPNz1wXRziJSO6AqjNXBMe86qnELwfXohI5oxUl9
-----END CERTIFICATE-----
"""

SSL_TEST_CRAWLER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAupGgGhQ66yMRwriA9tgHzK1e31awfReYdLkD+SkmsIoMSQR6
rPYCIz4u7q/ZxRsRhY4fnMhRe5JFmyziaQARLuidQwuvjD3uu650I6tyBHbPHXOE
6Inanz9fz4JeLjn1dDCaWBe+1aXPz9khwKY0SJe8Aj8QUudAWZD2l26G2+Xva90E
haci7L7NI3rtcaeMOwwXSbIh2P0Id3pL1AB9wP7Qv5EPeyvWZ3YCEH5VvjjvPRcF
kvaSi15GGyno4W2kOQ+sD9sXL2OAtPdwfJKWnjAPQwlvLVAExhk2GjejFITbfXdC
0GdEefLqJSVtqNkL+OU6JGKB5bLhmw3HNdYowwIDAQABAoIBAQCWTQ07FUMl/Rmo
0jTrJ7yY0q7UpCUIkcK7ffXKe7F0lbIx/M7LmmC8fbMXjUmWNilWe9nR17t1HrC+
w1kfF/O/45wV0Es7YwV546AiwFLZb9GJO3A+WhhrJIYOSUuQWBb65NDi2TZfLfaN
zrIXXo5OURcghCelcjFwNo3CD0PL0ECB2vfBJ27QYHlv3mBGCxKTLyCPb+Oyn1fT
bDGLiwHv5tPxx8zkcaNXDztjKDJYNMSS5hE3/69dyyIdkjA+PM8Qwghr5V14m2lJ
7RUIWntNzsbxRZ6t24rK1ytQVO2o9kOx+sEtNvu7hnvmkFSLhUhtXzEAabQXyXOn
ftCDVhqZAoGBANsha+ofkczMozKrALzEeugh5D57tDmGvcG2puIiiJiYCighovkr
cvQ0h5gr18lraEP3768rZlQ0814tA17yoXaHNeNY6IyE7EiLkTtKx4tRfi1FmgK1
YTc0LWQhELN6lg1YqbuRgAn9wPxJY1MEFutuGXJCzcsGhCNCvqmRhl01AoGBANn1
rabHjCBZRzWOeh8fNfAcbNdVLsrD/nmyCDxEN96q/ascb3fcyNx+USqKz1acoJNC
vGILzRa9gm/86KA5r7l41+bf0FYz0muTiqpzMNN9LCBG5ChosmsSB8v7i9Q4i7yu
pCcv5ATSSeAGUcvrenK5uWM7ht+fjfTdW1RsIsUXAoGAYSYVEMwEOLa0157GienV
z5pO9YCkayiYcgxHOlQzGOu2/QnElhE0Op4bS1SMq2ip5hBCu/dSu5xqFOOB7hNF
kCXrtypQlxPLKXJu5cmGY/ayKOIFoJPHUNEaGp0qKVf8tFgNj/G2wTc12uOyXDig
7Kl4MJb7Y7o01OkfXE//MM0CgYEAmJ87GNUUXzaE8ZCyHQba2ybcZDCG0n9Ju2eZ
8rGGOcqcVGxV9aXJlPRy24pVw31rx5JsnW9MDkdnhgmfz0p1rTdcX5OLrEEfcCrh
Z5e/segttPBPJaiifu0iPokHEfUCjH3x/mq/jUy/ZDqonlVm6dz5Xu449HAilDtI
j6Yk9sMCgYEAjE0g9OFzhHJtSwQtTy8S2GYJtFAvy8KneXsR/YAz/C0/CgvT+OsK
ACI948k1VXpUK/u2A+bmqxThN7OPDC9sLgThrdtAL+7UKH68fkqFYu0usiTif2z7
/1VI9PPkm9ZKtHx6O97fdBjv7DHhGdYITB+pVXxI6VKXmS4+YgfonJo=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_DAEMON_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUTYcm+E1jiGL7UEiopTFGmSwk3eQwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyN1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDD4xmVdRUqCRCDRebD9nds1h1mtyutoeHfruSn4PiEx30Q
YSzGRszSTvM+PwzL6jug6CVmlfWzLBC25unegeZhjlhoMkMkVavA1bZQ0sx2t2ll
wqFMhk0BvfQ0ftQ0BEgHpbll361gZGb7sLB0kuh1LhRE6uWpkg3WJT36DwzkCJ+R
YgAA63J11uLhMVk22bQ9UDIlmlL2Kd0M1sLrdPtF7h2wB77RirXpH9RxPilPWTwd
t63eHKetGMwmeCHP6VHWc3mtmnYCcEf851HXr/VYYdwn/Egbn5NWU9MkyG4U6Jw/
7iVRvf8XIv6IGcwY+qB922OjrCxsHYCWUbfwiaFXAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBFYpf2hnFIOfEEKFkNni9T
QK//s9W2Bf2hwn59TC6tvpN0pIenfqZ5A/Evc8PnjaO8UY+rWsxRL2YZoDEABnQb
3x0VfnZKQLKGju6JiVJWSn5F5Ilj2ntglHsAgQp4QBEMbIwfStW9AeaCwVoeD34B
/NFUoD33QM6E2yKuRetceeauBA+giBkSFaUA1jeSHfRGeWtuJmnNHvd9iA8cfrSg
gETkXKUyTYkS7Afi47oCMblmuy1pKOnQsirih8Vnic0Wn46bObLn8lt3k1d0+G0F
Nx37aAAP/ArHTyRh0ctfw99aTDgOm5v46NZNLPH9z7NPTtN0tz3r3C2nT4SUB+qq
-----END CERTIFICATE-----
"""

SSL_TEST_DAEMON_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEAw+MZlXUVKgkQg0Xmw/Z3bNYdZrcrraHh367kp+D4hMd9EGEs
xkbM0k7zPj8My+o7oOglZpX1sywQtubp3oHmYY5YaDJDJFWrwNW2UNLMdrdpZcKh
TIZNAb30NH7UNARIB6W5Zd+tYGRm+7CwdJLodS4UROrlqZIN1iU9+g8M5AifkWIA
AOtyddbi4TFZNtm0PVAyJZpS9indDNbC63T7Re4dsAe+0Yq16R/UcT4pT1k8Hbet
3hynrRjMJnghz+lR1nN5rZp2AnBH/OdR16/1WGHcJ/xIG5+TVlPTJMhuFOicP+4l
Ub3/FyL+iBnMGPqgfdtjo6wsbB2AllG38ImhVwIDAQABAoIBAQCv0n98LwM4H7q6
mVtwOSEoh2cMcwy5ZLwg0hJavQtT4trWgOJ3dcUSX9rk3CLYRP4Qh05Krf9DOyIl
iU4RcfcfSW0A2Vx6mIr5Itnp4cu0IxxvQisVTNaB4cX3+H7v0Yf1lUK7tfEgu/3T
m9xGRjZwN1PqKAzMD1RsCjF+6VNguOqHzsz+8aqppbAQPqGfVCwqjdfG0nn6h89M
KxpRBQXhsqLvrxVy452Danoz64vPEwRePXhF7ZOMStno9Gzc6ArjEhIFzkNvPp+M
OpwjOTeSzzFmkGP9bHPL9hbDWpFy/wVJYuJoHGdmtFZPdGyfTzOvWqxuBCnTkRAl
Na8oFz1BAoGBAOd9Pl09+zXzi0ILdnseLvGZ3aVeOr2fxf4v7/zHDCgpro/+9OPu
oYacMnnp+nbURrjCQBeE5lu5AKtq056JxLngXIAFrnVaEu/4BjuBTa/nauXJM+r6
q5CLtNQSWsq46wpcto/btPvv5kl5AaGx/AtkmGqD6O7e0W6Xm2+r5AiLAoGBANig
0uCRtv4I/vTjl6A82aRRy7zWyXRYXei7ti2G5/EOs+MwYs3tJF6ncrVMyKjcNpof
DcnuO5UO8bL6Lcz5G/XPmMfnoicsuZxZk5X7NofRPEwG1JKvUA7wvHBJU630M+p9
5xLI3fKIW1LB9zZT7wG64iJXx1CHFl5IoqCSDJflAoGBANH4m3nN/6/nMbh9V0HD
lgcVbqNR/mwDoX63krIxBgjkDe+U7iJVUHQd9/b3UXU5hNCPeb0bkis+eqoBouPZ
yPRk2uJQxPay9hxuV5Df70yP1zmIsCwCpV3eKu51m57n7mIeyIViXx5qcvLP7Lfz
DlBzNYDgF4eb2lG6+IVpX9STAoGBAMgpGZBss2PY1hNatABYGVWOSq1q3OvGtsbT
owpAC9IdnrN+Qt05kBBxsji5APOdvkn8BZaerKkXDNct+OHbDy26qtWTPq3p0nsX
/ZlobENkXs10xjffCx8y6zrpVgt2h/3UZY1i0klGGvPFy3GEbmPv1QCckMrkdxOZ
E8NAD6jNAoGBAJ9h+zA+zuJZZPddUltNeg1ZxvLbjg9rd/7YSGMVNmCWBpwv33HR
i881B4UXr3m/cEbA1PxBwHkSXGkfFvsmdqFN5UITd1oF3EAHVK0oUmewgl9clj8B
exwCTm7kDpCVHXsNu/ncODBQM8+r4Z3vjXAyw0DT94iaASYypEDpXVgw
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_INTRODUCER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUbtU04ozLF4XldtM40YPkF1DIMKEwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyN1oYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDnZYSeBOBGn94eiPAorxg9GdUoIGr4UUNxrtXTBmX8zZZp
LIu3m+2T+BO0ig6a4SZ7IxD4Ocbj2YP6sYl44F3fNXjvekvNzTE6LaeCvOh5myUj
3h/cCZTMCV9Ja4CMg+xOCBLu+CjyWSkp5Z8kdYz86o7gKNh1eJT50a8pARqyNdWw
Q/YoYTTpfG80GQp31Zb3hzX9fl6dT6+gYuV1xkiPrSuxX4oZZ7ZH+ktIwiFoXGOh
sQu1cLaLHP0iImF1QCHh56RwV7j/RcgqMx/hdzz80rShbUost85ngl+0ss3jYm1+
Z5Ps8u8FRSdgN4H+HQL16q8OGrMZXdnRKUYEiCY3AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQDG/ltB2n5vOIPi90d+GikR
nGu1SR7ALScsbF4w4uIH8UvtMTu4nctlLJWPNuor3s7ylnwv0eMwumtuHYuIBSm3
9umrUIGlwMedCdMNKpvQF/WkXevEQj1azfGmltta+ZrQBxwhHg069y8Ykb84SM8D
5vEy0rJ+zmrvFYeKaxzAjA1sG4bjCiMMiwJ2rHXFjIFdQHMwwYcFQ1FeAPxEe/8T
PGYY561vOKVP6P86swKPOsQn+3MYR0Ehi8vdw5E4f3TcOkyxx5sPmiC/3pq0h4U4
kmLI+Ng3D1A3NzSel2J0mp7RiPmUhu//WZOE3G38+27jGp9GPEM/zlc1gL2EHN9w
-----END CERTIFICATE-----
"""

SSL_TEST_INTRODUCER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEA52WEngTgRp/eHojwKK8YPRnVKCBq+FFDca7V0wZl/M2WaSyL
t5vtk/gTtIoOmuEmeyMQ+DnG49mD+rGJeOBd3zV473pLzc0xOi2ngrzoeZslI94f
3AmUzAlfSWuAjIPsTggS7vgo8lkpKeWfJHWM/OqO4CjYdXiU+dGvKQEasjXVsEP2
KGE06XxvNBkKd9WW94c1/X5enU+voGLldcZIj60rsV+KGWe2R/pLSMIhaFxjobEL
tXC2ixz9IiJhdUAh4eekcFe4/0XIKjMf4Xc8/NK0oW1KLLfOZ4JftLLN42JtfmeT
7PLvBUUnYDeB/h0C9eqvDhqzGV3Z0SlGBIgmNwIDAQABAoIBAQCPSwZ89HgORCHA
tvxBtWxFKiId3zVe4LPrSmGPdH7jtkxWhQdghGbzIsTRIE07DAJQbr6reNv5bVGV
hSukdwyqlOp3IjyfDVpWtL7u7xzncXPmaj9Ae45xa7xeMvxAB9Hl4IoZAgQZT612
DIQoh8LvPDGODr08wZc/vOHDerOVdyNdVIu27pJziTHyhHBZMpJar31yBsG2J4j1
FhKZrmZr+01fV/hGCQ1NkKy26gOA7OnOCqlco12iHX5PmWwAU1S6UJf6oSPxXAUS
4Za5T9pxvpFgYKlmp5665lhdRYNA+Kf3Z+dF6n956AOFZzBE1KuxTCl4ea1LPJqY
cmHGbeABAoGBAPy7PmMp/C+WbdK3JXactlV/XvMB5ldqbfh7q5CqwTG74q9Y70hJ
VFhfB/a/ZcMEb6vELgpnSzOMZFg6AA89PWBEip/2U1Yf6ugqjsU9xlKkXVnzoS/p
99QDtZ2vEw6Cm1dA0zIt615wz2A9/wDsBktya0/ijiBuxmc9CZcyUYoBAoGBAOpj
o0PlWbVTsKoj5N/rQH0VcIYwtIQqS4rbpsgAjhihA5oAS8ZKl484pAwf2adXdSdR
5vn+FP7y17oRt6ttQPITApKpZSIcxNuQlLNI95c49oU53tAvXZdddb0arjoqJtw1
GkTlHj08whgxpTd4S80GGOn3GROekcJHVnjSA4A3AoGBAOSCiI4w0AxW/0WewwjT
+Sik2bzu4s33NSeO6jkLq1LEhtn0l6XMZ67ffdvkgqYpxK6R2u8dJimdrrz29EbT
IEOCtbScjA07HrJ8iEpe6IqggqdqWTtxWNsh33yLZ7ee78Wcn1innEDvzxE9/Otg
fPCKq+y287rvbgS6c4l5vbABAoGBAJ0EOHggaZM2SFACEa4Li7z/oszSTeuH5elU
sgqjjI1lN+NvtVNV3uf7+rGAmK8owHuhu0jXdDtCdU/Z1J/LZcmFAKE9R1mtyhaI
aYUdKXetmj+vf9sZD+p5mokfGX4vhK7aCAoFLte5HxFUGKjrNmRXZFM/zBW/kUeD
wKLZlazLAoGBAJXC3C/NiCxyxPuSAQ3/0CA3cN6rqul7Z+buPi5VRyXJTljB+4pp
4FUSFNtXSssU61cBvxXu2J7VBp3PkFOHrAzRZWIdq2loLE2t6Ma20Mj2quT/0M26
fEK1BVt3jMFt2veQo0EZ7HMTvtSDeoKgkBnvcFvmXhjKOaqZYbSVEY7r
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_PRIVATE_CA_CERT_AND_KEY_5: Tuple[bytes, bytes] = (SSL_TEST_PRIVATE_CA_CRT, SSL_TEST_PRIVATE_CA_KEY)

SSL_TEST_NODE_CERTS_AND_KEYS_5: Dict[str, Dict[str, Dict[str, bytes]]] = {
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
