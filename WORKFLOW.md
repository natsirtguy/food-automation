# Development Workflow

This document describes the hybrid development workflow for the Food Automation project, allowing development from both desktop (Claude Code) and mobile (Claude web).

## Overview

The project uses a **dual-environment workflow**:
- **Desktop**: Claude Code CLI for full development capabilities
- **Mobile**: Claude web (claude.ai) for code review and patch generation

All work is tracked in **Jira** (project key: FA) and synchronized via **GitHub**.

**📱 See [MOBILE.md](MOBILE.md) for complete mobile development guide with Termux setup and patch workflow**

## Setup

### 1. GitHub Repository

Create a public GitHub repository:

```bash
# Create repo on GitHub, then:
git remote add origin https://github.com/<username>/food-automation.git
git branch -M master
git push -u origin master
```

Public access is required for Claude web to read the repository.

### 2. Claude Projects

#### Claude Code (Desktop)
- Already configured - you're using it now
- Has direct access to local repository
- Can commit, run tests, update Jira

#### Claude web (Mobile)
1. Go to claude.ai and create a new Project: "Food Automation"
2. Add CLAUDE.md as project context
3. Reference the GitHub repository URL in project instructions
4. Add custom instructions:
   ```
   You are working on the Food Automation project.
   Always create git patches instead of editing files directly.
   Reference the active Jira task (FA-X) in all work.
   See CLAUDE.md for project context and workflow details.
   ```

### 3. Jira Integration

- **Project**: Food Automation (FA)
- **Workspace**: natsirtguy.atlassian.net
- Always reference task keys (FA-X) in commits and patches

## Working with Claude Code (Desktop)

### Standard Workflow

1. **Check Jira** for next task to work on
2. **Pull latest changes** from GitHub
3. **Work on the task** using Claude Code
4. **Run checks**: `hatch run check` (format, lint, typecheck, test)
5. **Commit changes** with Jira task reference
6. **Push to GitHub**
7. **Update Jira** task status

### Example Session

```bash
# Pull latest
git pull

# Work with Claude Code
# "Let's work on FA-3: Research and configure AI vision services"

# Run quality checks
hatch run check

# Commit (Claude Code will help with this)
git commit -m "[FA-3] Add OpenAI and Anthropic API configuration"

# Push
git push

# Update Jira status (Claude Code can do this)
```

## Working with Claude Web (Mobile)

For complete mobile development instructions including Termux setup, patch workflow, and testing, see **[MOBILE.md](MOBILE.md)**.

**Quick Reference:**
- Claude web creates git patches instead of editing files directly
- Download patches and apply them using Termux on your mobile device
- One command applies patch and creates PR automatically
- See MOBILE.md for full setup and usage guide

## Coordination Between Environments

### Jira as Source of Truth

- Check Jira to see current task status
- Use Jira comments to communicate context between sessions
- Update Jira status after completing work in either environment

### GitHub as Sync Mechanism

- Always pull before starting work
- Push frequently to keep mobile and desktop in sync
- Patches are committed to the repo for later application

### Example Multi-Session Flow

**Session 1 (Desktop - Claude Code)**:
1. Start FA-3 in Jira
2. Create basic project structure
3. Commit and push
4. Add Jira comment: "Basic structure complete, need to add API clients"
5. Update Jira to "In Progress"

**Session 2 (Mobile - Claude web)**:
1. Check Jira, see FA-3 needs API clients
2. Review code on GitHub
3. Ask Claude to generate patch and save to outputs
4. Download patch file from Claude's link
5. Run Termux command to apply patch and create PR
6. Add Jira comment: "Created PR via Termux - link: [PR URL]"

**Session 3 (Desktop - Claude Code)**:
1. Check GitHub for PR created from Termux
2. Review changes in PR
3. Run tests if needed: `hatch run check`
4. Merge PR when ready
5. Update Jira to "Done"

## Tips and Best Practices

