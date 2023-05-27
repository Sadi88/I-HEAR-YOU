from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import *
from sqlalchemy.orm import Session
from db import get_db
import crud
from models import Image


image_router = APIRouter()

@image_router.post('/upload-image')
def uplaod_image(id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    try:
        result = crud.create_img(id, file, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')
    

@image_router.delete('/delete-image/{id}')
def delete_image(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.delete_img(id, db)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'result': 'DELETED'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'NOT'})
    