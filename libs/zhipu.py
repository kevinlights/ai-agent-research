from zhipuai import ZhipuAI
import requests
import base64
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelFamily


def draw_image(prompt: str):
    api_key = open("api-key").read()
    if not api_key:
        raise Exception("please put zhipuai api key to file api-key")
    client = ZhipuAI(api_key=api_key)  # 请填写您自己的APIKey
    response = client.images.generations(
        model="CogView-3-Flash",  # 填写需要调用的模型编码
        prompt=prompt,
    )

    return response.data[0].url


def draw_image_with_b64(prompt: str):
    url = draw_image(prompt)
    resp = requests.get(url)

    if resp.status_code == 200:
        return base64.b64encode(resp.content).decode("utf-8")
    else:
        return ""


def chat_model():
    api_key = open("api-key").read()
    if not api_key:
        raise Exception("please put zhipuai api key to file api-key")
    client = ZhipuAI(api_key=api_key)  # 请填写您自己的APIKey
    return OpenAIChatCompletionClient(
        model="GLM-4-Flash",
        base_url=client._base_url,
        api_key=api_key,
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": False,
            "family": ModelFamily.ANY,
        },
    )
