from applyflow.config import Settings


def test_demo_mode_is_enabled_by_default(monkeypatch):
    monkeypatch.delenv("APPLYFLOW_DEMO_MODE", raising=False)
    settings = Settings(_env_file=None)
    assert settings.demo_mode is True


def test_environment_variable_overrides_default(monkeypatch):
    monkeypatch.setenv("APPLYFLOW_DEMO_MODE", "false")
    settings = Settings(_env_file=None)
    assert settings.demo_mode is False
