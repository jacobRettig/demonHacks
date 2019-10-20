import bs4 as bs
from bs4 import BeautifulSoup
import urllib.request

'Gets the number of vehicles per route'
def routeNum(url):
    req= urllib.request.urlopen(url)
    xml = BeautifulSoup(req, 'lxml')
    res = 0
    for item in xml.findAll('rt'):
        res += 1
    return res
'Gets the number of Trains currently running'
def trainNumbers(url):
    req= urllib.request.urlopen(url)
    xml = BeautifulSoup(req, 'lxml')
    res = 0
    for item in xml.findAll('rn'):
        res += 1
    return res
'Get the number of Buses currently running'
def totalCTABus():
    lst=['http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=192,%20201,%20206','http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=148,%20151,%20152,%20155,%20156,%20157,%20165,%20169,%20171,%20172','http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=125,%20126,%20128,%20130,%20134,%20135,%20136,%20143,%20146,%20147','http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=106,%20108,%20111,%20111A,%20112,%20115,%20119,%20120,%20121,%20124','http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=91,%2092,%2093,%2094,%2095,%2096,%2097,%20X98,%20100,%20103','http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=81W,%2082,%2084,%2085,%2085A,%2086,%2087,%20N87,%2088,%2090','http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=75,%2076,%2077,%20N77,%2078,%2079,%20N79,%2080,%2081,%20N81', 'http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=65,%2066,%20N66,%2067,%2068,%2070,%2071,%2072,%2073,%2074', 'http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=57,%2059,%2060,%20N60,%2062,%20N62,%2062H,%2063,%20N63,%2063W', 'http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=N53,%2053A,%2054,%2054A,%2054B,%2055,%20N55,%2055A,%2055N,%2056', 'http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=8,%2049,%20N49,%20X49,%2049B,%2050,%2051,%2052,%2052A,%2053', 'http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=31,%2034,%20N34,%2035,%2036,%2037,%2039,%2043,%2044,%2047', 'http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=20,%20N20,%2021,%2022,%20N22,%2024,%2026,%2028,%2029,%2030', 'http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=9,%20N9,%20X9,%2010,%2011,%2012,%20J14,%2015,%2018,%2019', 'http://www.ctabustracker.com/bustime/api/v2/getvehicles?key=psRsTMdes3dddXDzSk5GcKNTy&rt=1,%202,%203,%204,%20N4,%20N5,%206,%207,%208,%208A']
    res = 0
    for item in range(len(lst)):
        res += routeNum(lst[item])
    return res
