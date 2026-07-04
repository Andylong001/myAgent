import os
from dotenv import load_dotenv
from zhipuai import ZhipuAI 

# 自动加载当前目录 .env
load_dotenv()

# 初始化 ZhipuAI 客户端
client = ZhipuAI(
    api_key=os.environ.get("ZHIPUAI_API_KEY"),
    base_url=os.environ.get("ZHIPUAI_BASE_URL"),
)

def main():
    # 发送聊天请求，要求生成一个营销口号
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[
            {"role": "system", "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"},
            {"role": "assistant", "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"},
            {"role": "user", "content": "智谱开放平台"}
        ],
        thinking={
            "type": "enabled",    # 启用深度思考模式
        },
        max_tokens=65536,          # 最大输出 tokens
        temperature=1.0          # 控制输出的随机性
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()

    input("按回车推出...")
