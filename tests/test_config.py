"""Unit tests for testing the development and production configurations."""

from matl_online.app import create_app
from matl_online.settings import DevConfig, ProdConfig


def test_production_config():
    """Production config."""
    app = create_app(ProdConfig)
    assert app.config['ENV'] == 'prod'
    assert app.config['DEBUG'] is False
    assert app.config['ASSETS_DEBUG'] is False


def test_dev_config():
    """Development config."""
    app = create_app(DevConfig)
    assert app.config['ENV'] == 'dev'
    assert app.config['DEBUG'] is True
    assert app.config['ASSETS_DEBUG'] is True
