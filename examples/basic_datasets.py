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
from greenfield_python_sdk.protos.greenfield.sp import QueryStorageProvidersRequest
from greenfield_python_sdk.protos.greenfield.storage import VisibilityType
from greenfield_python_sdk.storage_provider.utils import create_example_object
from datasets import load_dataset


logging.basicConfig(level=logging.INFO)

config = get_account_configuration()

def read_file_to_buffer(file_path):
    """
    Reads the content of a local file and returns it as a BytesIO object.

    Parameters:
    file_path (str): The path to the file to be read.
    """

    with open(file_path, 'rb') as file:
        content = file.read()

    return io.BytesIO(content)

async def main():
    network_configuration = NetworkConfiguration(**NetworkTestnet().model_dump())
    key_manager = KeyManager(private_key=config.private_key)

    logging.info(f"Main account address: {key_manager.address}")
    
    async with GreenfieldClient(network_configuration=network_configuration, key_manager=key_manager) as client:
        logging.info(f"---> TEST Greenfield <---")
        bucket_name = "bucket_name"
        object_name = "object_name"
        await client.async_init()

        ## Get Storage Providers
        sps = (await client.blockchain_client.sp.get_storage_providers(QueryStorageProvidersRequest())).sps

        # Load dataset
        dataset = load_dataset("HuggingFaceH4/no_robots")

        # Save locally
        dataset.save_to_disk("your_local_directory")

        zip_output_filename = 'you_zip_file_name'

        shutil.make_archive(zip_output_filename, '', folder_to_compress)

        ## Create Object
        # Open the file in binary mode and read its contents
        content = read_file_to_buffer(zip_output_filename)

        # Send Create Object Transaction
        logging.info(f"---> Create Object <---")
        object = await client.object.create_object(
            bucket_name,
            object_name,
            reader=content,
            opts=CreateObjectOptions()
        )
        logging.info(f"Result: {object}\n\n")
        await client.basic.wait_for_tx(hash=object)

        # Send Put Object Transaction to SP and wait for seal
        logging.info(f"---> Put Object <---")
        put_object = await client.object.put_object(
            bucket_name,
            object_name,
            object_size=content.getbuffer().nbytes,
            reader=content.getvalue(),
            opts=PutObjectOptions()
        )
        logging.info(f"Result: {put_object}\n\n")

        await asyncio.sleep(8)

        # Make sure the dataset is stored in Greenfield
        logging.info(f"---> Get Object <---")
        get_object = await client.object.get_object(
            bucket_name,
            object_name,
            opts=GetObjectOption()
        )
        logging.info(f"Result: {get_object}\n\n")

        ## Download Object
        path = "path/to/your/local/folder"
        logging.info(f"---> Get Object <---")
        await client.object.fget_object(
                   bucket_name,
                   object_name,
                   path,
        opts=GetObjectOption()
               )

        logging.info(f"Result: {get_object}\n\n")

        # load dataset from local directory
        dataset = load_dataset('parquet', data_files='path/to/my/dataset/folder')



if __name__ == "__main__":
    asyncio.run(main())