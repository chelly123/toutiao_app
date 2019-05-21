import json
try:
    from tooutiao.handle_redis import save_task
except:
    from handle_redis import save_task

def response(flow):
    print("--" * 30)
    print("nihao")
    if 'article/content/22/1/' in flow.request.url:
        json_data = json.loads(flow.response.text)["data"]
        if json_data["group_source"] == 3:
            toutiao_info = {}
            #四个字段,发布时间 标题 链接 来源
            toutiao_info['publish_time'] = json_data['h5_extra']['publish_time']
            toutiao_info['title'] = json_data['h5_extra']['title']
            toutiao_info['src_link'] = json_data['h5_extra']['src_link']
            toutiao_info['source'] = json_data['h5_extra']['source']
            save_task(toutiao_info)

# def request(flow):
