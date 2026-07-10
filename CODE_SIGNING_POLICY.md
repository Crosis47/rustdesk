# Code signing policy

Free code signing provided by [SignPath.io](https://about.signpath.io), certificate by [SignPath Foundation](https://signpath.org).

This policy applies to Windows release artifacts for LeeHollow RustDesk Client.

## Project Scope

LeeHollow RustDesk Client is a downstream AGPLv3 fork of RustDesk. The fork exists to build transparent, preconfigured RustDesk client binaries for LeeHollow's self-hosted RustDesk ID/relay server.

The intended fork-specific changes are limited to build-time configuration of the default ID server, relay server, and public key, plus fork-specific release, privacy, security, and signing documentation.

This project must not submit upstream RustDesk release binaries, unrelated third-party binaries, or locally modified artifacts for signing as LeeHollow RustDesk Client. Signed release artifacts must be built from source code and build scripts in this repository by the documented GitHub Actions release workflow.

## Team Roles

Committers and reviewers: [Crosis47](https://github.com/Crosis47)

Approvers: [Crosis47](https://github.com/Crosis47)

Each signing request requires manual approval by an approver. Changes from non-committers must be reviewed by a committer or reviewer before merge. Maintainers with repository or SignPath access must use multi-factor authentication.

If additional maintainers are added, this policy must be updated before they approve signing requests.

## Signing Rules

Signed Windows artifacts must use the product name `LeeHollow RustDesk Client` in Windows file metadata, and every product version value in a build must match the release version.

Release artifacts must be traceable to a public commit, tag, or release branch in this repository. Signing requests must not bypass SignPath.io technical controls, source verification, or manual approval.

This project signs only its own release artifacts. Upstream open source components included in a release package must remain traceable to their source and license and must not be represented as fork-owned code.

## Privacy Policy

Privacy policy: [PRIVACY.md](PRIVACY.md)

LeeHollow RustDesk Client does not include advertising, analytics, third-party tracking, hidden telemetry, or unrelated remote-control functionality. Network behavior required for remote support is described in the privacy policy.

## User Safety

LeeHollow RustDesk Client is intended for legitimate remote support with user consent. It is not intended to identify or exploit security vulnerabilities, bypass security controls, or operate as a hidden remote-control tool.

System changes made by installers must be announced by the installer or operating system prompts. Installation and uninstallation instructions are documented in [INSTALLATION.md](INSTALLATION.md).

Security and signing concerns should be reported privately as described in [SECURITY.md](SECURITY.md).
