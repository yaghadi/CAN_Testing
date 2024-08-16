import can 


PortUSB="kvaser"
CANchannel =0



CANDBC_PATH = r"C:\Users\PurplE\Documents\DBC\Sample_DBC.dbc"

def portwithchannel(PortUSB,CANchannel):
    return can.interface.Bus(channel=CANchannel,interface=PortUSB)

def receive_message(Can_bus):
    while True:
        msg = Can_bus.recv ()
        if msg:
            print(f"Received message :{msg}")


def main():
    try:
        can_bus=portwithchannel(PortUSB,CANchannel)
        print("Connected to CAN Bus")
        receive_message(can_bus)
    except FileNotFoundError:
        print(f"DBC file not found:{CANDBC_PATH}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ =='__main__':
    main()