# ---------------------------------------------------------
# BaseModel from Pydantic:
#
# Used for request validation and schema definition.
#
# Java equivalent:
# DTO / Request class
#
# Similar to:
#
# public class QuestionRequest {
#     private String question;
# }
#
# Why needed?
# So API knows expected JSON structure.
# Also validates incoming request automatically.
# ---------------------------------------------------------
from pydantic import BaseModel

# ---------------------------------------------------------
# Request DTO / Request Model
#
# Java equivalent:
#
# public class QuestionRequest {
#     private String question;
# }
#
# Why needed?
# Defines incoming JSON structure.
#
# Expected JSON:
#
# {
#   "question": "What is Kafka?"
# }
#
# FastAPI automatically:
# - validates request
# - converts JSON to Python object
# - returns validation errors if incorrect
# ---------------------------------------------------------
class QuestionRequest(BaseModel):

    # Expected field from incoming JSON request
    question: str
