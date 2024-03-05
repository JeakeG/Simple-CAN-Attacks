# Simple CAN Attacks
scripts for simple injections attacks for CAN bus networks

## F Attack
Captures messages on the CAN bus, replaces the data field with 8 bytes of 0xFF, and replays the message back onto the bus

# CAN Interface Setup for Vehicle
sudo ip link set can0 type can bitrate 500000
sudo ip link set up can0
