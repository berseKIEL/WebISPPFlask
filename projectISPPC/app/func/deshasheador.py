# $56e79bf43033d3b988b0a301e860bb536cb764ad45bdcd144d8b38b2a4fd6fb6
from werkzeug.security import check_password_hash, generate_password_hash

def revisar_contraseña_hasheada(hash, contraseña):
    return check_password_hash(hash, contraseña)

def generar_contraseña_hasheada(contraseña):
    return generate_password_hash(contraseña)


print(revisar_contraseña_hasheada('pbkdf2:sha256:260000$7nuSoC1LphzSg5y4$821c70cd7592df53cd226f91753028c199ad79c762daf64e4802043fce00f546','pepito123'))