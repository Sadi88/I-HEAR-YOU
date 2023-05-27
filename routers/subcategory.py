from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import *
from sqlalchemy.orm import Session
from db import get_db
import crud
from models import subCategory, subCategorySchema


subcategory_router = APIRouter()


@subcategory_router.post('/add-subcategory')
def add_product(req: subCategorySchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_crud(req, subCategory, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')