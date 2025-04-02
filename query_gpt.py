import os
import httpx
import pandas as pd
from dotenv import load_dotenv

from base_logger import logger

load_dotenv()

# AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
# AIPROXY_BASE_URL = "https://aiproxy.sanand.workers.dev/openai/v1"

USE_PERSONAL_TOKEN = True

if USE_PERSONAL_TOKEN:
    AIPROXY_TOKEN = os.environ["OPENAI_API_MYKEY"]
    # OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
    AIPROXY_BASE_URL = "https://api.openai.com/v1"

else:
    AIPROXY_TOKEN = os.environ["AIPROXY_TOKEN"]
    # OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    AIPROXY_BASE_URL = "http://aiproxy.sanand.workers.dev/openai/v1"


async def query_gpt(headers, payload):
    from fastapi import HTTPException

    try:
        logger.info(f"Making request to openai")
        logger.info(f"Using URL: {f"{AIPROXY_BASE_URL}/chat/completions"}")

        if "Authorization" in headers:
            logger.info(f"Authorization is already present in headers")

        else:
            logger.info(f"Authorization not received in the headers. Adding to headers")
            headers["Authorization"] = f"Bearer {AIPROXY_TOKEN}"

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{AIPROXY_BASE_URL}/chat/completions",
                headers=headers,
                json=payload,
                timeout=60.0,
            )

            if response.status_code != 200:
                logger.info(f"Error from openAI")
                raise Exception(f"Error from OpenAI API: {response.text}")

            logger.info("Response received successfully")
            result = response.json()
            return result

    except KeyError as e:
        logger.error(f"KeyError occurred while querying GPT: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        logger.error(f"General Error while querying gpt: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
