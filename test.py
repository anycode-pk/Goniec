import os

def send_req(type, endpoint):
    os.system("curl -i -g -X " + type + " \"" + endpoint + "\"")

userid = "122108985122029346"
pageid = "114174155116181"

recipient = "?recipient={'id':'" + userid + "'}"
messaging_type = "&messaging_type=RESPONSE"
message = "&message={text:hello,world}"
pagetoken = "EAAJIZAiUxvB8BO9CE7scILbtZCXykPZC9Tn00QVFzWOtkxfwblEmlSUWgZAeI54bmGst0uIHsdssz6HA2jXRUfE6QFqg4gPtb29FyroDaiWZBLizcA3NcAAWe6iOSEjeHSv3iuFec9qfZCsWD5OZCuOgxEQkhQahtZAZBTrpqli6Qm3YmZBi5OWZB15MVZC3hlSTjmdCsc69EGctiDF62X9hqKmaEd4ZD"
access_token = "&access_token=" + pagetoken

graph_endp = "https://graph.facebook.com/v18.0/"

#send_req("GET", graph_endp + pageid +  "?access_token=" + pagetoken)
send_req("GET", graph_endp + pageid + "/conversations?fields=participants,messages{id, message}&access_token=" + pagetoken)

send_req("POST", graph_endp + pageid + "/messages?recipient={id:6442179169244412}&message={text:'ZADZIALAJ2'}&messaging_type=RESPONSE&access_token=" + pagetoken)

#os.system("curl -i -X POST \"https://graph.facebook.com/v18.0/" + pageid + "/messages" + recipient + messaging_type + message + access_token + "\"")

#mylikes = "\"https://graph.facebook.com/" + pageid + "?fields=id,name,picture&access_token="+pagetoken + "\""

#os.system("curl -i -X GET " + mylikes)
#print(recipient)
