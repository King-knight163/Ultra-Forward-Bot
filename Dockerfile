FROM python:3.11-slim-bookworm

# Update system packages
RUN apt update && apt upgrade -y
RUN apt install git -y

# Copy and install Python requirements
COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

# Create working directory
RUN mkdir /fwdbot
WORKDIR /fwdbot

# ⭐ यह line add करें - Main Fix
COPY . /fwdbot/

# Start the bot
CMD ["python3", "bot.py"]