### For Claude Code Sessions
- Always run `hatch run check` before committing
- Keep commits focused and reference Jira tasks
- Update Jira status as you progress
- Push frequently so mobile sessions have latest code
- **Mark Jira tasks Done** only after code is pushed to GitHub (for coding tasks)

### For Claude Web Sessions
- See **[MOBILE.md](MOBILE.md)** for complete patch workflow instructions
- Always configure git credentials first (see MOBILE.md)
- **Install hatch using pipx to test patches**:
  ```bash
  pipx install hatch
  ```
- Test all changes with `hatch run check` before creating patches
- Create patch files saved to `/mnt/user-data/outputs/` for download
- Pull real code and generate actual patches, not guess content
- Provide ready-to-run Termux command with the patch
- **Do NOT mark Jira coding tasks as Done** - only Claude Code/user can do this after merging PR

### General
- Pull before every work session
- Use descriptive commit messages with [FA-X] prefix
- Keep Jira updated so both environments stay coordinated
- Save patches in a consistent location for easy retrieval

### Jira Task Completion Policy

**For Coding Tasks:**
- ✅ Only mark as "Done" **after code is pushed to GitHub**
- ✅ Claude Code or user marks tasks Done (not Claude web)
- ✅ Claude web can update status to "In Progress" or add comments
- ❌ Claude web should NOT mark coding tasks as "Done"

**Rationale**: Tasks should only be marked Done when the code is in the repository, not just when a patch exists. Since Claude web cannot push to GitHub, it cannot mark coding tasks complete.

**User Override**: The user can override this and mark tasks Done manually at any time if they choose.

**Non-Coding Tasks**: Research, documentation, or planning tasks can be marked Done without requiring a git push.

### Documentation and Serena Memory Updates

**IMPORTANT**: Only update documentation and Serena memory files **after completing a Jira task unit of work**, not during ongoing development.

#### When to Update

Update documentation/memory when:
- ✅ A Jira task (FA-X) is fully completed and tested
- ✅ Significant architectural changes have been implemented
- ✅ New modules, patterns, or conventions are established
- ✅ Project structure or tech stack changes

Do NOT update for:
- ❌ Work in progress on a task
- ❌ Minor bug fixes or tweaks
- ❌ Experimental code that might be reverted
- ❌ Partial implementations

#### What to Update

After completing a Jira task:

**Documentation Files** (if relevant):
- `README.md` - If setup instructions or usage changed
- `CLAUDE.md` - If project context or workflow changed
- `requirements.md` / `implementation-guide.md` - If requirements evolved

**Serena Memory Files** (use `write_memory` tool):
- `project_overview` - If project scope or phases changed
- `tech_stack` - If new dependencies or tools added
- `code_style_and_conventions` - If new patterns established
- `suggested_commands` - If new commands or workflows added
- `task_completion_checklist` - If completion process changed
- `codebase_structure` - If new modules or reorganization happened

#### How to Update

```bash
# After completing FA-X task and before marking it Done:

# 1. Review what changed
git log --oneline -5

# 2. Update relevant documentation files (if needed)
# Edit README.md, CLAUDE.md, etc.

# 3. Update Serena memories via Claude Code
# Ask: "Update Serena memory for [topic] based on changes in FA-X"

# 4. Commit documentation updates
git add .
git commit -m "[FA-X] Update documentation and Serena memories"
git push

# 5. Mark Jira task as Done
```

**Rationale**: Keeping documentation and memory updates tied to Jira tasks ensures they reflect stable, tested changes rather than work-in-progress, making the project easier to understand and maintain.

## Troubleshooting

### Patch Won't Apply
- Check if files have changed since patch was created
- Manually apply the changes using the patch as a guide
- Update the patch or create a new one

### Conflicts Between Sessions
- Always pull first
- Use Jira comments to coordinate
- When in doubt, create an issue in Jira to discuss

### Lost Context
- Check Jira task description and comments
- Review recent commits on GitHub
- Read CLAUDE.md for project overview
- Check requirements.md and implementation-guide.md
