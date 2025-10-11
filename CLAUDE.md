# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Food Automation is an AI-powered food inventory monitoring system that automatically tracks food items, quantities, and freshness using computer vision. The system processes refrigerator photos (initially manual, eventually automated via ESP32-CAM) to maintain an accurate inventory without user input.

**Key Philosophy**: Start simple (Python + JSON + smartphone photos), prove the concept with AI processing first, then build proper data models, and finally add hardware automation.

## Development Workflow

This project uses a **hybrid development approach**:

### Claude Code (Desktop)
When working from a computer, use Claude Code for full development capabilities including:
- Direct file editing and commits
- Running tests and code quality checks
- Updating Jira tasks
- Git operations

### Claude Web (Mobile)
When working from a phone via claude.ai:

**IMPORTANT**: You must create patches for ALL code changes instead of editing files directly.

For each change:
1. Generate a **raw git patch** using git format-patch
2. Save in location for user to download
3. Provide download link and ready-to-run Termux command
4. User downloads patch and runs command in Termux

**Workflow**: Download patch → Run Termux command → PR created directly.

**Context for Claude Web**:
- Reference the active Jira task (FA-X) in all work
- This file (CLAUDE.md) provides project context
- See WORKFLOW.md for detailed Termux patch workflow
- Check requirements.md and implementation-guide.md for project details

### Jira Task Management
- All development work should reference a Jira task (FA-X)
- Update task status as work progresses
- Add comments to tasks documenting significant progress
- Use Jira to coordinate between Claude Code and Claude web sessions

**Task Completion Policy**:
- **Claude Code**: Mark coding tasks "Done" only after code is pushed to GitHub
- **Claude Web**: Do NOT mark coding tasks "Done" (can update to "In Progress" or add comments)
- **Non-coding tasks** (research, planning): Can be marked Done without git push
- **User override**: User can mark tasks Done manually at any time

### Repository Access
- **GitHub**: https://github.com/natsirtguy/food-automation
- Public repository required for Claude web access to codebase
- All changes should go through git (patches or direct commits)

## Development Environment

This project uses **Hatch** for Python environment and dependency management.

**IMPORTANT**: Always use `hatch run` to execute Python commands and scripts.

### Common Commands
```bash
# Run Python scripts
hatch run python -m tests.check_openai <image-path>
hatch run python -m tests.check_anthropic <image-path>

# Run tests
hatch run test

# Code quality checks
hatch run format    # Format code with ruff
hatch run lint      # Lint code with ruff
hatch run typecheck # Type check with pyright
hatch run check     # Run all checks (format, lint, typecheck, test)
```

### Environment Details
- Virtual environment location: `.hatch/food-automation/`
- Python version: 3.12+
- Dependencies defined in: `pyproject.toml`
- The hatch environment is automatically created and managed

**Never use bare `python` or `pip` commands** - always prefix with `hatch run`.

## Development Approach

### Phase-Based Implementation

1. **Phase 1 (Current Priority)**: AI Processing Pipeline
   - Prove GPT-4V or Google Vision can identify food items and count quantities
   - Manual smartphone photo workflow
   - Success threshold: 80%+ accuracy on real fridge photos

2. **Phase 2**: Data Models & Storage
   - JSON-based inventory tracking (inventory.json, history.json, config.json)
   - Simple query interface for inventory state

3. **Phase 3**: Camera Hardware System
   - ESP32-CAM with door-triggered photo capture (light sensor)
   - WiFi upload integration with AI pipeline
   - Target: 6+ month battery life

### Jira Integration

- **Project Key**: FA (Food Automation)
- Track epics and stories aligned with the three-phase approach
- All work items should reference the appropriate phase

## Architecture Principles

**Modularity**: AI processing, data storage, photo capture, and UI are independent concerns that can be developed in parallel.

**Extensibility**: Design with future MCP server integration in mind - the inventory data should be queryable programmatically for AI assistant access.

**Local First**: Start with local JSON storage and filesystem-based photo handling before adding cloud/remote capabilities.

## Technical Stack

- **Language**: Python
- **AI Services**: OpenAI GPT-4V (primary), Google Cloud Vision (alternative)
- **Storage**: JSON files for MVP
- **Hardware**: ESP32-CAM with photoresistor door trigger (Phase 3)
- **Future**: MCP server for AI assistant integration

## Data Model (Phase 2)

Inventory items track:
- Food item name and category
- Quantity (count-based: "3 apples", "2 milk cartons")
- Entry/exit timestamps for freshness
- Leftover detection (special handling for homemade food)
- Confidence scores from AI analysis
- Location within fridge

## Key Constraints

- **Fully automatic**: No user notifications or confirmations required
- **Pull-based**: User checks status when needed, no push alerts
- **Non-intrusive**: Background operation
- **Hobby pace**: Evenings/weekends development, not production-critical
- **Rebuild-friendly**: Accept simple solutions that may need refactoring as requirements clarify
