from pymodbus.client import ModbusTcpClient
# Modbus TCP server configuration
server_ip = '192.168.4.12'  # Replace with your server's IP address
server_port = 502          # Default Modbus TCP port
esclavo=255
# Create a Modbus TCP client
client = ModbusTcpClient(server_ip, server_port)
def escribirplc(registro, valor):
    # Connect to the Modbus server with a timeout
    connection_result = client.connect()
    if connection_result:
        print("Modbus device is reachable.")
        # Write to a single holding register
        write_result = client.write_register(registro, valor, esclavo)
        # Check if the write was successful
        if write_result.isError():
            print(f"Write error: {write_result}")
        else:
            print("Write successful.")
    else:
        print("Modbus device is not reachable.")
    # Close the Modbus connection
    client.close()

#El primer relé que apunta a la V1.0
escribirplc(0,0)

#El segundo relé que apunta a la V3.0
escribirplc(1,0)

#El Tercer relé que apunta a la V5.0
escribirplc(2,0)

#El cuarto  relé que apunta a la V7.0
#escribirplc(3,0)