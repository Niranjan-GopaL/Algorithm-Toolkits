import random


class SimulatedChannel:
    ''' A simulated channel that is used by both sender and reciever '''



    def __init__(self, loss_rate=0.3):
        self.loss_rate = loss_rate
        self.packet = None

    def send(self, packet):
        '''  Channel through which sender sends '''

        if random.random() >= self.loss_rate:
            self.packet = packet
        else:
            self.packet = None

    def receive(self):
        '''  Channel through which reciever sends '''

        if random.random() >= self.loss_rate:
            return self.packet
        return None



class RDTSender:
    def __init__(self, channel):
        self.channel = channel
        self.seq_num = 0


    def rdt_send(self, data, receiver):
        '''
        Send data through the channel.
            -> The data should be a string.
        '''

        packet = self.make_packet(data)

        self.send_packet(packet)

        print(f'\n\n\n\n\n\n\n\nSender side --------------------------\n')
        print(f"Sending  {data} with sequence number {packet['seq_number']}")

        ack = None
        while ack != packet['seq_number']:
            ack = receiver.rdt_receive(packet['seq_number'])

            if (not ack) or (ack != packet['seq_number']):
                self.send_packet(packet)
                print(f'\n\nSender side --------------------------\n')
                print(f"Received ACK {ack}.\nRetransmitting {data} with sequence number {packet['seq_number']}")
            else:
                print(f'\n\nSender side --------------------------\n')
                print(f"Received ACK {ack}.\nTransmission successful")


    def send_packet(self, packet):
        '''
        Send a packet by sending it through the channel.
            -> The packet should be a tuple (seq_num, data) where
               seq_num is the sequence number and data is the data.
            -> The sequence number is toggled before sending.
        '''

        self.channel.send(packet)


    def make_packet(self, data):
        '''
        Make a packet by adding the sequence number to the data and 
        return the packet as a dictionary.
        '''

        # this is to toggle seguence number 
        self.seq_num ^= 1  
        pckt = {
                "seq_number" : self.seq_num,
                "data" : data,
                }   
        return pckt



class RDTReceiver:
    def __init__(self, channel):
        self.channel = channel

    def rdt_receive(self, expected_seq_num):
        ''' Recieves the packet through the channel. '''


        print(f'\n\n\nReciever side --------------------------\n')


        packet = self.receive_packet()
        if not packet :
            print("Transfer unsuccessful")
            return expected_seq_num ^ 1
        
        seq_num = packet["seq_number"]
        data = packet["data"]

        if seq_num == expected_seq_num:
            print(f"Received {data} with sequence number {seq_num}")
            self.send_acknowledgement(seq_num)
            return seq_num
        else:
            print(f"Discarded {data} with sequence number {seq_num}. Sending ACK {1 - expected_seq_num}")
            self.send_acknowledgement( expected_seq_num ^ 1)
            return expected_seq_num ^ 1



    def receive_packet(self):
        ''' Receive a packet through the channel.'''
        return self.channel.receive()



    def send_acknowledgement(self, seq_num):
        print(f"Sending ACK {seq_num}")
        self.channel.send(seq_num)






channel = SimulatedChannel(loss_rate=0.3)
sender = RDTSender(channel)
receiver = RDTReceiver(channel)

with open('./test_rdt.txt', 'r') as file:
    data = file.readlines()

print(f'\n\n\n\n\n\n------------------ START OF TRANSMISSION -----------------------------------------------------\n\n\n\n')
# sending each line to reciever
for line in data:
    cleaned_line = line.strip()
    sender.rdt_send(cleaned_line, receiver)


print(f'\n\n\n\n\n\n------------------ END OF TRANSMISSION ----------------------------------------------\n\n\n\n')