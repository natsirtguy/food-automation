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
1. Generate a git patch file showing the changes
2. User will copy/paste and save the patch locally on their device
3. Include the Jira task key in the patch description
4. Document what the patch does and why

**Patch Format**:
```
From: Claude <noreply@anthropic.com>
Subject: [FA-X] Brief description

Detailed explanation of changes and how to apply the patch.

---
diff --git a/path/to/file b/path/to/file
index abc123..def456 100644
--- a/path/to/file
+++ b/path/to/file
@@ -1,3 +1,5 @@
[actual diff content]
```

**Note**: Patches are NOT committed to the repository. The user saves them locally and applies them when back at their computer.

**Context for Claude Web**:
- Reference the active Jira task (FA-X) in all work
- This file (CLAUDE.md) provides project context
- See WORKFLOW.md for detailed patch workflow
- Check requirements.md and implementation-guide.md for project details

### Jira Task Management
- All development work should reference a Jira task (FA-X)
- Update task status as work progresses
- Add comments to tasks documenting significant progress
- Use Jira to coordinate between Claude Code and Claude web sessions

### Repository Access
- **GitHub**: https://github.com/natsirtguy/food-automation
- Public repository required for Claude web access to codebase
- All changes should go through git (patches or direct commits)

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
