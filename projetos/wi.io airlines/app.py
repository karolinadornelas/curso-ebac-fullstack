import qrcode

def gerar_qr(passagem_data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(str(passagem_data))
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save('passagem_qr.png')

dados_passagem = {
    'name': 'Nome do Passageiro',
    'aeroportoSaindo': 'Aeroporto de Partida',
    'aeroportoDestino': 'Aeroporto de Destino',
    'date': 'Data da Viagem',
    'time': 'Horário da Viagem'
}

gerar_qr(dados_passagem)
