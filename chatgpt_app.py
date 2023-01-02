
from googleapiclient.discovery import build
from flask import Flask,redirect,url_for,render_template,request
from revChatGPT.ChatGPT import Chatbot


def chatgpt(question,comments):
    out=""
    for comm in comments:
        try:
            chatbot = Chatbot({
          "session_token": session_token
        }, conversation_id=None, parent_id=None) # You can start a custom conversation

            response = chatbot.ask(f"{question} in the following comments {comm}", conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)
            out=out+response['message']
        except Exception as e:
            if e=="Wrong response code! Refreshing session...":
                return out
            else:
                continue       
        
    chatbot = Chatbot({
      "session_token": session_token
    }, conversation_id=None, parent_id=None) # You can start a custom conversation

    response = chatbot.ask(f"summarize the following {out}", conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)
    
    return response['message']

api_key="AIzaSyCVKtAYFU9pcg_LayIQ0qsM3O9M_BfWWyc"
session_token="eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..MnHXAiAk69rCtmxH.VK_MPebAplYlEs4KKpSR5z2FkBNg3t7Oyxyfrl_jvGy9fHlxihPw_F35ViorLKoDMLKWu_hwPHnKHWD5XsrAGL2OQP783hgLICcDj7ZDNcIoQA-b1Ki2q-hUsTDYuhcvMa-xMTZftg_VfmJPAXDhMSQ4inPzIUcKwUvNou2AhuRc2pp9nlXiOArUra2tiIGemwukvv6AU0_FI84Zkf3qCm2M3GwlKnD6b63CgmgSeoViTVQmOTibl6-76HCDZ_WQO4KpGlKL21Rj2VkpRQbcO2305Bv0TS3BPzl0MjchsnJQQ8BPkKqNyL5cerLpq8dubkgKzYEbPg9fiXzFA8BlI8mYPyYF8POUmmtQu6MG0uE8mm7d7GRjxZS6QJkekYIjUt4d8JgiPo3HnxQIJ5kjWRh33-HEWGcbBzJlvjgpRrszvGpN0N0t7NDWepW-dFGlMPr7-COJUTjfh7ToubmW8oYOp0Ym6i_DPp1FHseWDa_sOG537Y5OBLW4mORLNZf_hRuKg3G7vD_zVpfqr5kujnR0wBVucSLq1oHM1VakMW4Bkb_dY49blCF74w627aByKWRZR_cEr6YdVaWLUVBnhWu_lySfr_lhki67Q7jj2TVe2lCnO_mT1SZmx25-JcvSpGjJiksunefSaa3y1az2pJjDWl0umFbEqxGb3vI6lwj0YH7Mu6BWDEiUMgqjNWmMeKk86lK-F2n8mbWK_CJiMEJ2tc2IeGHCVu7AwEgEdkVWeCsdU2rcYMEAJTmjXMFArpvBcef-qwAmGQ9jCEHkwWAux0gqw9_BRPUZmIwUTZDj0aW-uqR5hqGwdxPq5jlI_yCagQtLUQMTA8EfBehUpDRLyvC7tvE_61oyoCCPcbEngZydp4wIKe-M2LowRlr0fxdYrfscdh2jJ8VuhJFNnjSnJmSh82faCBIX7Ddzf3Fe8rs46ep3TdC4208ADzTRGwQpEHWCYM_1KzXI_f-XNjl5kAThZmNr-lEERqqgAWQhDVYyIYIwICIc2wjWeHr-538DxC1UgwLUVTQ3wVu9IfpZSDvkXKX8SltVECa-TJ14DPZMym5KUSDf5YF-ie1D7fZ2MQAvDb6uwWiOhFAVigJitCUv_VxFTwmRSKF16iJ0ryZo_3O8OqHrIN-YmISksKtByDw6rQ3RWrUkIPmi88TDg89yYlJ4f3fdE5IgBc4Qj4D23wsFBxRTo4M0PE1kmkI0gwzHLAKNMe9TlXxUjiQsXY-9ZlMwrF1p4daqQaeak4BEaVvINA5FhJat2rLt3I25PJOSM9Q-frhc8VP9xnGmMr__zJcMRyE1mHQVPjhwlW1XLPoenmTVGNrfi1Lh4jJo67ocTs_S7Y8UCowdPAc6FLxzjoK3PL_rKljcLdY5DKyWjlrEkPvsaFp87f1gFY33-y9vlcv7MjXGkMufnZE5oHeJEcdP-zne7rTkp_PNhCwVdQdQ92qsLhIzKYQ-m3pmjnFrxZcSXYChKKRUDwXUDK-hn2wKeiZP2d-iRDwzLG2A1ZtfZd54TMKU5OqLzIk9DnO9c3eZjlBYIeZ-oZX7mmix_7ppC4u82lqljTEzLyb_N6ToPn33RWEth-P_Ps_IQUyh06Tt-mudD71esHoYBlK8MCBg0gpsXGuPS4k32B-XNwQpXsFPKnDrMaswQm-KkDdKPyiKisW5zQGeiE9aG4kaZ4yuHH1C-9u6Q-MSHy0Ob6Qx7PI1q-kcRi4bqr3kUEsPfObrmnrs2KJNuaZpzdwGVUfrKsewapBy8spopOC154X8BEKHGrNLsARIERiFQbQ1MeYOLZDVZS7SbFPOPG9OcinJVgWsvDgSxnJdkjTXTP1TlwxXojDiNHEP5uvTna33_GGPPne04A1JerjE2-F_vgvOvz6OHPkzCGuQw1-RTqTEQ0H7eCQONInv3koDmaW2ycIf5LuV8ypR_WWKpsOXX8vgmzgR4nhAGfdtzeark0igR7P4gLS4uTUFlj05-gmnUJ7cDfT4vz5epQryAwKPT66_KynjXPGZJath305EkCwsVKZvMOQGdka1SnQWnZNkOqMx8wWh1bHLI40GJ1m8oSZBkst5AxOOpwmxVxkjtPPAKueI_UuKzMLYiEDUvTbYBjCcqMwS_skoVv-gffhCvdApCEIyiWL3aOUu_dy9eoWd1xo0qmE7ztX-vbYeLpl2owywV5mwnjtEJILEzGS-JTGsld88AdCF-Y4KMNrRmY6ViptAqUcyw2qo_Jdo3WGCvGaQ_LE2zR0tV-PyMXFU3Gh3RzQMjWKniBv3zoQpDN8ptbPaEeMJEo66Jw_jc3gINNv8UvQzx1wEvo8obJhJLwpXtkfN7ycVArlogJJMI11YOIbPr0pxl-OwtbhJ7JYoBPf_sg.xB6soQcV7l4Ul8eqQ8cwZQ"
youtube=build('youtube','v3',developerKey=api_key)


