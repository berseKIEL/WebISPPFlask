INSERT INTO Usuario (Usuario) VALUES (42698355);
INSERT INTO UsuarioPerfil (UsuarioID, PerfilID) VALUES ((SELECT UsuarioID from Usuario where usuario = 42698355), 5);

INSERT INTO Usuario (Usuario) VALUES (424242424);
INSERT INTO UsuarioPerfil (UsuarioID, PerfilID) VALUES ((SELECT UsuarioID from Usuario where usuario = 424242424), 5);