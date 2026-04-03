# 🛒 Lista de Compras em Python
Um script simples e funcional em Python para gerenciamento de listas de compras via terminal. O projeto permite adicionar, remover e visualizar itens, com tratamento de erros e interface limpa.

## ✨ Funcionalidades
- Adicionar itens: Permite inserir novos itens na lista (converte automaticamente para minúsculas).
- Remover itens: Remoção feita diretamente pelo nome do produto.
- Evitar Duplicados: O sistema impede a adição de itens que já constam na lista.
- Visualização Limpa: Exibição da lista em formato de tópicos, sem índices numéricos.
- Multiplataforma: Comando para limpar o terminal funciona tanto em Windows quanto em sistemas Unix (Linux/macOS)

## 🛠️ Tecnologias Utilizadas
-Python 3
-Módulo `os`: Para interação com o sistema operacional (limpeza de tela).

## 🕹️ Como Usar
Para gerenciar sua lista, siga a numeração do menu:

1. **Adicionar:** Digite `1` e escreva o nome do produto.
2. **Remover:** Digite `2` e escreva o nome exato do item que deseja tirar.
3. **Listar:** Digite `3` para ver tudo o que você já adicionou.
4. **Sair:** Digite `4` para fechar o programa.

## 📝 Notas de Implementação
- O programa utiliza um loop while True para manter a interface ativa até que o usuário escolha sair.
- A função `limpar_tela()` detecta se o sistema é Windows `(nt)` ou Posix para garantir que a experiência visual seja consistente.

---
Desenvolvido por isacalves25