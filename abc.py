import requests
import json
import re
import time
import random
import html

# 设置接口 URL
<<<<<<< HEAD:abc.py
base_url = "http://erwrwrw.com/index.php?m=&c=Index&a=fetch_chapter&novel_id=406023475&spread_id="
=======
base_url = "http://ssssss.com/index.php?m=&c=Index&a=fetch_chapter&novel_id=406023475&spread_id="
>>>>>>> 17bc46e0b2b6b66635fc9d3e7c214a97308698d0:skill.py
output_file = "C:\\book\\406023475.txt"

# 设置模拟的手机用户代理
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"

# 构建请求头部
headers = {
    "User-Agent": user_agent,
}

# 循环调用接口 10 次
for index in range(0, 20):
    url = f"{base_url}{index}"

    # 构建 POST 请求参数
    post_data = {
        "index": index,
    }

    # 发送 POST 请求，带有模拟的用户代理头部
    response = requests.post(url, headers=headers, data=post_data)

    if response.status_code == 200:
        # 解析 JSON 响应
        data = json.loads(response.text)

        # 提取 body 字段并处理
        body = data.get("info", {}).get("body", "")
        if body:
            # 使用html.unescape解码HTML实体
            body = html.unescape(body)
            # 将<br>替换为换行符
            body = body.replace("<br>", "\n")
            # 使用正则表达式将<p>和</p>标签替换为空字符串

            #<p style='font-size:px'>
            #body = re.sub(r'<p\s*style\s*=\s*\'font-size:[^>]+>\s*</p>', '', body)
            #body = re.sub(r'<p\s* style\s*=\s*\'font-size:[^>]+>\s*</p>', '', body)
            #body = re.sub(r'<p[^>]*>[^<]*</p>', '', body)
            body = body.replace("</p>", "")

            # 使用正则表达式将<p>标签的style属性替换为空字符串
            body = re.sub(r'<p\s*style\s*=\s*\'[^>]+\'>', '', body)
            time.sleep(random.uniform(1,2))
            with open(output_file, "a", encoding="utf-8") as file:
                file.write(body + "\n")
        
        print(f"成功获取第 {index} 条数据")
    else:
        print(f"获取第 {index} 条数据失败")

print("数据抓取完成，已保存到 output.txt 文件中")
