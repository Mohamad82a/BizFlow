from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional


router = APIRouter(prefix='/bizops', tags=['bizops'])

@router.get('/test/', status_code=status.HTTP_200_OK)
def test_something(str:str):
    return {'message': f'Test {str}'}