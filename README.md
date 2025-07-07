# Biblioteca-POO
Projeto em Python que simula o funcionamento de um sistema de biblioteca, com foco em programação orientada a objetos. Desenvolvido com:
 - Classes de modelo para Livro, Usuário (Aluno/Professor), Biblioteca
 - Regras de negócio (empréstimos, limites por tipo de usuário)
 - Persistência de dados com JSON
 - Interface simplificada em terminal

Funcionalidades:
 - Seleção de biblioteca antes de iniciar as operações
 - Login com distinção entre Professor e Aluno
 - Busca de livros por ISBN ou por gênero
 - Empréstimo de livros com verificação de disponibilidade
 - Limites de empréstimo: 1 para aluno, 5 para professor
 - Consulta de situação (livros alugados + limite restante)
 - Loop interativo até o usuário escolher sair

Regras de negócio:
 - Alunos têm limite de 1 livro alugado por vez.
 - Professores têm limite de 5 livros alugados por vez.
 - Um livro só pode ser alugado se houver exemplares disponíveis.
 - A interface permanece ativa até o usuário optar por sair.

