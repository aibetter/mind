#!/usr/bin/env zx
/* eslint-disable no-undef */

await $`pyinstaller --clean -F -n server-aarch64-apple-darwin --distpath src-tauri/binaries src-backend/main.py`
