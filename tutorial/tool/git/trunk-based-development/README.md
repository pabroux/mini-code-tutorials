# Trunk-Based Development

This tutorial shows the Trunk-Based Git workflow where everyone commits to a single long-lived branch, using feature flags and short-lived PRs to ship continuously without breaking production.

## What?

Trunk-based development replaces long-lived feature branches with a single branch — `main` — that is always deployable.
Features are broken into small sub-parts, merged frequently, and hidden behind feature flags until ready for users.
Releases are business decisions marked with a semver tag, not deployment events.

## How it works?

### 1. Work on `main`, always

There is one long-lived branch: `main`. No `develop`, no `release/x.y` like with GitFlow. 
Every developer branches off main, works for hours to a few days maximum, then opens a Pull Request (PR) back to main.

### 2. Break features into sub-parts

A PR is not a full feature — it's a vertical slice of one.
A new feature becomes: data layer, business logic, API surface, frontend wiring.
Each slice is independently mergeable without breaking anything. If it can't be merged safely yet, it goes behind a flag.

### 3. Gate unfinished work with feature flags

Any code that isn't ready for normal users is wrapped in a flag. Two common strategies:

- **Dedicated environment:** a staging-like app where the flag is permanently *ON*, used by stakeholders for validation.
- **Special accounts in prod:** the flag is *ON* only for specific user IDs or roles, so stakeholders validate against real infrastructure.

The flag is *OFF* by default for everyone else.

### 4. Merge to main = CI/CD triggers

Every merge to `main` triggers the full CI/CD pipeline: tests, build, deploy. `main` is always in production.
This is continuous delivery — there is no manual deploy step, no release branch to cut, no merge freeze.

### 5. Validate with stakeholders, then tag a release

When the team and stakeholders agree that everything behind flags is ready, you tag the commit:

```zsh
git tag v1.4.0
git push origin v1.4.0
```

This is a purely informational marker. Nothing changes in prod — that code has been running continuously. The tag just says: "*we collectively agreed this snapshot is v1.4.0.*"

### 6. Gradually enable the flag, then remove it

After the release tag, you progressively turn the flag `ON` for real users — 5%, 50%, 100%. The flag is your rollback mechanism.
Once the rollback window is closed and the feature is stable, you open a cleanup PR that removes the flag and all its conditionals entirely.
The feature is now permanently part of the app.

> [!NOTE] Gradual rollout is optional but common
> The minimal path is just: flag *ON* → monitor → remove flag. 
