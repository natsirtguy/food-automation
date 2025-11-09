# Development Workflow

This document describes the development workflow for the Food Automation project.

## Overview

The project uses **Claude Code** (desktop or web) for development with:
- **Jira** for task tracking (project key: FA)
- **GitHub** for code storage and pull requests

## Setup

### 1. GitHub Repository

The repository is hosted at https://github.com/natsirtguy/food-automation

```bash
# Clone the repository
git clone https://github.com/natsirtguy/food-automation.git
cd food-automation
```

### 2. Jira Integration

- **Project**: Food Automation (FA)
- **Workspace**: natsirtguy.atlassian.net
- Always reference task keys (FA-X) in commits and PRs

## Standard Workflow

1. **Check Jira** for next task to work on
2. **Create/checkout feature branch** (Claude Code handles this automatically)
3. **Work on the task** with Claude Code assistance
4. **Run checks**: `hatch run check` (format, lint, typecheck, test)
5. **Commit changes** with Jira task reference
6. **Push to GitHub**
7. **Create pull request** for code review
8. **Update Jira** task status after PR is merged

## Example Session

```bash
# Work with Claude Code
# "Let's work on FA-3: Research and configure AI vision services"

# Claude Code will:
# - Create a feature branch (e.g., claude/fa-3-vision-setup-xxxxx)
# - Make necessary changes
# - Run quality checks
hatch run check

# - Commit with proper message
git commit -m "[FA-3] Add OpenAI and Anthropic API configuration"

# - Push to branch
git push -u origin claude/fa-3-vision-setup-xxxxx

# - Create pull request
gh pr create --title "[FA-3] Add AI vision service configuration" --body "..."

# - Update Jira status
```

## Tips and Best Practices

### General Development
- Always run `hatch run check` before committing
- Keep commits focused and reference Jira tasks with [FA-X] prefix
- Update Jira status as you progress
- Use pull requests for all changes to enable code review
- Mark Jira tasks "Done" only after PR is merged

### Code Quality
- Format: `hatch run format`
- Lint: `hatch run lint`
- Type check: `hatch run typecheck`
- Test: `hatch run test`
- All checks: `hatch run check`

### Commit Messages
Use descriptive commit messages with [FA-X] prefix:
```
[FA-3] Add OpenAI and Anthropic API configuration
[FA-5] Implement image analysis pipeline
[FA-7] Add inventory data models
```

### Jira Task Completion Policy

**For Coding Tasks:**
- ✅ Mark as "Done" **after PR is merged to main branch**
- ✅ Can update to "In Progress" when actively working
- ✅ Add comments to document significant progress or decisions

**For Non-Coding Tasks:**
- ✅ Research, documentation, or planning tasks can be marked Done without requiring a merged PR

**Rationale**: Tasks should only be marked Done when the code is in the main branch, ensuring the task status accurately reflects completion.

## Documentation Updates

**IMPORTANT**: Only update documentation files **after completing a Jira task unit of work**, not during ongoing development.

### When to Update

Update documentation when:
- ✅ A Jira task (FA-X) is fully completed and tested
- ✅ Significant architectural changes have been implemented
- ✅ New modules, patterns, or conventions are established
- ✅ Project structure or tech stack changes

Do NOT update for:
- ❌ Work in progress on a task
- ❌ Minor bug fixes or tweaks
- ❌ Experimental code that might be reverted
- ❌ Partial implementations

### What to Update

After completing a Jira task:

**Documentation Files** (if relevant):
- `README.md` - If setup instructions or usage changed
- `CLAUDE.md` - If project context or workflow changed
- `requirements.md` / `implementation-guide.md` - If requirements evolved

### How to Update

```bash
# After completing FA-X task and before marking it Done:

# 1. Review what changed
git log --oneline -5

# 2. Update relevant documentation files (if needed)
# Edit README.md, CLAUDE.md, etc.

# 3. Commit documentation updates
git add .
git commit -m "[FA-X] Update documentation"
git push

# 4. Include in PR or create separate documentation PR

# 5. Mark Jira task as Done after PR is merged
```

**Rationale**: Keeping documentation updates tied to Jira tasks ensures they reflect stable, tested changes rather than work-in-progress.

## Troubleshooting

### Tests Failing
- Review test output carefully
- Run individual tests: `hatch run pytest tests/test_specific.py`
- Check for environment issues or missing dependencies

### Merge Conflicts
- Pull latest changes: `git pull origin main`
- Resolve conflicts manually
- Test after resolving: `hatch run check`
- Commit conflict resolution

### Lost Context
- Check Jira task description and comments
- Review recent commits on GitHub
- Read CLAUDE.md for project overview
- Check requirements.md and implementation-guide.md
