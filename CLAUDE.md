# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Food Automation is an AI-powered food inventory monitoring system that automatically tracks food items, quantities, and freshness using computer vision. The system processes refrigerator photos (initially manual, eventually automated via ESP32-CAM) to maintain an accurate inventory without user input.

**Key Philosophy**: Start simple (Python + JSON + smartphone photos), prove the concept with AI processing first, then build proper data models, and finally add hardware automation.

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
