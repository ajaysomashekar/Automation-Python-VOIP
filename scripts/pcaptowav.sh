FILE=$1
#ssrc=$(sudo tshark -n -r pcmu.pcap -R rtp -T fields -e rtp.ssrc -Eseparator=, | sort -u)
ssrc=$(tshark -n -r $FILE -d udp.port==6009,rtp -R rtp -T fields -e rtp.ssrc -Eseparator=, | sort -u)

echo $ssrc
set `echo $ssrc`
ssrc=$1

echo $ssrc
#exit 0
sudo rm payloads
sudo touch payloads 
sudo chmod 777 payloads
#sudo tshark -n -r pcmu.pcap -R rtp -R "rtp.ssrc == $ssrc" -T fields -e rtp.payload | tee payloads
tshark -n -r $FILE -d udp.port==6009,rtp -R rtp -R "rtp.ssrc == $ssrc" -T fields -e rtp.payload | sudo tee payloads

sudo rm sound.raw
sudo touch sound.raw
sudo chmod 777 sound.raw
#for payload in `cat payloads`; do IFS=:; for byte in $payload; do tbyte="\x${byte}" printf "$byte" >> sound.raw; done; done
for payload in `cat payloads`; 
do
IFS=:; 
	for byte in $payload; 
	do 
		printf "\\$(printf "%o" 0x$byte)" >> sound.raw;
		#tbyte="\x${byte}" ; printf "$byte" | hex2binary >> sound.raw; 
	done;
done

echo 'sox has converted pcap to wav file'
sudo sox -t raw -r 16000 -c 1 -U sound.raw capture3D.wav

sudo mv capture3D.wav /root/testing/automation/sounds/
