from pydantic import ConfigDict

FROZEN_CONFIG = ConfigDict(frozen=True)
# frozen -> 얼어 있다.
# 얼어있는 객체 -> 생성이후에는 변경 할 수 없는 객체
# immutable
