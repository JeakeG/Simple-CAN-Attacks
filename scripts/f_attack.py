import can

def main():
    with can.Bus(interface="socketcan", channel="can0", recieve_own_messages=False) as bus:
        for msg in bus:
            new_msg = can.Message(arbitration_id=msg.arbitration_id, data=[0xff]*8)
            bus.send(new_msg)

if __name__ == "__main__":
    main()