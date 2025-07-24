from utils.db import conectar

class UsuarioModel:
    @staticmethod
    def autenticar(email, senha):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
        cursor.execute(query, (email, senha))
        usuario = cursor.fetchone()
        conn.close()
        return usuario