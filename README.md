# Food Automation

AI-powered food inventory monitoring system that tracks what food you have, quantities, and freshness without requiring daily user input.

## Development Workflow

This project supports **hybrid development** from both desktop and mobile:
- **Desktop**: Use Claude Code for full development
- **Mobile**: Use Claude web with patch-based workflow

**📋 See [WORKFLOW.md](WORKFLOW.md) for complete workflow documentation**

**📝 See [CLAUDE.md](CLAUDE.md) for project context and AI assistant guidance**

## Setup

### Requirements

- Python 3.12+
- [Hatch](https://hatch.pypa.io/) for project management

### Installation

1. Install hatch if you haven't already:
```bash
pip install hatch
```

2. Clone the repository:
```bash
git clone <repository-url>
cd food-automation
```

3. Create and activate the virtual environment:
```bash
hatch shell
```

This will automatically create a virtual environment with all dependencies installed.

### Development

#### Running the CLI

```bash
fridge <path-to-photo>
```

Or from the project root without installing:
```bash
hatch run python -m food_automation.cli <path-to-photo>
```

#### Running Tests

```bash
hatch run test
```

#### Code Quality Checks

```bash
# Format code
hatch run format

# Lint code
hatch run lint

# Type check
hatch run typecheck

# Run all checks + tests
hatch run check
```

## Project Status

Currently implementing **Phase 1: AI Processing Pipeline** (Epic FA-1).

See `requirements.md` and `implementation-guide.md` for detailed project documentation.

## Project Management

- **GitHub**: https://github.com/natsirtguy/food-automation
- **Jira**: Food Automation (FA) project at natsirtguy.atlassian.net
- **Task Tracking**: All work references Jira tasks (FA-X format)
