# DevSecOps Pipeline com CodeQL e GitHub Actions

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de implementar uma pipeline DevSecOps utilizando GitHub Actions e CodeQL para análise estática de segurança em aplicações Python.

A pipeline automatiza etapas importantes do ciclo de desenvolvimento, incluindo:

* análise de vulnerabilidades;
* testes automatizados;
* validação de qualidade de código;
* controle de deploy por ambiente;
* proteção de branches.

A proposta do projeto é simular um fluxo próximo ao utilizado em ambientes corporativos, aplicando conceitos de CI/CD, AppSec e automação de segurança.

---

# Tecnologias Utilizadas

| Tecnologia      | Finalidade                           |
| --------------- | ------------------------------------ |
| Python          | Desenvolvimento da aplicação         |
| GitHub Actions  | Pipeline CI/CD                       |
| CodeQL          | Análise estática de segurança (SAST) |
| Pytest          | Testes automatizados                 |
| Flake8          | Padronização e linting               |
| GitHub Security | Exibição de alertas de segurança     |
| Git             | Controle de versão                   |

---

# Estrutura do Projeto

```text id="vjlwmr"
codeql-lab/
│
├── main.py
│
├── vulnerable/
│   ├── sql_injection.py
│   ├── path_transversal.py
│   └── harded_code_secret.py
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── requirements.txt
│
└── .github/
    └── workflows/
        └── codeql.yml
```

---

# Funcionamento da Pipeline

A pipeline foi construída utilizando GitHub Actions e possui múltiplas etapas automatizadas.

Fluxo de execução:

```text id="5jlwm5"
Push / Pull Request
        ↓
GitHub Actions
        ↓
CodeQL Analysis
        ↓
Pytest + Flake8
        ↓
Deploy Stage
```

O deploy somente é executado caso todas as etapas anteriores sejam concluídas com sucesso.

---

# Análise Estática com CodeQL

O projeto utiliza CodeQL para realizar análise estática de segurança automaticamente a cada push ou pull request.

As vulnerabilidades identificadas ficam disponíveis em:

```text id="jlwm8q"
Security → Code scanning alerts
```

Durante os testes realizados no projeto, o CodeQL identificou vulnerabilidades como:

* SQL Injection;
* Path Traversal.

---

# Vulnerabilidades Simuladas

Os arquivos vulneráveis foram criados intencionalmente para fins acadêmicos e demonstração da análise automatizada.

## SQL Injection

Arquivo:

```text id="6jlwmr"
vulnerable/sql_injection.py
```

Exemplo de construção insegura de query SQL utilizando entrada controlada pelo usuário.

---

## Path Traversal

Arquivo:

```text id="pjlwm2"
vulnerable/path_transversal.py
```

Exemplo de leitura insegura de arquivos utilizando parâmetros enviados pelo usuário.

---

## Hardcoded Secret

Arquivo:

```text id="vjlwm0"
vulnerable/harded_code_secret.py
```

Exemplo de credenciais expostas diretamente no código-fonte.

---

# Testes Automatizados

O projeto utiliza Pytest para execução de testes automatizados durante a pipeline.

Os testes validam:

* funcionamento básico da aplicação;
* retorno esperado das funções;
* integridade do código executado na pipeline.

---

# Qualidade de Código

A validação de qualidade é realizada utilizando Flake8.

O linting garante:

* conformidade com PEP8;
* organização do código;
* padronização;
* redução de problemas de formatação.

---

# Proteção de Branches

O repositório utiliza regras de proteção de branch para garantir maior controle no fluxo de desenvolvimento.

Configurações aplicadas:

* Pull Request obrigatório;
* aprovação antes do merge;
* execução obrigatória da pipeline;
* bloqueio de merge em caso de falha.

---

# Ambiente Stage

Foi configurado um ambiente Stage utilizando GitHub Environments para simular um fluxo controlado de deploy.

O deploy só é executado quando:

* testes automatizados passam;
* linting é aprovado;
* pipeline executa sem falhas.

---

# Execução Local

## Clonar o repositório

```bash id="jlwm5t"
git clone https://github.com/ruansaure17/codeql-lab.git
```

---

## Instalar dependências

```bash id="3jlwm7"
pip install -r requirements.txt
```

---

## Executar testes

```bash id="0jlwmz"
python -m pytest tests/test_main.py -v
```

---

## Executar linting

```bash id="hjlwm9"
flake8 . --max-line-length=120 --exclude=venv
```

---

# Conceitos Aplicados

* DevSecOps
* CI/CD
* SAST
* Secure SDLC
* Shift Left Security
* Automação de Segurança
* GitHub Actions
* Branch Protection
* Pipeline Automation

---

# Considerações Finais

O projeto demonstra a integração de práticas de segurança diretamente no ciclo de desenvolvimento, utilizando automação para identificar vulnerabilidades e validar a qualidade do código antes do processo de deploy.

A proposta busca aproximar o ambiente acadêmico de cenários reais encontrados em equipes de desenvolvimento e segurança de aplicações.
