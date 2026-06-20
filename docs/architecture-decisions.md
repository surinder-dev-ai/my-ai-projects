    # Architecture Decisions

## ADR-001

Decision:
Use `cross_cutting/` to group infrastructure concerns that apply across the application.

Reason:
Improves logical organization and separates business logic from technical infrastructure.

Examples:
- Request ID
- Logging
- Authentication
- Metrics
- Tracing

Trade-offs:
Less conventional than a top-level `middleware/` package for FastAPI developers, but provides a broader and more scalable organizational concept.