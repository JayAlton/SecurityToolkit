#!/bin/bash

#-------------------------
# INSTALL SNIFFER SERVICE
# ------------------------

# Define variables
SERVICE_NAME="sniffer.service"
SERVICE_FILE="systemd/sniffer.service"
TARGET_PATH="/etc/systemd/system/$SERVICE_NAME"
REPO_PATH="$(pwd)"

# Confirm the service file exists
if [ ! -f "$SERVICE_FILE" ]; then
	echo "Service file not found at $SERVICE_FILE"
	exit 1
fi

# Ask for email to use in alerts
read -p "Enter email address for alerts: " EMAIL

# Create a temp copy of the service file with modified values
TEMP_FILE="/tmp/$SERVICE_NAME"

sed "s|your@email.com|$EMAIL|g" "$SERVICE_FILE" | \
sed "s|/opt/security-toolkit|$REPO_PATH|g" > "$TEMP_FILE"

# Copy the modified service file
sudo cp "$TEMP_FILE" "$TARGET_PATH"


# Pre-create log files
sudo touch /var/log/sniffer.log /var/log/sniffer.err
sudo chmod 644 /var/log/sniffer.*

# Reload and enable
sudo systemctl daemon-reexec
sudo systemctl enable sniffer
sudo systemctl restart sniffer

# Final check
echo "Sniffer service installed and running."
sudo systemctl status sniffer --no-pager
