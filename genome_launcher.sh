#!/bin/bash
# genome_launcher.sh - Termux/Unix launcher for human genome JS project
# Usage: bash genome_launcher.sh [args]

# Ensure Node.js is installed
if ! command -v node &> /dev/null; then
  echo "Node.js is required. Install with: pkg install nodejs"
  exit 1
fi

# Launch the JavaScript file
node human_genome.js "$@"

# Reference: For Ruby version, see genome.rb or install as a gem if available.
# gem install genome (if published)
