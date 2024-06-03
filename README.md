currently hosted locally at: https://bit.ly/llama-djang-nn

## Installation Steps

Clone the repository and install the dependencies:

```bash
git clone https://github.com/NamrataNair/django-llama/

make install
```
## Get a language model - mistral7b

To make this work you need a Llama.cpp gguf quantitized language model. We
will use Mistral 7B Instruct from [this repository](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF):

```bash
cd some/dir/where/to/put/your/models
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

## Settings

Change the `LLM_MODELS_DIR` setting in `main/settings.py` to your model directory path.

Change the `LLM_DEFAULT_MODEL` setting in `main/settings.py` if you
want to use another model. Use an absolute path.

## Run

Run the http server:

```bash
make run
Open the frontend at `localhost:8000` and the admin at `localhost:8000/admin/`
