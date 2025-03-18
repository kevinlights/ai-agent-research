from autogen_core.models import ModelFamily
from autogen_ext.models.openai import OpenAIChatCompletionClient


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
