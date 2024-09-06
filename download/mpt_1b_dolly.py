import transformers
model = transformers.AutoModelForCausalLM.from_pretrained('mosaicml/mpt-1b-redpajama-200b-dolly', trust_remote_code=True)
