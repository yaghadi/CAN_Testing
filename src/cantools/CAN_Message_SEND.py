import can 
import cantools
import cantools.database
import time

PortUSB="kvaser"
CANchannel =0
AMOUNT_OF_CAN =1000


CANDBC_PATH = r"C:\Users\PurplE\Documents\DBC\Sample_DBC.dbc"

def portwithchannel(PortUSB,CANchannel):
    return can.interface.Bus(channel=CANchannel,interface=PortUSB)

def main():
    can_bus =portwithchannel(PortUSB,CANchannel)
    dbc = cantools.database.load_file(CANDBC_PATH)
    ABS_WheelSpeed = can.Message(arbitration_id=0x12C,is_extended_id=False,dlc=8,data=[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01])

    for i in range(AMOUNT_OF_CAN):
        can_bus.send(ABS_WheelSpeed)
        time.sleep(0.20)
        print(f"Sent : {ABS_WheelSpeed}")
        # Add 1 to each element in the data field
        new_data = [(b + i) % 256 for b in ABS_WheelSpeed.data]

        # Update the data field with a bytearray or list
        ABS_WheelSpeed.data = bytearray(new_data)




if __name__=='__main__':
    main()

