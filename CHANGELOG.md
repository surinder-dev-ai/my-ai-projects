# Changelog

All notable changes to this project will be documented in this file.

## v0.1.0 - Initial Foundation

### Added

* FastAPI application setup
* Uvicorn server integration
* Swagger/OpenAPI documentation
* Ollama integration with local Llama model
* Layered architecture (Controller → Service → Provider)
* Request and response models using Pydantic
* Centralized logging
* Environment-based configuration using `.env`
* Provider abstraction (`AIProvider`)
* `ProviderFactory` for provider creation
* Custom exception (`AIProviderException`)
* Global exception handling
* Health check endpoint (`/health`)
* Git repository and GitHub integration

### Architecture

* Introduced provider abstraction to reduce coupling
* Established a clean separation of concerns between controller, service, and provider layers
* Externalized configuration from source code
