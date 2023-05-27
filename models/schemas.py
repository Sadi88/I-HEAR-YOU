from pydantic import BaseModel


class BaseSchema(BaseModel):
    name_tm: str
    name_ru: str
    
    
class subCategorySchema(BaseSchema):
    category_id: int
    
    
class productSchema(subCategorySchema):
    description_tm: str
    description_ru: str
    subcategory_id: int


class loginSchema(BaseModel):
    email: str
    password: str
    
class registerSchema(loginSchema):
    username: str
    status: str 
