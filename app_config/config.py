# ==========================================================
# config.py
#
# PURPOSE:
# Centralized application configuration.
#
# Java Equivalent:
# application.properties / application.yml
#
# Instead of hardcoding values in code, we keep them
# in .env and load them here.
# ==========================================================

# ----------------------------------------------------------
# Loads values from .env into environment variables
#
# Java equivalent:
# Spring Boot automatically loads application.properties
# ----------------------------------------------------------
from dotenv import load_dotenv

# ----------------------------------------------------------
# os module is used to read environment variables
#
# Java equivalent:
# System.getenv("KEY")
# ----------------------------------------------------------
import os

# ----------------------------------------------------------
# Load the .env file
# ----------------------------------------------------------
load_dotenv()

# ----------------------------------------------------------
# Read values from .env
#
# Java equivalent:
#
# @Value("${model.name}")
# private String modelName;
# ----------------------------------------------------------
APP_NAME = os.getenv("APP_NAME")

APP_VERSION = os.getenv("APP_VERSION")

MODEL_NAME = os.getenv("MODEL_NAME")
