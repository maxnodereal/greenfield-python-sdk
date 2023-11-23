#import boto3
import asyncio
import logging
import random
import string
import io

from greenfield_python_sdk.config import NetworkConfiguration, NetworkTestnet, get_account_configuration
from greenfield_python_sdk.greenfield_client import GreenfieldClient
from greenfield_python_sdk.key_manager import KeyManager
from greenfield_python_sdk.models.bucket import CreateBucketOptions
from greenfield_python_sdk.models.object import CreateObjectOptions, GetObjectOption, PutObjectOptions
from transformers import T5ForConditionalGeneration, T5Tokenizer


logging.basicConfig(level=logging.INFO)

config = get_account_configuration()

async def main():
    network_configuration = NetworkConfiguration(**NetworkTestnet().model_dump())
    key_manager = KeyManager(private_key=config.private_key)

    logging.info(f"Main account address: {key_manager.address}")

    async with GreenfieldClient(network_configuration=network_configuration, key_manager=key_manager) as client:
        logging.info(f"---> TEST Greenfield <---")
        bucket_name = "bucket_name"
        object_name = "object_name"
        await client.async_init()

        ## download Object of model
        path = "/path/to/your/dir"
        logging.info(f"---> Get Object <---")
        await client.object.fget_object(
            bucket_name,
            object_name,
            path,
            opts=GetObjectOption()
        )
        logging.info(f"Result: {fget_object}\n\n")


		# Load model and tokenizer
		model = T5ForConditionalGeneration.from_pretrained(path)
		tokenizer = T5Tokenizer.from_pretrained(model_dir,legacy=False)

		# Prepare input text
		input_text = "translate English to French: The quick brown fox jumps over the lazy dog."

		# Tokenize input text
		input_ids = tokenizer.encode(input_text, return_tensors="pt")

		# Generate output with max_new_tokens
		output = model.generate(input_ids, max_new_tokens=50)  # Generates up to 50 new tokens

		# Decode and print the translated text
		translated_text = tokenizer.decode(output[0], skip_special_tokens=True)
		print(translated_text)

if __name__ == "__main__":
    asyncio.run(main())


