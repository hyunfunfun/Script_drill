import urllib
import http.client
conn = http.client.HTTPConnection('apis.data.go.kr')
conn.request("GET","/B551182/hospInfoServicev2/getHospBasisList?serviceKey=WfaTpP4BPEFyU0r49aJ0yEs2niEBt99e19fn4zTYsC%2BAr%2F%2BdU9Pr9ug9i6Uv0Ibaj3ynhqZpZUBUuKYso%2F7q5w%3D%3D&pageNo=1&numOfRows=10&sidoCd=110000&sgguCd=110019&emdongNm=%EC%8B%A0%EB%82%B4%EB%8F%99")
req = conn.getresponse()
print(req.status,req.reason)
print(req.read().decode('utf-8'))