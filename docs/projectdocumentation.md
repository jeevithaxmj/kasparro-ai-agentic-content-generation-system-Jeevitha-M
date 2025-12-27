# Problem Statement

Design and implement a modular multi-agent system that ingests structured product data and autonomously generates machine-readable content pages using reusable logic blocks, templates, and orchestrated agents.

# Solution Overview

This solution implements an agentic content generation pipeline composed of independent agents, reusable content logic blocks, and a custom template engine. The system converts raw product data into structured internal models, generates categorized user questions, applies transformation logic, and assembles multiple content pages as clean JSON outputs.

# Scopes & Assumptions

- The system operates only on the provided product dataset.
- No external data sources or domain knowledge are used.
- Product B in the comparison page is fictional and internally defined.
- The system is deterministic and designed for extensibility.
- The focus is on system design and automation, not content creativity.

# System Design

The system is designed as a modular, agentic content generation pipeline where each agent has a single, well-defined responsibility and communicates through structured data contracts. The architecture emphasizes reusability, composability, and deterministic orchestration rather than monolithic execution.

At a high level, the system converts raw product data into structured internal models, applies reusable content transformation logic, and assembles multiple machine-readable content pages using a custom template engine. All execution is coordinated through an explicit orchestration flow.

1. Agent Roles & Responsibilities

Parser Agent
The Parser Agent is responsible for ingesting raw product input and converting it into a normalized internal Product Model. This ensures downstream agents operate on a consistent schema, decoupling the system from raw input formats.

Question Generation Agent
This agent generates a categorized set of user questions based solely on the structured Product Model. Categories include informational, usage, safety, purchase, and comparison questions. The agent does not perform content formatting and outputs only structured question data.

Content Logic Block Agents
Content logic blocks are reusable transformation units that apply deterministic rules to structured data. Each block performs a single type of transformation, such as extracting benefits, usage instructions, safety considerations, or ingredient comparisons. These blocks are intentionally page-agnostic and can be reused across multiple templates and page types.

Template Engine Agent
The Template Engine Agent defines structured templates that specify required fields, dependencies on content logic blocks, and output schemas. Templates act as contracts that govern how content blocks are assembled, ensuring consistent and machine-readable outputs across pages.

Page Assembly Agents
Page-specific agents (FAQ Page Agent, Product Page Agent, Comparison Page Agent) are responsible for selecting the appropriate template, invoking the required content logic blocks, and assembling the final page output as structured JSON. Each page agent produces exactly one output artifact.

Orchestrator
The Orchestrator controls the execution flow of the system. It initializes agents, manages execution order, and passes structured data between agents. The orchestrator contains no business logic and exists solely to coordinate the agent pipeline.

2. Orchestration Flow

The system executes as a deterministic, step-based pipeline:

Raw product data is parsed by the Parser Agent into a Product Model.

The Product Model is passed to the Question Generation Agent.

Content logic blocks are executed to generate structured content components.

The Template Engine applies page-specific templates.

Page Assembly Agents produce final JSON outputs.

This flow ensures clear data lineage from input to output and allows individual agents to be replaced or extended without impacting the overall system.

3. System Properties

Modularity: Each agent has a single responsibility and clear input/output boundaries.

Reusability: Content logic blocks and templates can be reused across multiple page types.

Extensibility: New agents, templates, or page types can be added without modifying existing logic.

Determinism: The system operates without hidden global state or external dependencies.

Machine-Readable Output: All final artifacts are structured JSON designed for downstream consumption
