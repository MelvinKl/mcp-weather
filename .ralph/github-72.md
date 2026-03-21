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
- [x] 2. Verify removal of .beads directory and any beads-related artifacts
  - Acceptance Criteria:
    - No .beads directory exists in the repository
    - No beads-related files or directories remain in the file system
- [x] 3. Verify removal of Agents.md and similar agent documentation files
  - Acceptance Criteria:
    - No agents.md or AGENTS.md file exists in the repository
    - No agent documentation files remain
  - Details from Step 2: Verification confirmed no agents.md or AGENTS.md files exist in repository root or subdirectories
- [ ] 4. Verify removal of opencode.json and any LLM tool configuration files
  - Acceptance Criteria:
    - No opencode.json or similar LLM tool configuration files exist
    - No .ai/, .claude/, or other LLM tool directories remain
    - No LLM-generated artifacts (e.g., conversation history, session files) remain
  - Details from Step 2: Repository root directory contains no opencode.json, .ai/, .claude/, or LLM tool directories; all LLM artifacts confirmed removed
  - Details from Step 3: Comprehensive search methodology (checking both repository root and all subdirectories) used for agents.md verification confirms thorough artifact removal verification approach
- [ ] 5. Verify that make test succeeds
  - Acceptance Criteria:
    - `make test` command executes without errors
    - All tests pass and exit successfully
  - Details from Step 2: Makefile exists at /root/git/managed/mcp-weather/Makefile; test command runs pytest with coverage, flake8 linting, and black formatting; coverage files (.coverage, coverage.xml, htmlcov/) already present from previous runs
  - Details from Step 3: Systematic verification from Step 3 confirms all agent documentation files removed, providing confidence repository is clean before running test suite