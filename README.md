# ai-trends
This repo contains a prototype for an AI trends summarizer. 
The code can be used to summarize the abstracts of the top AI papers per month according to [HuggingFace daily papers](https://huggingface.co/papers).
It also creates a list of the top concepts for each month.


## Requirements

* Python >= 3.7
* Additional packages are defined in the [requirements.txt]() file.
* Token for [HuggingFace Serverless Inference](https://huggingface.co/docs/api-inference/getting-started), a free account is fine.

It is recommended to create a virtual environment and install the packages there.
```commandline
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Running

First, clone the repo.
Then, run the summarizer as follows.
```commandline
python summarize_hf.py -m '01,02' -y 2025 -k 5 -o hf_report.html -t <HUGGINGFACE_TOKEN>
```
### Options
* `-m`, months to download, note the leading `0` for single digit month numbers, and use quotes for multiple months, eg. `'01,02,04'`.
* `-y`, years to download, same syntax as months.
* `-k`, How many papers to summarize for each month.
* `-o`, filename to write the html report to.
* `-t`, HuggingFace token with Serverless Inference access.