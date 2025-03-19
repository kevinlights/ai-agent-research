from autogen_core.models import ModelFamily
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage, ChatCompletionClient


async def chat(msg: str, model_client: ChatCompletionClient):
    return await model_client.create(messages=[UserMessage(content=msg, source="user")])


def llama3_sd_prompt():
    return OpenAIChatCompletionClient(
        model="impactframes/llama3_ifai_sd_prompt_mkr_q4km:latest",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": False,
            "json_output": False,
            "family": ModelFamily.ANY,
        },
    )


def llava_7b():
    return OpenAIChatCompletionClient(
        model="llava:7b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": True,
            "function_calling": False,
            "json_output": False,
            "family": ModelFamily.ANY,
        },
    )


def llama3_2_3b():
    return OpenAIChatCompletionClient(
        model="llama3.2:3b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": False,
            "family": ModelFamily.ANY,
        },
    )


def phi4_mini_3_8b():
    return OpenAIChatCompletionClient(
        model="phi4-mini:3.8b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": False,
            "family": ModelFamily.ANY,
        },
    )


def qwq_32b():
    return OpenAIChatCompletionClient(
        model="qwq:32b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": ModelFamily.ANY,
        },
    )


def qwen_25_1_5b():
    return OpenAIChatCompletionClient(
        model="qwen2.5:1.5b",
        # model="llama3.2:3b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": ModelFamily.ANY,
        },
    )


def qwen_25_7b():
    return OpenAIChatCompletionClient(
        model="qwen2.5:7b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": False,
            "family": ModelFamily.ANY,
        },
    )


def qwen_25_14b():
    return OpenAIChatCompletionClient(
        model="qwen2.5:14b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": ModelFamily.ANY,
        },
    )


def qwen2_5_coder_3b():
    return OpenAIChatCompletionClient(
        model="qwen2.5-coder:3b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": ModelFamily.ANY,
        },
    )


def qwen2_5_coder_14b():
    return OpenAIChatCompletionClient(
        model="qwen2.5-coder:14b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": ModelFamily.ANY,
        },
    )


def qwen2_5_coder_7b():
    return OpenAIChatCompletionClient(
        model="qwen2.5-coder:7b",
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": ModelFamily.ANY,
        },
    )
