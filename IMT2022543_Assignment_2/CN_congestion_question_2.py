''' Implementing Congestion control by following Tahoe's schema '''


import random




class SimulatedChannel:
    def __init__(self, loss_rate=0.01):
        self.loss_rate = loss_rate
        self.packet = None

    def send(self, packet):
        if random.random() >= self.loss_rate:
            self.packet = packet
        else:
            self.packet = None

    def receive(self):
        if random.random() >= self.loss_rate:
            return self.packet


class CongestionControl:
    def __init__(self,channel,packets,ssthresh):
        self.congWin = 1
        self.packet = None
        self.channel = channel
        self.ssthresh = ssthresh 
        self.packetsToSend = packets
        self.packetsSent = 0

    def send_data(self, data):
        self.packet = self.construct_packet(data)

    def send_packet(self):
        self.channel.send(self.packet)
        self.packetsSent += 1

    def construct_packet(self, data):
        pckt =  {
                    'data': data, 
                    'size': len(data)
                }
        return pckt

    def receive_ack(self):
        packet_received = self.channel.receive()
        return packet_received != None


def get_data():
    ''' Whatever data we want to send should be mined from here'''

    
    data = "Stuff we wanna send "
    return data














print(f'\n\n\n\n\n\n------------------ START OF TRANSMISSION -----------------------------------------------------\n\n\n\n')


# adjust the parameters here
channel = SimulatedChannel( loss_rate = 0.02)
control_simulation = CongestionControl(channel, packets = 1000, ssthresh = 16)

print(f"Initial Threshold: {control_simulation.ssthresh} \n\n")


while control_simulation.packetsSent < control_simulation.packetsToSend:

    print("Congestion Window size:", control_simulation.congWin)

    packet = 0
    while packet < control_simulation.congWin:
        data = get_data()
        control_simulation.send_data(data) 
        control_simulation.send_packet()

        # no ack means the packet was lost.
        # so we will decrease the threshold to half of congestion window size we are currently at
        if not control_simulation.receive_ack():
            control_simulation.ssthresh = control_simulation.congWin // 2   
            control_simulation.congWin = 1  
            print(f"\n\nPacket Lost. \nNew Threshold : {control_simulation.ssthresh}\n\n\n")    
            break

        packet += 1

    else:
        # We increase the congWindow size according to AIMD
        # this ternery expression will increase congWin accordingly
        control_simulation.congWin = control_simulation.congWin*2 if (control_simulation.congWin < control_simulation.ssthresh) else control_simulation.congWin + 1  
 

print(f'\n\n\n\n\n\n------------------ END OF TRANSMISSION ----------------------------------------------\n\n\n\n')