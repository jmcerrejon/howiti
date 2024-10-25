import pytest

from schemas import UserType


class TestUserType:
    @pytest.mark.parametrize(
        "user_type, value", [(UserType.STANDARD, "standard"), (UserType.ADMIN, "admin")]
    )
    def test_user_type_values(self, user_type, value):
        assert user_type.value == value

    def test_user_type_enum(self):
        assert isinstance(UserType.STANDARD, UserType)
        assert isinstance(UserType.ADMIN, UserType)
