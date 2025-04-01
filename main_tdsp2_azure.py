from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import Optional, List
from openai_client import get_openai_response
from file_handler import save_upload_file_temporarily


from base_logger import logger

# Import the functions you want to test directly
from functions import *

app = FastAPI(title="IITM Assignment API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
@app.post("/api/")
async def process_question(
    # question: str = Form(...), file: Optional[UploadFile] = File(None)
    question: str = Form(...),
    file: List[UploadFile] = File([]),
):
    print(" " * 80)
    print("=" * 80)
    print(" " * 80)

    logger.info(f"Received question: {question}")
    logger.info(f"Number of files received: {len(file)}")
    try:
        # Save file temporarily if provided
        logger.info(f"Attempting to save the file")
        temp_file_path = None
        if file:
            logger.info(f"Detected that file has been received")
            if len(file) == 1:
                logger.info(f"Only single file received")
                logger.info(f"Attempting to save the file")
                temp_file_path = await save_upload_file_temporarily(file[0])
                logger.info(f"Successfully saved the file to {temp_file_path}")

            elif len(file) > 1:
                file_path_list = []
                logger.info(f"Multiple files received")
                logger.info(f"Attempting to save multiple files")
                for counter, f in enumerate(file):
                    logger.info(f"Saving file {counter} of {len(file)}")
                    temp_file_path = await save_upload_file_temporarily(f)
                    logger.info(f"Saved succesfully to {temp_file_path}")
                    file_path_list.append(temp_file_path)

        # Get answer from OpenAI
        logger.info(f"Sending question to openai {question}")
        answer = await get_openai_response(question, temp_file_path)

        return {"answer": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


from fastapi.responses import PlainTextResponse
from fastapi import Query


@app.get("/wiki")
async def wiki_entrypoint(
    country: str = Query(..., title="Country"), response_class=PlainTextResponse
):
    print("Inside wiki_entrypoint")
    from functions import generate_markdown_outline

    outline = await generate_markdown_outline(country)
    return outline


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting FastAPI server...")
    uvicorn.run("main_tdsp2_azure:app", host="0.0.0.0", port=8000, reload=True)
    # uvicorn.run("app", host="0.0.0.0", port=8000, reload=True)