def get_comments(url,k):
    url=url
    videoId=url.split("v=")[1]
    request2= youtube.commentThreads().list(
                part="snippet",
                videoId=videoId,
                maxResults=100).execute()
    nextpageToken=request2.get("nextPageToken",None)
    stop_at=0
    nextpage=[]
    comments=[]
    commentId=[]
    while stop_at<=30:

        len_items=len(request2['items'])
        for i in range(1,len_items):
            comment_id=request2['items'][i]['id']
            comment=request2['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal']
            comments.append(comment)
            commentId.append(comment_id)
        nextpageToken=request2.get("nextPageToken",None)
        if not nextpageToken:
            break
        request2 = youtube.commentThreads().list(
                part="snippet",
                videoId=videoId,
                maxResults=100,
                pageToken=f'{nextpageToken}').execute()
        stop_at+=1
    comments=[f"{i+1}.{comm}" for i,comm in enumerate(comments)]
    comment=[]
    if len(comments)>k:
        j=0
        for i in range(1,len(comments)+1):
            if i%k==0:
                comment.append(comments[j:i])
                j=i

        comment.append(comments[j:])
        comment=["".join(sent) for sent in comment]
        return comment
    
    return comments


app=Flask(__name__)

@app.route("/",methods=['POST',"GET"])
def home():
    if request.method=="POST":
        link=request.form['link_field']
        question=request.form['que_field']
        comments=get_comments(link,100)
        out=chatgpt(question,comments)
        return render_template("index.html",content=out)
    else:
        return render_template("index.html",content="")


if __name__=="__main__":
    app.run()


