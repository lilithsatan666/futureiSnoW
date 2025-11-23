ensure_pkg gem ruby
ensure_pkg git git
# optional build tools
ensure_pkg make make || true
ensure_pkg clang clang || true

# Update RubyGems and installed gems (best-effort)
if command -v gem >/dev/null 2>&1; then
  log "Updating RubyGems system and installed gems (no docs)"
  # try to avoid root; Termux typically allows user installs; --no-document reduces extra output
  set +e
  gem update --system --no-document
  gem update --no-document
  gem cleanup || true
  set -e
else
  log "gem not found; skipping Ruby gem updates."
fi

# Node / npm updates in project
if command -v npm >/dev/null 2>&1; then
  log "Node.js and npm versions:"
  node --version || true
  npm --version || true

  # change to project dir
  if [[ ! -d "$PROJECT_DIR" ]]; then
    echo "Project directory '$PROJECT_DIR' does not exist."
    exit 1
  fi
  pushd "$PROJECT_DIR" >/dev/null

  # initialize package.json if missing
  if [[ ! -f package.json ]]; then
    log "No package.json found in '$PROJECT_DIR' — creating a minimal one (npm init -y)."
    npm init -y
  fi

  log "Installing (or ensuring) local dependencies from package.json"
  npm install --no-audit --no-fund

  log "Listing outdated packages (current -> wanted -> latest):"
  npm outdated || true

  log "Running npm update (updates to latest allowed by semver ranges in package.json)"
  npm update --no-audit --no-fund

  if [[ "$LATEST_FLAG" = true ]]; then
    log "--latest flag set: upgrading dependencies to the latest versions (may be breaking)."
    # use npx so we don't require a global install
    if ! command -v npx >/dev/null 2>&1; then
      log "npx not found, attempting to install npm-check-updates globally"
      npm install -g npm-check-updates --no-audit --no-fund
    fi
    # update package.json to latest versions and install
    npx npm-check-updates -u
    npm install --no-audit --no-fund
  fi

  log "Final installed package summary (top-level):"
  npm ls --depth=0 || true

  popd >/dev/null
