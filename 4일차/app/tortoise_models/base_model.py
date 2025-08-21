from tortoise import fields


class BaseModel:
    id = fields.BigIntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)


# MYSQL: primary key를 정할때 주의해야 되는 점
# MYSQL version 8이상 부터라면 (5.7부터도 쓰긴함)
# innodb가 Default engine (옛날 MYISAM)

# innodb의 특징 중 하나 -> clustering index
# primary key를 기준으로
# primary key 값이 비슷한 row 들끼리 disk에서도 실제로 모여있다.


# HDD
# 랜던 IO가 느리고, 순차 IO가 빠르다.
