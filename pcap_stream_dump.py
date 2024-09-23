from scapy.all import rdpcap, IP, TCP, UDP, Raw
from collections import defaultdict

# Function to extract streams and concatenate packet payloads
def extract_streams(packets):
    tcp_streams = defaultdict(list)
    udp_streams = defaultdict(list)

    # Loop through packets
    for packet in packets:
        if IP in packet:
            # TCP stream extraction
            if TCP in packet:
                stream_id = (packet[IP].src, packet[IP].dst, packet[TCP].sport, packet[TCP].dport)
                if Raw in packet:
                    tcp_streams[stream_id].append(packet[Raw].load)
            # UDP stream extraction
            elif UDP in packet:
                stream_id = (packet[IP].src, packet[IP].dst, packet[UDP].sport, packet[UDP].dport)
                if Raw in packet:
                    udp_streams[stream_id].append(packet[Raw].load)

    return tcp_streams, udp_streams

# Function to write concatenated streams to a file
def write_streams_to_file(tcp_streams, udp_streams, filename='packet_streams.txt'):
    with open(filename, 'w') as file:
        # Write TCP streams
        file.write("TCP Streams:\n")
        for stream_id, packets in tcp_streams.items():
            file.write(f"Stream {stream_id}:\n")
            stream_data = b''.join(packets)  # Concatenate all payloads into a single bytes object
            try:
                file.write(stream_data.decode('ascii', errors='ignore') + "\n")
            except Exception as e:
                file.write("[Non-ASCII data]\n")
            file.write("="*50 + "\n")

        # Write UDP streams
        file.write("\nUDP Streams:\n")
        for stream_id, packets in udp_streams.items():
            file.write(f"Stream {stream_id}:\n")
            stream_data = b''.join(packets)  # Concatenate all payloads into a single bytes object
            try:
                file.write(stream_data.decode('ascii', errors='ignore') + "\n")
            except Exception as e:
                file.write("[Non-ASCII data]\n")
            file.write("="*50 + "\n")

# Load packets from a PCAP file
packets = rdpcap('capture.pcap')  # Replace with your file

# Extract streams
tcp_streams, udp_streams = extract_streams(packets)

# Write the streams to a text file
write_streams_to_file(tcp_streams, udp_streams)

print("Streams have been concatenated and written to packet_streams.txt")
