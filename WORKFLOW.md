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

1. Copy the patch content
2. Save to a file: `patches/YYYY-MM-DD-fa-X-description.patch`
3. Commit the patch file to the repo (via GitHub web interface or next Claude Code session)

### Applying Patches (Back on Desktop)

When you return to your computer:

```bash
# Pull latest (including any new patch files)
git pull

# Review the patch
cat patches/2025-10-04-fa-3-openai-config.patch

# Apply the patch
git apply patches/2025-10-04-fa-3-openai-config.patch

# Review changes
git diff

# If good, commit
git add .
git commit -m "[FA-3] Apply patch: Add OpenAI client configuration"

# Run checks
hatch run check

# Fix any issues, then push
git push

# Archive the applied patch
mkdir -p patches/applied
git mv patches/2025-10-04-fa-3-openai-config.patch patches/applied/
git commit -m "Archive applied patch FA-3"
git push
```

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
3. Generate patch for OpenAI client
4. Save patch, commit patch file via GitHub web UI
5. Add Jira comment: "Created patch for OpenAI client - needs testing"

**Session 3 (Desktop - Claude Code)**:
1. Pull latest (gets patch file)
2. Review and apply patch
3. Run tests: `hatch run test`
4. Fix any issues
5. Commit, push
6. Update Jira to "Done"
7. Archive patch file

## Tips and Best Practices

### For Claude Code Sessions
- Always run `hatch run check` before committing
- Keep commits focused and reference Jira tasks
- Update Jira status as you progress
- Push frequently so mobile sessions have latest code

### For Claude Web Sessions
- Always create patches, never attempt to edit files
- Include detailed explanations in patches
- Reference the specific Jira task
- Note in Jira that a patch is waiting to be applied
- Review the code on GitHub before suggesting changes

### General
- Pull before every work session
- Use descriptive commit messages with [FA-X] prefix
- Keep Jira updated so both environments stay coordinated
- Archive patches after applying to keep repo clean

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
