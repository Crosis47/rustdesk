# LeeHollow RustDesk Client

LeeHollow RustDesk Client is an AGPLv3 fork of [RustDesk](https://github.com/rustdesk/rustdesk).

It builds RustDesk client binaries that bundle LeeHollow's self-hosted RustDesk ID/relay server configuration. The bundled configuration is imported into RustDesk's normal stored server options so non-technical users do not have to configure these values manually.

This project is not affiliated with, sponsored by, or endorsed by the upstream RustDesk project.

Windows builds are intended to be code-signed through the SignPath Foundation program after project approval.

## Purpose

This fork exists to provide transparent, preconfigured RustDesk client builds for legitimate remote support with user consent.

The intended fork-specific changes are limited to bundling LeeHollow's self-hosted RustDesk server configuration and importing it through RustDesk's normal configuration storage. This fork does not add advertising, analytics, hidden telemetry, or unrelated remote-control functionality.

## Downloads

Windows builds will be published through this repository's GitHub Releases page:

[https://github.com/Crosis47/rustdesk/releases](https://github.com/Crosis47/rustdesk/releases)

See [DOWNLOADS.md](DOWNLOADS.md) for the download policy.

## Code signing policy

See [CODE_SIGNING_POLICY.md](CODE_SIGNING_POLICY.md) for this project's Code signing policy, including SignPath Foundation signing scope, team roles, privacy policy links, and release approval rules.

Free code signing provided by [SignPath.io](https://about.signpath.io), certificate by [SignPath Foundation](https://signpath.org).

## Privacy and Security

- [Privacy Policy](PRIVACY.md)
- [Security Policy](SECURITY.md)
- [Fork Notice](FORK-NOTICE.md)
- [Installation and Uninstallation](INSTALLATION.md)

## Bundled Configuration

Windows Flutter builds run [.github/scripts/prepare-rustdesk-selfhost-config.py](.github/scripts/prepare-rustdesk-selfhost-config.py) during GitHub Actions builds.

The script does not modify RustDesk's upstream default server constants. Instead, it writes bundled `LeeHollowRustDesk.toml` and `LeeHollowRustDesk2.toml` files into the Windows app folder. On first launch, if no custom server is already configured, the client imports those values into RustDesk's normal stored options.

The workflow reads configuration from GitHub Actions secrets:

- `RUSTDESK_ID_SERVER`
- `RUSTDESK_RELAY_SERVER` (optional)
- `RUSTDESK_API_SERVER` (optional)
- `RUSTDESK_PUBLIC_KEY`

The server values are supplied as secrets because these clients connect to LeeHollow's privately operated self-hosted RustDesk infrastructure, and the maintainer does not want the server address exposed in repository configuration or CI logs. This is not a concealment mechanism for client behavior: released clients intentionally bundle the server configuration, and those values may be inspectable from distributed artifacts.

Do not hardcode LeeHollow's RustDesk hostname or public key into the repository or print the generated configuration in build logs.

The manual test workflow is available at [.github/workflows/leehollow-build-test.yml](.github/workflows/leehollow-build-test.yml).

## Upstream Attribution

RustDesk is developed by the upstream RustDesk project:

[https://github.com/rustdesk/rustdesk](https://github.com/rustdesk/rustdesk)

This repository is a downstream fork. The AGPLv3 license and upstream attribution are retained.

For general RustDesk source, architecture, and build documentation, refer to the upstream RustDesk project.
