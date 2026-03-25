# Trunk Based Development (TBD)

This tutorial shows the Trunk Based Git workflow where everyone pushes to a single long-lived branch, using direct commits or short-lived PRs to integrate continuously while keeping the trunk always releasable.

## What?

Trunk Based Development (TBD) replaces long-lived feature branches with a single branch — `main` — that is always deployable.
Features are broken into small sub-parts and integrated frequently. When a change could affect users before it is complete, it can be hidden behind a feature flag (see [Complementary practices](#complementary-practices) below).
Branches, if used, must be short-lived — typically no more than one to two days — and integrated back into the trunk as quickly as possible.
This constraint is central to TBD and prevents integration drift.

> [!IMPORTANT]
> TBD is primarily a **branching strategy** — it defines how code flows into the trunk, not how or when it reaches users. Deployment and release practices (feature flags, gradual rollouts, tagging) are complementary but independent choices.

## How does it work?

#### Work on the *trunk* (usually `main`), always

There is one long-lived branch (called *trunk*), usually named `main`. Unlike [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/), there is no `develop`, no long-lived release branches. Short-lived release branches (stabilization-only, receiving cherry-picked fixes from trunk) are allowed.
Depending on team size, developers either commit straight to `main` or branch off it for a few hours to a couple of days maximum, then open a Pull Request (PR) back to `main`.

> [!NOTE]
> In a small team, each developer can stream small commits straight into the *trunk* after running the build locally (which must pass).

#### Break features into sub-parts

A commit or PR is not a full feature — it's a small, independently mergeable increment.
A new feature might be broken down into: data layer, business logic, API surface, frontend wiring.
Each increment is independently mergeable without breaking anything.
If an increment can't be merged safely yet, common strategies include hiding it behind a feature flag, using branch by abstraction, or breaking it down into even smaller parts.

#### Push to `main` → CI triggered

Every push to `main` triggers the CI pipeline: tests, build, artifact packaging. 

> [!IMPORTANT]
> TBD itself does not prescribe what happens next — deployment is a separate decision. You can layer on Continuous Delivery (every green build is deployable on demand) or Continuous Deployment (every green build auto-deploys), but neither is inherent to TBD. The branching model and the release strategy are independent choices.

## Complementary practices

The practices below are independent and optional — teams can adopt any combination depending on their release process.

#### Gate unfinished work with feature flags

When code that could affect users isn't ready yet, it can be wrapped in a flag. Two common strategies:

- **Dedicated environment:** a staging-like app where the flag is permanently *ON*, used by stakeholders for validation.
- **Special accounts in prod:** the flag is *ON* only for specific user IDs or roles, so stakeholders validate against real infrastructure.

The flag is *OFF* by default for everyone else.

#### Validate with stakeholders, then tag a release

When the team and stakeholders agree that everything behind flags is ready, you can tag the commit:

```zsh
git tag v1.4.0
git push origin v1.4.0
```

This is a marker that says: "*we collectively agreed this snapshot is v1.4.0.*" If you practice Continuous Deployment, nothing new is deployed — that code has already been running in prod (behind flags), so the tag is purely informational. If you practice Continuous Delivery, the tag may be what triggers the actual deployment.

#### Gradually enable the flag, then remove it

After the release tag, you progressively turn the flag `ON` for real users — 5%, 50%, 100%. The flag is your rollback mechanism.
Once the rollback window is closed and the feature is stable, you open a cleanup PR that removes the flag and all its conditionals entirely.
The feature is now permanently part of the app.

> [!NOTE]
> Gradual rollout is optional but common. The minimal path is just: flag *ON* → monitor → remove flag.

## Main differences with GitHub Flow

In practice, TBD and GitHub Flow overlap (both commonly target a deployable `main`). The main difference is usually cadence and how strongly teams optimize for integrating to trunk extremely frequently.

| | TBD | GitHub Flow |
| --- | --- | --- |
| Integration cadence | Very frequent; direct-to-trunk or very short-lived branches | Typically branch-per-change merged via PR into main |
| Unfinished work | Small safe increments, optionally gated by flags or other mechanics | Commonly handled via branch isolation (and optionally feature flags) |
| PRs | Optional or very short-lived; optimized for fast merges | Typically required; size varies (often small, but not inherently per-feature) |

## Resources

- [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) by Vincent Driessen
- [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) by GitHub
- [Trunk Based Development](https://trunkbaseddevelopment.com) by Trunk Based Development
