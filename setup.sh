#!/bin/bash

# Install Node.js if not already installed
if ! command -v node &> /dev/null; then
    echo "Installing Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

# Install global dependencies
echo "Installing global dependencies..."
sudo npm install -g @slidev/cli

# Install project dependencies
echo "Installing project dependencies..."
npm install

# Install Playwright browsers
echo "Installing Playwright browsers..."
npx playwright install chromium

echo "Setup complete!" 