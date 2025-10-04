# Development Workflow

This document describes the hybrid development workflow for the Food Automation project, allowing development from both desktop (Claude Code) and mobile (Claude web).

## Overview

The project uses a **dual-environment workflow**:
- **Desktop**: Claude Code CLI for full development capabilities
- **Mobile**: Claude web (claude.ai) for code review and patch generation

All work is tracked in **Jira** (project key: FA) and synchronized via **GitHub**.

## Setup

### 1. GitHub Repository

Create a public GitHub repository:

```bash
# Create repo on GitHub, then:
git remote add origin https://github.com/<username>/food-automation.git
git branch -M main
git push -u origin main
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

### Patch-Based Workflow

When using Claude web, you **cannot edit files directly**. Instead, create patches that can be applied later.

### Creating Patches

Ask Claude to generate a patch for your changes:

```
I'm working on FA-X. Please create a patch that [describes the change].
Generate a git patch file I can save and apply later.
```

Claude should respond with a patch in this format:

```patch
From: Claude <noreply@anthropic.com>
Date: 2025-10-04
Subject: [FA-3] Add OpenAI client configuration

Add configuration for OpenAI API client including environment
variable handling and basic error handling.

---
diff --git a/src/food_automation/config.py b/src/food_automation/config.py
new file mode 100644
index 0000000..1234567
--- /dev/null
+++ b/src/food_automation/config.py
@@ -0,0 +1,15 @@
+"""Configuration management."""
+
+import os
+
+def get_openai_api_key() -> str:
+    """Get OpenAI API key from environment."""
+    key = os.getenv("OPENAI_API_KEY")
+    if not key:
+        raise ValueError("OPENAI_API_KEY not set")
+    return key
```

### Saving Patches

1. Copy the patch content from Claude's response
2. Save locally on your device (Notes app, files, email to yourself, etc.)
3. Suggested naming: `YYYY-MM-DD-fa-X-description.patch`
4. Add a Jira comment noting that a patch is ready to apply

### Applying Patches (Back on Desktop)

When you return to your computer:

```bash
# Pull latest changes
git pull

# Save the patch to a file (copy from where you saved it)
# For example, create a temporary patch file:
cat > /tmp/fa-3-patch.patch
# Paste the patch content, then Ctrl+D

# Review the patch
cat /tmp/fa-3-patch.patch

# Apply the patch
git apply /tmp/fa-3-patch.patch

# Review changes
git diff

# If good, commit
git add .
git commit -m "[FA-3] Apply patch: Add OpenAI client configuration"

# Run checks
hatch run check

# Fix any issues, then push
git push

# Clean up temporary file
rm /tmp/fa-3-patch.patch
```

**Tip**: You can also save the patch directly to a file on your computer and use `git apply <path-to-patch-file>`.

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
3. Ask Claude to generate patch for OpenAI client
4. Copy patch and save locally (Notes app, email, etc.)
5. Add Jira comment: "Created patch for OpenAI client - ready to apply when back at computer"

**Session 3 (Desktop - Claude Code)**:
1. Pull latest changes from GitHub
2. Check Jira, see patch is ready
3. Retrieve patch from where you saved it (Notes, email, etc.)
4. Apply patch using `git apply`
5. Run tests: `hatch run check`
6. Fix any issues if needed
7. Commit and push
8. Update Jira to "Done"

## Tips and Best Practices

### For Claude Code Sessions
- Always run `hatch run check` before committing
- Keep commits focused and reference Jira tasks
- Update Jira status as you progress
- Push frequently so mobile sessions have latest code
- **Mark Jira tasks Done** only after code is pushed to GitHub (for coding tasks)

### For Claude Web Sessions
- Always create patches, never attempt to edit files
- Include detailed explanations in patches
- Reference the specific Jira task
- Note in Jira that a patch is ready to apply (include where you saved it)
- Review the code on GitHub before suggesting changes
- Save patches somewhere you can easily retrieve them later
- **Do NOT mark Jira coding tasks as Done** - only Claude Code/user can do this after pushing to GitHub

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
