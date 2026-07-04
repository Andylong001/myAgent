# 从零开始测试对接智普大模型

> - [从零开始测试对接智普大模型步骤系列]
> - 第一步获取API KEY
> - 第二步设置环境变量
> - 第三步运行调试

这里通过从零开始测试对接ZHIPU大模型实践中，将对应的步骤总结如下。我使用的是GLM-4.7-Flash免费版，进行简单的调试测试和学习所用。

## 第一步获取API KEY
在智普官网进行注册，并完成实名认证，在个控制台->API KEY中新建API KEY。

```
[智普官网](https://open.bigmodel.cn/console/overview)
```

**注意：必须实名认证，API KEY才可以正常使用。

## 第二步设置环境变量
所以使用的环境为windows, 安装了Git Bash(MINGW64)、 VS Code和IDLE Shell， 分别可以在这三个环境下运行。

1. Git Bash
```
vim ~/.bashrc

export ZHIPUAI_API_KEY="your-api-key"
export ZHIPUAI_BASE_URL="https://open.bigmodel.cn/api/paas/v4/"

```
2. VS Code

在launch.json上进行设置，及仅能够在F5运行时被执行文件所读取, 在terminal运行时则还是不可被获取。
```
...
    "env": {
        "OPENAI_API_KEY": "your-api-key"
        "OPENAI_BASE_URL": "https://open.bigmodel.cn/api/paas/v4/"
    }
```

在项目根目录下新建.env文件，将APKI-KEY存储到.env文件中，通过python中dotenv的load_dotenv()实现环境变量的加载。
```
ZHIPUAI_API_KEY=your-api-key
ZHIPUAI_BASE_URL=https://open.bigmodel.cn/api/paas/v4/
```

## 第三步运行调试
大模型的API-KEY获取，环境变量设置好后，对模型调用的简易测试代码如下。

```
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

```