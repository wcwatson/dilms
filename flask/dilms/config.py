"""This module contains configurations and secrets for managing DILMS."""

import os


class Config(object):
    """Class for managing configurations and secrets for the DILMS webapp.

    More TK.
    """
    DEBUG = False
    DEVELOPMENT = False
    POSTGRES_DB_NAME = os.getenv('POSTGRES_DB_NAME', 'test_dilms')
    POSTGRES_DB_URI = os.getenv('POSTGRES_DB_URI', 'wwatson:///test_dilms')
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'flask')
    POSTGRES_PW = os.getenv('POSTGRES_PW', 'capta')


class ProductionConfig(Config):
    """For production."""
    pass


class StagingConfig(Config):
    """For final staging."""
    DEBUG = True


class DevelopmentConfig(Config):
    """For development work."""
    DEBUG = True
    DEVELOPMENT = True
