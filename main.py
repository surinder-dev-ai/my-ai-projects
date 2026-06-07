# ---------------------------------------------------------
# FastAPI:
# Similar to Spring Boot in Java.
#
# In Java:
# import org.springframework.boot...
#
# Why needed?
# FastAPI gives us:
# - REST API creation
# - routing
# - request handling
# - automatic Swagger docs
# ---------------------------------------------------------
from fastapi import FastAPI


from models.request_models import QuestionRequest
from models.summarize_request import SummarizeRequest
from models.response_models import SummaryResponse

# ---------------------------------------------------------
# Import service layer
#
# Java equivalent:
#
# @Autowired
# private LLMService llmService;
#
# Why needed?
# Keeps controller clean.
# Business logic stays in service layer.
# ---------------------------------------------------------
from services.llm_service import ask_llama, summarize_text

# ---------------------------------------------------------
# Create FastAPI application object
#
# Java equivalent:
# Spring Boot application context
#
# Similar concept:
# @SpringBootApplication
#
# Why needed?
# This becomes the main web application instance.
# Uvicorn looks for this object while starting server.
#
# That's why command was:
# uvicorn main:app --reload
#
# main = filename
# app  = FastAPI object name
# ---------------------------------------------------------
app = FastAPI()
from app_config.config import MODEL_NAME
from app_logging.logger_config import logger
logger.info("Application Started - FastAPI is running")


# ---------------------------------------------------------
# GET endpoint
#
# Java equivalent:
#
# @GetMapping("/")
#
# Why needed?
# Simple health check endpoint.
#
# Used in production for:
# - service health
# - monitoring
# - load balancer checks
# ---------------------------------------------------------
@app.get("/")


# Endpoint handler function
def home():

    # Python dictionary
    # Automatically converted to JSON response
    #
    # Java equivalent:
    # return ResponseEntity.ok(...)
    return {
        "message": "AI API is running"
    }


# ---------------------------------------------------------
# POST endpoint
#
# Java equivalent:
#
# @PostMapping("/ask")
#
# Why POST?
# Because:
# - sending request body
# - user input/question
#
# GET usually used for retrieval only.
# ---------------------------------------------------------
@app.post("/ask")


# FastAPI automatically converts incoming JSON
# into QuestionRequest object
#
# Java equivalent:
#
# public Response askAI(
#      @RequestBody QuestionRequest request)
#
def ask_ai(request: QuestionRequest):

    # -----------------------------------------------------
    # try block
    #
    # Java equivalent:
    #
    # try {
    #   ...
    # } catch(Exception e) {
    #   ...
    # }
    #
    # Why needed?
    # AI APIs/models can fail:
    # - timeout
    # - model unavailable
    # - invalid response
    # - quota issues
    # -----------------------------------------------------
    try:

        # -------------------------------------------------
        # Call service layer
        #
        # Java equivalent:
        # llmService.askLlama(...)
        #
        # Why needed?
        # Controller should delegate business logic
        # to service layer.
        # -------------------------------------------------
        answer = ask_llama(request.question)

        # -------------------------------------------------
        # Return structured JSON response
        #
        # Java equivalent:
        # returning Response DTO
        # -------------------------------------------------
        return {
            "question": request.question,
            "answer": answer
        }

    # -----------------------------------------------------
    # Error handling
    #
    # Java equivalent:
    #
    # catch(Exception e)
    #
    # Production systems NEVER assume success.
    # -----------------------------------------------------
    except Exception as e:

        # Return error response as JSON
        return {
            "error": str(e)
        }
    

# ---------------------------------------------------------
# POST /summarize
#
# Java Equivalent:
#
# @PostMapping("/summarize")
#
# Purpose:
# Summarize large text
# ---------------------------------------------------------
@app.post(
    "/summarize",
    response_model=SummaryResponse
)
def summarize(request: SummarizeRequest):
    try:

        summary = summarize_text(request.text)

        return {
            "summary": summary
        }

    except Exception as e:

        return {
            "error": str(e)
        }