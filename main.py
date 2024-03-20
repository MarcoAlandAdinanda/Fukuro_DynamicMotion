from fukuro_dynamic import Fukuro_Dynamic

bola = "MESSAGE DARI ROS"

koordinat_omni = [] # INPUT DARI ROS MESSAGE
koordinat_sekarang = [] # INPUT DARI ROS MESSAGE
koordinat_bola = [] # INPUT DARI ROS MESSAGE

dribble = True # INPUT DARI ROS MESSAGE

koordinat_attack_zone1 = [1975, 900] # CONTOH KOORDINAT TARGET
koordinat_attack_zone2 = [1975, 700] # CONTOH KOORDINAT TARGET
koordinat_attack_zone3 = [1975, 500] # CONTOH KOORDINAT TARGET

koordinat_attack_zone = [[1975, 900],
                         [1975, 700],
                         [1975, 500]]
smooth = 15

while True:
    if dribble == True:
        code = Fukuro_Dynamic(koordinat_sekarang, koordinat_attack_zone2, koordinat_omni, smooth)

    elif dribble == False:
        Fukuro_Dynamic(koordinat_sekarang, koordinat_bola, koordinat_omni, smooth)