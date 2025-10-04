# Patches Directory

This directory contains git patches created during mobile development sessions using Claude web.

## Structure

- `patches/` - Unapplied patches waiting to be reviewed and applied
- `patches/applied/` - Archive of patches that have been applied and committed

## Naming Convention

Patches should be named: `YYYY-MM-DD-fa-X-brief-description.patch`

Example: `2025-10-04-fa-3-openai-config.patch`

## Usage

### Creating a Patch (Claude Web)

When working via Claude web, ask it to generate a patch:

```
I'm working on FA-X. Create a patch for [change description].
```

Save the patch content to a file in this directory and commit via GitHub web interface.

### Applying a Patch (Claude Code / Desktop)

```bash
# Review the patch
cat patches/YYYY-MM-DD-fa-X-description.patch

# Apply it
git apply patches/YYYY-MM-DD-fa-X-description.patch

# Review changes
git diff

# If good, commit the changes
git add .
git commit -m "[FA-X] Apply patch: Brief description"

# Run tests
hatch run check

# Push
git push

# Archive the patch
git mv patches/YYYY-MM-DD-fa-X-description.patch patches/applied/
git commit -m "Archive applied patch FA-X"
git push
```

## Tips

- Always test patches with `hatch run check` after applying
- If a patch doesn't apply cleanly, use it as a guide for manual changes
- Keep patches small and focused on a single change
- Include the Jira task key (FA-X) in patch names and descriptions

See [WORKFLOW.md](../WORKFLOW.md) for complete workflow documentation.
