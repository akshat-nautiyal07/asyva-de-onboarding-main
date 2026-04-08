# 09 Git (Basics for Working in ASYVA Repos)

## Objective
Become comfortable with day-to-day Git workflows used in real delivery:
- cloning repos, branching, committing, pushing
- opening PRs, responding to review comments
- resolving simple merge conflicts
- writing good commit messages

## Assignment

### A) Setup
1. Install Git
2. Configure your identity:
   - `git config --global user.name "Your Name"`
   - `git config --global user.email "your.email@domain.com"`

### B) Core workflow (daily)
1. Clone the repo
2. Create a feature branch
3. Make changes
4. Commit with a clean message
5. Push branch
6. Open a Pull Request (PR)
7. Address review comments
8. Merge (mentor will merge for bootcamp)

### C) Required commands (must practice)
- `git clone <url>`
- `git status`
- `git branch`
- `git checkout -b <branch>`
- `git add -A`
- `git commit -m "message"`
- `git push -u origin <branch>`
- `git pull --rebase`
- `git log --oneline --decorate --graph --all`
- `git diff`
- `git stash` (basic)
- `git fetch`
- `git rebase` (basic concept)
- `git revert` (concept)
- `git reset` (only concept + safe usage explained by mentor)

### D) Practice tasks (hands-on)
1. **Branching**
   - Create branch: `day-01-foundations`
   - Add a small change in `00_foundations/architecture.md`
   - Commit + push
2. **PR**
   - Open a PR with a short description of what changed
3. **Review cycle**
   - Mentor leaves 2 comments; you respond and push updates
4. **Conflict simulation**
   - Mentor updates the same line; you pull and resolve conflict
   - Push the resolved version

## Expected outputs (acceptance criteria)
- A PR exists for at least 3 days of work (Day 1, Day 2, Day 3)
- Commit messages follow this pattern:
  - `day-02: add join + group by practice queries`
- Can resolve a simple merge conflict confidently
- Can explain (in 1 minute):
  - what a branch is
  - what a PR is
  - what merge conflict means

## Mentor review checklist
- Uses branches (does not commit to main directly)
- Commits are small and meaningful
- PR description is clear
- Can resolve conflict without panic

## Learning links (legit)
- Git official book (free): https://git-scm.com/book/en/v2
  - Read: 1 (Getting Started), 2 (Git Basics), 3.1 (Branches in a Nutshell), 3.2 (Basic Branching/Merging)
- Atlassian Git tutorials (very practical):
  - https://www.atlassian.com/git/tutorials
- YouTube (short + practical): Git & GitHub crash course (Traversy Media)
  - https://www.youtube.com/watch?v=SWYqp7iY_Tc
