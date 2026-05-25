# 🐟 AquaFeed - Monitoramento e Alertas para Piscicultura

Bem-vindo ao repositório do desafio da empresa **AquaFeed** da segunda fase do curso Futuro Digital (CEPEDI)! 

Equipe: Campus Aracaju

## 📖 Sobre o Projeto
O objetivo deste projeto é desenvolver o Minimum Viable Product (MVP) do AquaFeed, um sistema web voltado para o monitoramento de dados essenciais na piscicultura. A ferramenta foca na validação rápida do produto, entregando uma interface responsiva e intuitiva para centralizar dados e otimizar a tomada de decisão de produtores e técnicos. A solução engloba o desenvolvimento de ponta a ponta, contemplando tanto o Frontend quanto o Backend.

---

## 🔗 Links Úteis
* **Repositório GitHub:** [danielpaess/AquaFeed](https://github.com/danielpaess/AquaFeed)

---

## 📋 Tabela de Requisitos

* **Tabela de Requisitos Funcionais e Não Funcionais:**

<img width="541" height="710" alt="image" src="https://github.com/user-attachments/assets/556812a8-feb4-466c-9bd5-f43f217bd2ec" />

<img width="541" height="707" alt="image" src="https://github.com/user-attachments/assets/b45b9295-57c4-459c-83cb-2ee77e32933d" />


---

## 🏗️ Arquitetura e Modelagem

### Modelagem do Banco de Dados
A modelagem foi pensada com uma arquitetura preparada para o futuro, utilizando uma tabela genérica de parâmetros para facilitar a adição de novos sensores além de temperatura e oxigenação. 

<img width="2780" height="1007" alt="Model databases" src="https://github.com/user-attachments/assets/80660275-713a-4069-b6a1-ec68fcfd1c5a" />


---

## 📱 Telas do Projeto (Figma)

img


---

## 🚀 Progresso e Tarefas (Milestones)

O cronograma do projeto é dividido em entregas mensais ao longo de 3 meses. Acompanhe o progresso do desenvolvimento abaixo:

### 📍 Milestone 1: Base Forte e Design Focado no Campo (Prazo: 29 de Maio)
#### Link do Relatório (Maio): [Relatório - Maio]([https://docs.google.com/document/d/1c4bVccjR0S4GJxiqdbLch61k3NYVSsJv/edit?usp=sharing&ouid=102176604401866097318&rtpof=true&sd=true](https://docs.google.com/document/d/10s_PEez4O-1DkbrxrGxfOaqa2SShxeRh/edit?usp=sharing&ouid=102176604401866097318&rtpof=true&sd=true))
**Front-end:**
- [X] Definir identidade visual com foco estrito em mobile-first (botões grandes e acessíveis). 
- [X] Criar wireframes para cadastro de tanques e dashboard.  
- [X] Realizar setup do projeto e entregar layout estático inicial. 

**Back-end:**
- [X] Modelar o banco de dados (SQLite ou Postgres) com tabelas genéricas para parâmetros. 
- [X] Realizar setup do ambiente da API (Node/Express ou Python/FastAPI/Django).  
- [X] Criar endpoints de CRUD para os tanques.  
- [X] Implementar autenticação via JWT. 

### 📍 Milestone 2: Conectividade e Alertas Ativos (Prazo: 30 de Junho)
**Front-end:**
- [ ] Desenvolver dashboard dinâmico consumindo dados da API.  
- [ ] Implementar tabelas e gráficos (Chart.js ou Recharts).  
- [ ] Criar alertas visuais.  
- [ ] Iniciar configuração PWA (Service Worker) para cache.  
- [ ] Implementar lógica offline-first com Local Storage para sincronização de leituras.  

**Back-end:**
- [ ] Criar endpoint para registro de leituras (manual e simulador). 
- [ ] Implementar lógica de cálculo de status (OK, Atenção, Crítico) baseada em temperatura e oxigenação.  
- [ ] Integrar API do Telegram (Bot) ou E-mail (Resend/SendGrid) para alertas ativos.
- [ ] Configurar disparo automático de mensagens para níveis "Críticos" de oxigênio. 

### 📍 Milestone 3: Polimento e "Instalação" (Prazo: 03 de Agosto)
**Geral:**
- [ ] Realizar deploy da aplicação web completa em nuvem (Front e Back).  

**Front-end:**
- [ ] Finalizar configuração do PWA (manifest.json, ícones).  
- [ ] Habilitar função "Adicionar à Tela Inicial" para uso nativo.  
- [ ] Conduzir testes finais de usabilidade.  

**Back-end:**
- [ ] Executar testes de estresse para recebimento de dados sincronizados em massa pós-conexão offline.  
- [ ] Realizar testes de rotas principais e validação de segurança da API. 
