import os

import pytest

from main import EnvironmentType, Settings


class TestSettings:
    @pytest.fixture(autouse=True)
    def set_env_vars(self):
        os.environ["DEBUG"] = "True"
        os.environ["ENVIRONMENT"] = "development"
        os.environ["APP_VERSION"] = "1.0.0"
        os.environ["BASE_URL"] = "https://howiti.com"

    def test_settings_loading(self):
        settings = Settings()
        assert settings.debug is True
        assert settings.environment == EnvironmentType.DEVELOPMENT
        assert settings.app_version == "1.0.0"
        assert settings.base_url == "https://howiti.com"
