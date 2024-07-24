from pymodbus.client import ModbusTcpClient

# Modbus TCP server configuration
server_ip = '192.168.4.12'  # Replace with your server's IP address
server_port = 502          # Default Modbus TCP port
esclavo=255
# Create a Modbus TCP client
client = ModbusTcpClient(server_ip, server_port)

def entradas():
    lista=[]
    direcentradas=[4,5,6,7,8,9,10,11]
    connection_result = client.connect()
    if connection_result:
        print("Modbus device is reachable.")
        try:
            for i in direcentradas:
                response=client.read_holding_registers(i,1,esclavo)
                entrada = format(response.registers[0])
                lista.append(entrada)
            print(lista)  
        except Exception as e:
            print(f"Error leyendo: {e}")
    else:
        print("Modbus device is not reachable.")
entradas()