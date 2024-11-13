import os 

patch_urL_logs = "/opt/cgnat/HILLSTONE/W-005-INFORMAC/"
ip_antigo = "172.17.0.1"
ip_novo = "172.31.254.254"


input_ip_usuario = input('Informe qual servidor voce deseja: "antigo ou novo"')



def localizar_servidor (ip_fornecido_pelo_usuario):
    if (ip_fornecido_pelo_usuario == ip_novo):
        print ({ip_novo})
    else: 
        print({ip_antigo})    
    