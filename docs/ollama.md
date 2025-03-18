# Ollama

> https://ollama.com/search
> https://ollama.cadn.net.cn/faq.html#google_vignette

```shell
export OLLAMA_CONTEXT_LENGTH=128000
export OLLAMA_DEBUG=true
export OLLAMA_FLASH_ATTENTION=true

ollama serve
```


## Tips

> OLLAMA_MAX_LOADED_MODELS- 如果模型适合可用内存，则可以同时加载的最大模型数。默认值为 3 * GPU 数量或 3 用于 CPU 推理。
> OLLAMA_NUM_PARALLEL- 每个模型将同时处理的最大并行请求数。默认值将根据可用内存自动选择 4 或 1。
> OLLAMA_MAX_QUEUE- Ollama 在忙碌时在拒绝其他请求之前将排队的最大请求数。默认值为 512
> Flash Attention 是大多数现代模型的一项功能，随着上下文大小的增长，它可以显著减少内存使用量。要启用 Flash Attention，请将OLLAMA_FLASH_ATTENTION环境变量设置为1启动 Ollama 服务器时。
> K/V 上下文缓存可以量化，以便在启用 Flash Attention 时显著减少内存使用。要将量化 K/V 缓存与 Ollama 一起使用，您可以设置以下环境变量：OLLAMA_KV_CACHE_TYPE- K/V 缓存的量化类型。默认值为f16
> 当前可用的 K/V 缓存量化类型包括：
> f16- 高精度和内存使用率（默认）。
> q8_0- 8 位量化，使用大约 1/2 的内存f16由于精度损失非常小，这通常不会对模型的质量产生明显影响（如果不使用 F16，建议使用）。
> q4_0- 4 位量化，使用大约 1/4 的内存f16精度损失为中小，在较高的上下文大小下可能更明显。

