# AgentFlow

AgentFlow is an **agentic ML workflow orchestration and RAG evaluation platform** for developer workflows. It is designed to decompose software tasks, retrieve project context, route subtasks to specialized agents, and evaluate execution quality using measurable ML-style benchmarks.

This repository is currently in progress. The scaffold focuses on the core architecture, benchmark design, retrieval layer, agent workflow contracts, and evaluation pipeline that support the project description used for the Amazon ML Summer School application.

## Project Identity

- **Title:** AgentFlow: Agentic ML Workflow Orchestration and RAG Evaluation Platform
- **Domain:** Natural Language Processing / Machine Learning / AI Systems
- **Project Type:** Applied AI / ML System / Research Prototype
- **Status:** In progress
- **Repository:** https://github.com/17dhruv/AgentFlow

## What AgentFlow Builds Toward

AgentFlow combines:

- Multi-agent workflow planning for developer tasks
- RAG-based project context retrieval
- Structured tool-call and workflow-state tracking
- Evaluation pipelines for benchmarked task execution
- Future task-router experiments for learning-based agent selection

The project does **not** currently claim model training or fine-tuning results. Metrics are framed as planned or scaffolded until benchmark runs are implemented and recorded.

## Current Components

- `backend/` - FastAPI service scaffold for task submission, retrieval, orchestration, and evaluation results
- `agents/` - Agent roles, workflow state contracts, and orchestration skeleton
- `rag/` - Document ingestion, chunking, retrieval, and citation-aware context interfaces
- `evaluation/` - Benchmark runner and metrics functions
- `datasets/` - Sample developer-workflow benchmark records
- `experiments/task_router/` - Future lightweight ML task-router experiment placeholder
- `docs/` - Architecture notes and application form answers
- `configs/` - Default configuration for local experiments
- `tests/` - Focused tests for evaluation and workflow contracts

## Application Summary

AgentFlow is an agentic ML infrastructure project for automating developer workflows using multi-agent orchestration, retrieval-augmented generation, structured task planning, and evaluation pipelines. It coordinates specialized agents for planning, debugging, code generation, validation, and workflow state management while measuring performance through benchmark tasks and retrieval-quality metrics.

## Planned Metrics

- Task completion rate
- Tool-call success rate
- Retrieval precision@k
- Answer faithfulness
- Average workflow latency
- Human-rated solution quality

## Quick Start

This repo is a scaffold. Once Python dependencies are installed, the intended backend entrypoint will be:

```bash
uvicorn backend.app.main:app --reload
```

The benchmark runner is planned around JSONL records in `datasets/benchmark_sample.jsonl`.

## Honesty Note

AgentFlow is being built as an applied AI system. Until evaluation runs are completed, metrics should be described as planned or in progress, not as achieved production results.
