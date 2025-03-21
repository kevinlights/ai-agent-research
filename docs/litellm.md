# LiteLLM

```
curl -fsSL https://ollama.com/install.sh | sh

ollama pull llama3.2:1b

pip install 'litellm[proxy]'
litellm --model ollama/llama3.2:1b


litellm --model ollama/llama3.2:1b --host localhost --port 4000 --debug --max_tokens 128000 --temperature 0.7 --telemetry False 

litellm --model ollama/llama3.2:1b --host localhost --debug --max_tokens 128000 --temperature 0.7 --telemetry False 


```

