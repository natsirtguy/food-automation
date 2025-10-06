# Mobile Development Guide

This guide covers development from mobile devices using Claude web (claude.ai) with the patch-based Termux workflow.

## Overview

When using Claude web on mobile, you **cannot edit files directly**. Instead, Claude creates git patches that you apply using **Termux** on your mobile device.

**Workflow**: Ask Claude for patch → Download patch → Run Termux command → PR created automatically

## Prerequisites

### Termux Setup (One-Time, 5 minutes)

1. **Install Termux** from F-Droid or Play Store

2. **Grant storage access and install tools**:
   ```bash
   # Grant storage permissions (Android will prompt)
   termux-setup-storage

   # Install git and GitHub CLI
   pkg install git gh

   # Authenticate with GitHub
   gh auth login
   ```

3. **Install pipx and hatch** for running tests:
   ```bash
   # Install Python and pipx
   pkg install python
   pip install pipx
   pipx ensurepath

   # Install hatch (project management tool)
   pipx install hatch
   ```

4. **Clone the repository**:
   ```bash
   git clone https://github.com/natsirtguy/food-automation.git
   cd food-automation
   ```

## Working with Patches

### Requesting a Patch

Ask Claude to generate a patch:

```
I'm working on FA-X. Please create a patch for [describes the change].
Save it to outputs for the Termux workflow.
```

### What Claude Does

1. **Pulls actual code** from GitHub repository
2. **Generates real patch** using git format-patch
3. **Saves patch file** to `/mnt/user-data/outputs/` for download
4. **Provides download link** and ready-to-run Termux command

### What You Get

- **Download link**: Patch file ready to download
- **Termux command**: Complete command to apply patch and create PR

### Applying the Patch

**What you do:**
1. Download the patch file from Claude's link
2. Copy and paste the Termux command
3. Done! PR is created automatically

**Example Termux command:**
```bash
cd ~/food-automation && \
git checkout master && \
git pull && \
git checkout -b FA-X-patch && \
git apply ~/storage/downloads/patch-name.patch && \
git add . && \
git commit -m "[FA-X] Description" && \
git push -u origin FA-X-patch && \
gh pr create --fill
```

### Benefits of This Workflow

- ✅ No clipboard size limits (no copying large patches)
- ✅ One command creates the PR directly  
- ✅ Works entirely on mobile
- ✅ Fast and streamlined

## Testing Changes

After applying a patch, you can test it in Termux:

```bash
# Navigate to project
cd ~/food-automation

# Run all quality checks and tests
hatch run check

# Or run individual checks
hatch run format   # Format code
hatch run lint     # Lint code
hatch run typecheck # Type check
hatch run test     # Run tests
```

## Claude Web Project Setup

To work effectively with Claude web:

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

## Tips and Best Practices

### For Claude (When Generating Patches)

- **FIRST: Configure git credentials** before any git operations:
  ```bash
  git config user.name "Claude Assistant"
  git config user.email "claude@anthropic.com"
  ```
  The code environment doesn't persist git credentials, so configure them immediately after cloning the repo or initializing git.

- Always create patch files saved to `/mnt/user-data/outputs/` for download
- Claude must pull real code and generate actual patches, not guess content
- Provide ready-to-run Termux command with the patch
- Use master branch as base for patches
- Review the code on GitHub before suggesting changes

### For Developers (Mobile)

- Always pull latest changes before requesting patches
- Download patches to `~/storage/downloads/` (default download location)
- Test patches with `hatch run check` before creating PR
- Note PR link in Jira after creating it via Termux
- **Do NOT mark Jira coding tasks as Done** - only Claude Code or desktop users can do this after merging the PR

### Jira Integration

- Always reference the active Jira task (FA-X) in patch requests
- Claude web can update Jira status to "In Progress" or add comments
- Only mark tasks "Done" after PR is merged (do this from desktop or have someone else do it)

**Rationale**: Tasks should only be marked Done when code is in the repository, not just when a patch exists. Since Claude web cannot push to GitHub, it cannot mark coding tasks complete.

## Example Session

1. **Check Jira** for next task: FA-5 needs API client implementation
2. **Review code** on GitHub to understand current state
3. **Ask Claude web**: "I'm working on FA-5. Create a patch to add the OpenAI API client. Save it to outputs for Termux."
4. **Download patch** from Claude's link to `~/storage/downloads/`
5. **Run Termux command** (copy/paste from Claude's response)
6. **Test in Termux**: `cd ~/food-automation && hatch run check`
7. **Add Jira comment**: "Created PR via Termux - link: [PR URL]"

## Troubleshooting

### Patch Won't Apply
- Check if files have changed since patch was created
- Manually apply the changes using the patch as a guide
- Ask Claude to create a new patch based on current master

### Hatch Not Found
- Ensure pipx is in your PATH: `pipx ensurepath`
- Restart Termux session
- Verify installation: `hatch --version`

### GitHub Authentication Issues
- Re-run `gh auth login` in Termux
- Check that your GitHub token has repo permissions
- Try using SSH instead of HTTPS for git operations

### Files Changed On GitHub
- Always pull before requesting patches
- Use Jira comments to coordinate with desktop sessions
- Ask for a fresh patch based on latest master
