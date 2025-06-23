# 📃 Relatório de Testes - Projeto de Testes Automatizados

## 📚 Índice

- [1. Introdução](#1-introdução-)
- [2. Justificativas](#2-justificativas-)
- [3. Testes Realizados](#3-testes-realizados-)
  - [3.1 Testes Funcionais](#31-testes-funcionais-)
  - [3.2 Testes Não Funcionais](#32-testes-não-funcionais-)
- [4. Resultados Obtidos](#4-resultados-obtidos-)
- [5. Considerações Finais](#5-considerações-finais-)

---

## 1. Introdução 📘

Este relatório apresenta um conjunto de testes automatizados desenvolvidos em Python, aplicando as abordagens de **testes funcionais**, **integração** e **interface**. O foco é garantir a qualidade de um sistema web relacionado à gestão de filmes.

---

## 2. 📕 Justificativas

### Objetivo

Testar funcionalidades essenciais da aplicação com foco em:

- Acesso e autenticação de usuários  
- Pesquisa e manipulação de dados de filmes  
- Integração entre camadas da aplicação  
- Redirecionamentos de interface (UI)

### 🛠️ Ferramentas Utilizadas

- **Python**: Linguagem principal dos testes.  
- **Pytest**: Framework de testes escolhido pela sua simplicidade e organização.  
- **Bibliotecas auxiliares**: Utilização de `requests`, manipulação de dados JSON e suporte a fixtures via `conftest.py`.

---

## 3. Testes Realizados ⚗

### 3.1 Testes Funcionais 🧪

📄 Arquivo: `test_funcional.py`

- `test_login`: Verifica se o login funciona corretamente com credenciais válidas.  
- `test_search_movie`: Realiza busca por um filme específico e valida o resultado.  
- `test_show_admin_menu`: Garante que o menu administrativo aparece corretamente após login.

---

### 3.2 Testes Não Funcionais 🔐

#### a) Testes de Integração  
📄 Arquivo: `test_integracao.py`

- `test_movie_register`: Testa o processo de cadastro de um novo filme no sistema.  
- `test_movie_delete`: Verifica se a exclusão de um filme funciona corretamente.

#### b) Testes de Interface  
📄 Arquivo: `test_ui.py`

- `test_ui_redirect_buttons`: Confirma se os botões de interface redirecionam para as páginas corretas.

---

## 4. Resultados Obtidos 📈

| Tipo de Teste           | Nome do Teste               | Resultado Esperado                         | Status |
|-------------------------|-----------------------------|--------------------------------------------|--------|
| Funcional               | Login                       | Login com sucesso                          | ✔️     |
| Funcional               | Buscar Filme                | Filme retornado corretamente               | ✔️     |
| Funcional               | Menu Admin                  | Menu visível após autenticação             | ✔️     |
| Integração              | Cadastro de Filme           | Filme registrado com sucesso               | ✔️     |
| Integração              | Remoção de Filme            | Filme removido da base de dados            | ✔️     |
| Interface (UI)          | Botões de Redirecionamento  | Redirecionamento correto ao clicar         | ✔️     |

---

## 5. Considerações Finais 🏁

O projeto obteve sucesso na execução de todos os testes propostos, assegurando o correto funcionamento de funcionalidades principais, além da integração entre camadas e interações de interface.

Esses testes automatizados representam um avanço na qualidade do software, trazendo segurança e agilidade para futuras evoluções da aplicação.
