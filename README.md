# LeeHollow RustDesk Client

LeeHollow RustDesk Client is an AGPLv3 fork of [RustDesk](https://github.com/rustdesk/rustdesk).

It builds RustDesk client binaries preconfigured for LeeHollow's self-hosted RustDesk ID/relay server. The build-time configuration sets the default ID server, relay server, and public key so non-technical users do not have to configure these values manually.

This project is not affiliated with, sponsored by, or endorsed by the upstream RustDesk project.

Windows builds are intended to be code-signed using a certificate issued through the SignPath Foundation program.

## Purpose

This fork exists to provide transparent, preconfigured RustDesk client builds for legitimate remote support with user consent.

The intended fork-specific changes are limited to build-time configuration for LeeHollow's self-hosted RustDesk infrastructure. This fork does not add advertising, analytics, hidden telemetry, or unrelated remote-control functionality.

## Downloads

Windows builds are published through this repository's GitHub Releases page:

[https://github.com/Crosis47/rustdesk/releases](https://github.com/Crosis47/rustdesk/releases)

See [DOWNLOADS.md](DOWNLOADS.md) for the download policy.

## Privacy and Security

- [Privacy Policy](PRIVACY.md)
- [Security Policy](SECURITY.md)
- [Fork Notice](FORK-NOTICE.md)

## Build-Time Configuration

Windows Flutter builds run [.github/scripts/patch-rustdesk-selfhost.py](.github/scripts/patch-rustdesk-selfhost.py) during GitHub Actions builds.

The workflow reads configuration from repository variables:

- `RUSTDESK_ID_SERVER`
- `RUSTDESK_PUBLIC_KEY`

Do not hardcode LeeHollow's RustDesk hostname or public key into the repository.

The manual test workflow is available at [.github/workflows/leehollow-build-test.yml](.github/workflows/leehollow-build-test.yml).

## Upstream Attribution

RustDesk is developed by the upstream RustDesk project:

[https://github.com/rustdesk/rustdesk](https://github.com/rustdesk/rustdesk)

This repository is a downstream fork. The AGPLv3 license and upstream attribution are retained.

For general RustDesk source, architecture, and build documentation, refer to the upstream RustDesk project.
