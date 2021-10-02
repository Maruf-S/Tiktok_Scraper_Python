from TikTokApi import TikTokApi
import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
import json
count  = 4

def scrapeTiktok(username):
    api = TikTokApi.get_instance()
    return api.by_username(username, count=count,custom_verifyFp="verify_ku9r83k0_JWMZD8du_HQyE_43tt_BdNp_JgzmcsRNmgoi",use_test_endpoints=True)
@app.route('/api/profile/tiktok/<username>', methods=['GET'])
def get_profile(username):
    user = stats =  {}
    averagePlayCount = {}
    # userMeta.stats.averagePlayCount = average_play_count;
    # userMeta.stats.maxPlayCount = Math.max( ...viewsCountArray );
    # userMeta.stats.minPlayCount = Math.min( ...viewsCountArray )
    # userMeta.content = content;
    averagePlayCount = 0
    maxPlayCount = 0
    playCountList = []
    minPlayCount = 0
    content = []
    # try:
    tiktoks = scrapeTiktok(username)
    c = 0
    for tiktok in tiktoks:
        if(c==0):
            user=tiktok["author"]
            stats = tiktok["authorStats"]
            c+=1
            continue
        else:
            playCountList.append(tiktok["stats"]["playCount"])
            content.append(tiktok["video"]["playAddr"])
    maxPlayCount = max(playCountList)
    minPlayCount = min(playCountList)
    averagePlayCount = sum(playCountList)//3
    output = {"user":user,"content":content,"stats":{stats|{"averagePlayCount":averagePlayCount,"maxPlayCount":maxPlayCount,"minPlayCount":minPlayCount}}}
    print(output)
    return json.dumps(output)
    # except Exception as e :
    #     print(e)
    #     return jsonify({}), 404
app.run()