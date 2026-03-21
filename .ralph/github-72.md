# GitHub Issue Task: AI artifacts

Issue Number: 72
Branch: ai/issue-72-ai-artifacts

## Required Task

Remove beads, Agents.md, opencode.json, etc from the repository. Every artifact that can be attributed to either an LLM tool or beads should be removed from the repository

## Steps

- [x] 1. Identify all LLM/beads artifacts in the repository
  - Acceptance Criteria:
    - List created of: .beads directory, agents.md file, and any opencode.json or similar files
    - Verified no other LLM/beads artifacts exist (e.g., no other configuration files from LLM tools)
- [ ] 2. Remove the .beads directory
  - Acceptance Criteria:
    - .beads directory is completely removed from the repository
    - No trace of .beads remains in the file system
  - Note: Step 1 confirmed no .beads directory exists in the repository
- [ ] 3. Remove the agents.md file
  - Acceptance Criteria:
    - agents.md file is deleted from the repository root
    - File no longer appears in git status or file listings
  - Note: Step 1 confirmed no agents.md file exists in the repository
- [ ] 4. Search for and remove any opencode.json or similar LLM tool artifacts
  - Acceptance Criteria:
    - No opencode.json file exists in the repository
    - No other LLM tool configuration files remain (searched for common patterns)
  - Note: Step 1 confirmed no opencode.json or similar LLM tool artifacts exist in the repository
- [ ] 5. Verify that make test succeeds
  - Acceptance Criteria:
    - `make test` command executes without errors
    - All tests pass and exit successfully
  - Note: Step 1 confirmed no LLM/beads artifacts exist, so removal steps may be unnecessary but verification still required