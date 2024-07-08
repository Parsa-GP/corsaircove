from requests import get
from json import loads, dumps
from urllib import parse

srv="http://localhost:8009"

def get_from_api(req):
	return loads(get(srv+req, timeout=3).text)

def get_sites():
	response=get_from_api("/api/v1/sites")
	return response["supported_sites"]

def search(site, query, limit=0, page=1):
	query=parse.urlencode({"site":site, "query":query, "limit":limit, "page":page})
	response=get_from_api("/api/v1/search?"+query)
	return response

def trending(site, category="", limit=0, page=1):
	query=parse.urlencode({"site":site, "category":category, "limit":limit, "page":page})
	response=get_from_api("/api/v1/trending?"+query)
	print("Well, that took", response["time"], "secounds.")
	print("Total torrents found:", response["total"])
	torrents = response["data"]
	for t in torrents:
		print(t["name"])										# Mirzapur (2024) Hindi S03 Complete 720p AMZN WEBRip - 2 GB - AAC 5.1 HEVC x265 E...
		print(t["url"])											# https://1337x.to/torrent/6154813/Mirzapur-2024-Hindi-S03-Complete-720p-AMZN-WEBRip-2-GB-AAC-5-1-HEVC-x265-Esub-HDHub-ProtonMovies/
		print("*"+t["size"]+"* \t@ \""+t["date"]+"\" \tby: ["+t["uploader"]+"]")	# *2.2 GB* 	@ "8pm Jul. 4th" 	by: [AlejandroAXL]
		print("SE:"+t["seeders"]+" LE:"+t["leechers"])			# SE:3833 LE:1129
		print("Screenshots: \n"+"\n\t".join(t["screenshot"]))	# 	https://www.picsxtra.com/images/2024/07/05/03af37176f7992280aac6ceb0862b75b9661faceb1e6af2c0cd7cbd0513415bd.jpg
		print(t["category"])									# TV:
		print("Files:"+"\n\t".join(t["files"]))					# 	Mirzapur.S03E02.720p.AMZN.WEB-Rip.DDP5.1.H.265- ProtonMovies.mkv (343.0 MB)
		print(t["magnet"]) 										# magnet:?xt=urn:btih:B6A9E3E0355C516401F5D90E66AD0FD839E8F4E3&dn=Mirzapur+%282024%29+Hindi+S03+Complete+720p+AMZN+...
		print(t["hash"])										# B6A9E3E0355C516401F5D90E66AD0FD839E8F4E3

if __name__ == "__main__":
	#print(get_sites())
	print(search("yts", "inside out"))
	