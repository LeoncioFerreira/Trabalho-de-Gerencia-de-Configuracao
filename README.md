# Trabalho-de-Gerencia-de-Configuracao
# GitFlow

### Tema 6 — Gerenciador de Cursos e Alunos

##  Autores

| Nome                         | GitHub                                                |
| ---------------------------- | ------------------------------------------------------|
| Carlos Santos                | [@carlossan25c](https://github.com/davidvital-dev)    |
| David Josué                  | [@davidvital-dev](https://github.com/davidvital-dev)  |
| José Luiz De Lima            | [@J-Luiz-L](https://github.com/J-Luiz-L)              |
| Leôncio Ferreira Flores Neto | [@LeoncioFerreira](https://github.com/LeoncioFerreira)|
| Jetro Kepler                 | [@jetrokepler](https://github.com/jetrokepler)        |
| Paulo Gabriel                | [@LandimPG](https://github.com/LandimPG)              |

**Disciplina:** Gerência de Configuração  
**Professor:** Dr. Rafael Will  
**Instituição:** UFCA - Universidade Federal do Cariri  
**Campus:** Juazeiro do Norte - Centro de Ciências e Tecnologia  
**Curso:** Bacharelado em Engenharia de Software

## O que é GitFlow?

O GitFlow é um modelo de organização de branches no Git criado por Vincent Driessen com o objetivo de padronizar e organizar o fluxo de desenvolvimento de software. Esse modelo define diferentes tipos de branches para separar funcionalidades, correções e versões do projeto.

O GitFlow é muito utilizado em projetos maiores e equipes que trabalham com ciclos de release bem definidos, pois ajuda a manter o código organizado e estável.

---

# Estrutura de Branches

O GitFlow utiliza principalmente cinco tipos de branches:

| Branch      | Função                                         |
| ----------- | ---------------------------------------------- |
| `main`      | Contém a versão estável e pronta para produção |
| `develop`   | Branch principal de desenvolvimento            |
| `feature/*` | Desenvolvimento de novas funcionalidades       |
| `release/*` | Preparação de novas versões                    |
| `hotfix/*`  | Correções urgentes em produção                 |

---

# Funcionamento do GitFlow

## Branch `main`

A branch `main` armazena apenas versões estáveis do sistema.
Tudo que estiver nela deve estar pronto para produção.

Exemplo:

```bash
git checkout main
```

---

## Branch `develop`

A branch `develop` funciona como a branch principal de desenvolvimento, onde as funcionalidades são integradas antes de chegarem à `main`.

Exemplo:

```bash
git checkout -b develop
```

---

## Feature Branches

As funcionalidades são criadas a partir da branch `develop`.

Exemplo:

```bash
git checkout develop
git checkout -b feature/login
```

Após finalizar a funcionalidade:

```bash
git checkout develop
git merge feature/login
```

Depois disso, a branch pode ser removida:

```bash
git branch -d feature/login
```

---

## Release Branches

Quando o projeto está próximo de uma nova versão, cria-se uma branch de release.

Exemplo:

```bash
git checkout develop
git checkout -b release/1.0.0
```

Ela serve para:

* ajustes finais
* correção de bugs
* preparação da documentação
* testes finais

Após finalizar:

```bash
git checkout main
git merge release/1.0.0

git checkout develop
git merge release/1.0.0
```

---

## Hotfix Branches

As hotfixes são utilizadas para corrigir erros críticos diretamente em produção.

Exemplo:

```bash
git checkout main
git checkout -b hotfix/corrige-login
```

Após corrigir:

```bash
git checkout main
git merge hotfix/corrige-login

git checkout develop
git merge hotfix/corrige-login
```

---

# Exemplo de Fluxo

```text
main
 ├── hotfix/*
 └── develop
       ├── feature/*
       └── release/*
```

---

# Como subir uma branch

Criando uma branch:

```bash
git checkout -b feature/cadastro
```

Enviando a branch para o GitHub:

```bash
git push -u origin feature/cadastro
```

---

# Vantagens do GitFlow

* Organização do desenvolvimento
* Separação clara entre funcionalidades e produção
* Melhor controle de versões
* Facilita o trabalho em equipe
* Permite correções rápidas em produção

---

# Desvantagens do GitFlow

* Pode ser complexo para projetos pequenos
* Cria muitas branches
* Pode gerar conflitos em projetos muito dinâmicos

---

# Conclusão

O GitFlow é um modelo de organização de branches que ajuda equipes a manterem o desenvolvimento mais seguro, organizado e previsível. Ele separa claramente o desenvolvimento de funcionalidades, preparação de versões e correções emergenciais, tornando-se bastante útil em projetos maiores e com múltiplas releases.

---

# Referências

* GitFlow Workflow (Atlassian): https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

* The Gitflow Workflow: https://git-flow.sh/workflows/gitflow/

* Gitflow Workflow (Nulab): https://nulab.com/learn/software-development/git-tutorial/git-collaboration/branching-workflows/example-git-branching-workflow/

* Slides Rafael Will-Phd: https://drive.google.com/file/d/1TzwbRzKKPkH1xRsyKvOPaBEW9m8x0qwD/view