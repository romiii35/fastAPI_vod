# main.py

from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, Query
from app.models.users import UserModel
from app.schema.users import UserCreateRequest, UserUpdateRequest, UserSearchParams


# FastAPI 앱 인스턴스를 먼저 생성
app = FastAPI()

# API 테스트를 위한 더미 데이터 생성 메서드 호출
UserModel.create_dummy()


@app.post('/users')
async def create_user(data: UserCreateRequest):
    user = UserModel.create(**data.model_dump())
    return user.id


@app.get('/users')
async def get_all_users():
    result = UserModel.all()
    if not result:
        raise HTTPException(status_code=404)
    return result


@app.patch('/users/{user_id}')
async def update_user(data: UserUpdateRequest, user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404)
    user.update(**data.model_dump())
    return user


@app.delete('/users/{user_id}')
async def delete_user(user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404)
    user.delete()
    return {'detail': f'User: {user_id}, Successfully Deleted.'}


@app.get('/users/search')
async def search_users(query_params: Annotated[UserSearchParams, Query()]):
    valid_query = {key: value for key, value in query_params.model_dump().items() if value is not None}
    filtered_users = UserModel.filter(**valid_query)
    if not filtered_users:
        raise HTTPException(status_code=404)
    return filtered_users


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)