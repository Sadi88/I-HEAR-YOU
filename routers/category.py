from fastapi import *
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import *
from sqlalchemy.orm import *
from db import get_db
import crud
from models import BaseSchema, Category



category_router = APIRouter()


@category_router.post('/add-category')
def add_product(req: BaseSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_crud(req, Category, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')
    
    
@category_router.get('/get-category')
def get_category(db: Session = Depends(get_db)):
    try:
        result = crud.read_category(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')