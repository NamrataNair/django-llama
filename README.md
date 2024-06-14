Currently hosted locally at:[https://bit.ly/llama-djang-nn] 

For public view, have written a wrapper code - which integrates Gradio as the primary interface and then processes the request to the django application which inturn called the LLM trained and processes the information/prompt. Gradio creates a temporary link active for 72hrs   

Please note : 
1. There will be an initial deplay in loading the webpage, this is normal in terms of production implementation using Gradio. This delay is only there during the 1st initialization, thereon after there would be no issues.
2. If running the application on a CPU, it will take a lot of time to process the prompt. A single GPU card with 8GB RAM is good enough to load a quantized model and run the application, with support to even Quadro and GeForce RTX cards.  

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
