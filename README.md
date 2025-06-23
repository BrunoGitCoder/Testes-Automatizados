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

Este relatório apresenta a execução de testes automatizados, utilizando a abordagem de **caixa preta**, aplicando testes **funcionais** e **não funcionais** em um sistema simulado. O foco está em validar funcionalidades do sistema e aspectos de usabilidade, integração e interface.

---

## 2. 📕 Justificativas

### Objetivo

Avaliar o comportamento do sistema em cenários simulados, empregando testes automatizados desenvolvidos com **Python** e **Pytest**, com foco em:

- Correção funcional  
- Integração entre componentes  
- Validação de interface com o usuário

### 🛠️ Ferramentas Utilizadas

- **Python**: Linguagem principal para automação de testes.  
- **Pytest**: Framework escolhido pela sua flexibilidade, clareza na sintaxe e suporte a fixtures.  
- **Selenium (presumido)**: Potencial ferramenta usada em `test_ui.py` para simular interações com a interface gráfica (apesar do código não estar explícito).

---

## 3. Testes Realizados ⚗

### 3.1 Testes Funcionais 🧪

📄 Arquivo: `test_funcional.py`

- `test_login_sucesso`: Verifica autenticação válida.  
- `test_login_falha`: Verifica falha de autenticação com dados inválidos.  
- `test_navegacao_menu`: Garante que o menu principal é acessível após login.

---

### 3.2 Testes Não Funcionais 🔐

#### a) Testes de Integração  
📄 Arquivo: `test_integracao.py`

- `test_login_e_dashboard`: Valida a comunicação entre autenticação e painel principal.  
- `test_entrada_dados`: Simula preenchimento de formulários e envia dados entre componentes.

#### b) Testes de Interface  
📄 Arquivo: `test_ui.py`

- `test_tela_login_exibida`: Verifica exibição correta da tela de login.  
- `test_elementos_visiveis`: Garante visibilidade de campos e botões essenciais.  
- `test_botao_submit_funciona`: Testa funcionalidade do botão de submissão.

---

## 4. Resultados Obtidos 📈

| Tipo de Teste           | Nome do Teste                | Resultado Esperado                     | Status |
|-------------------------|------------------------------|----------------------------------------|--------|
| Funcional               | Login com sucesso            | Usuário redirecionado ao dashboard     | ✔️     |
| Funcional               | Login com falha              | Mensagem de erro exibida               | ✔️     |
| Funcional               | Navegação após login         | Menu principal acessível               | ✔️     |
| Integração              | Login + Dashboard            | Integração entre módulos OK            | ✔️     |
| Integração              | Envio de dados               | Formulário enviado corretamente        | ✔️     |
| Interface (UI)          | Tela de login                | Elementos visíveis                     | ✔️     |
| Interface (UI)          | Botão de login               | Clique processado com sucesso          | ✔️     |

---

## 5. Considerações Finais 🏁

Os testes executados comprovaram que o sistema se comporta conforme o esperado nas funcionalidades principais e em aspectos de integração e interface. A abordagem automatizada trouxe **eficiência**, **confiabilidade** e **consistência** nas verificações aplicadas.

Esse conjunto de testes serve como base sólida para garantir a qualidade do sistema em futuras atualizações ou manutenções.
