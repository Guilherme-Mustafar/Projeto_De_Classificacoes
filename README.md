# Projeto de Governança e Qualidade de Dados Operacionais

## Visão Geral

Este projeto foi desenvolvido com o objetivo de solucionar um problema recorrente identificado na operação de atendimento de uma empresa de telecomunicações: a baixa qualidade dos dados gerados durante o registro dos atendimentos.

A ausência de critérios padronizados para classificação dos chamados resultava em informações inconsistentes, dificultando análises operacionais, identificação de tendências, geração de indicadores confiáveis e suporte à tomada de decisão.

O projeto foi estruturado utilizando Python e técnicas de Governança de Dados para identificar inconsistências, padronizar classificações e criar um modelo hierárquico de categorização dos atendimentos.

---

# O Problema

Durante a análise inicial da base histórica de atendimentos, foi identificado que grande parte dos registros possuía classificações genéricas ou incorretas.

Exemplos encontrados:

| Classificação Registrada |
| ------------------------ |
| Atendimento em Geral     |
| Atendimento              |
| Suporte                  |
| Outros                   |
| Financeiro               |

Essas classificações apresentavam dois problemas principais:

### 1. Falta de detalhamento

Não era possível compreender o motivo real do contato do cliente.

Exemplo:

"Financeiro"

Essa classificação poderia representar:

* Solicitação de segunda via;
* Negociação de débito;
* Bloqueio por inadimplência;
* Dúvida sobre cobrança.

Todas situações diferentes sendo registradas da mesma forma.

---

### 2. Inconsistência entre atendentes

Atendentes diferentes classificavam situações semelhantes de formas distintas.

Exemplo:

| Cenário              |
| -------------------- |
| Atendimento em Geral |
| Suporte              |
| Sem Internet         |
| Problema Técnico     |

Todos representando o mesmo tipo de ocorrência.

Como consequência:

* Relatórios apresentavam informações distorcidas;
* Indicadores operacionais perdiam confiabilidade;
* Tendências não podiam ser identificadas corretamente;
* Decisões estratégicas eram tomadas com base em dados inconsistentes.

---

# Diagnóstico da Base

A etapa inicial do projeto consistiu na análise exploratória dos registros históricos.

Foram avaliados:

* Frequência das classificações;
* Duplicidade de categorias;
* Termos genéricos;
* Ausência de padronização;
* Distribuição dos atendimentos.

A análise revelou uma elevada concentração de registros classificados como "Atendimento em Geral", impossibilitando a identificação dos reais motivos de contato dos clientes.

---

# Solução Proposta

Foi desenvolvido um modelo hierárquico de classificação baseado em três níveis de detalhamento.

## 1ª Camada — Contato

Representa o motivo informado inicialmente pelo cliente.

Exemplos:

* Sem Conexão
* Internet Lenta
* Pagamento
* Instalação
* Mudança de Endereço
* Upgrade de Plano

---

## 2ª Camada — Diagnóstico

Representa a causa identificada durante a análise do atendimento.

Exemplos:

* Rompimento de Fibra
* Problema no Roteador
* Inadimplência Prolongada
* Suspensão por Débito
* Equipamento Obsoleto
* Atenuação Elevada

---

## 3ª Camada — Solução

Representa a ação executada para resolução do problema.

Exemplos:

* Fibra Reparada
* Troca de Roteador
* Cliente Liberado
* Upgrade Efetivado
* Roteador Reiniciado
* Vencimento Reprogramado

---

# Fluxo da Solução

Cliente entra em contato

↓

Motivo do contato registrado

↓

Diagnóstico realizado

↓

Solução aplicada

↓

Registro estruturado para análise

---

# Arquitetura do Projeto

```text
Projeto_Classificacao/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── extracao.py
├── limpeza.py
├── main.py
│
├── DadosTratados1-Atendimento.csv
│
└── README.md
```

---

# Etapas do Pipeline

## Extração

Responsável por localizar automaticamente o arquivo mais recente disponibilizado para processamento.

Principais atividades:

* Identificação automática do arquivo;
* Leitura da base bruta;
* Carregamento para DataFrame.

---

## Limpeza

Responsável pela preparação dos dados.

Principais atividades:

* Padronização de nomes de colunas;
* Conversão de datas;
* Conversão de tempo de atendimento;
* Tratamento de valores ausentes;
* Normalização de classificações.

---

## Classificação de Outliers

Identificação de atendimentos com duração acima do limite esperado.

Regra utilizada:

```python
tempo_atendimento_min > 720
```

Atendimentos superiores a 12 horas são sinalizados para análise posterior.

---

# Benefícios Obtidos

Após a implementação do modelo:

* Padronização dos registros operacionais;
* Melhoria da qualidade dos dados;
* Maior confiabilidade dos indicadores;
* Facilidade para geração de dashboards;
* Identificação dos principais motivos de contato;
* Base estruturada para análises futuras.

---

# Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* CSV
* Git
* GitHub

---

# Conceitos Aplicados

* Data Quality
* Data Governance
* ETL
* Data Cleaning
* Data Profiling
* Padronização de Dados
* Análise Exploratória
* Governança de Dados Operacionais

---

# Próximos Passos

* Construção de dashboards analíticos;
* Criação de indicadores operacionais;
* Monitoramento contínuo da qualidade dos dados;
* Automação da classificação de atendimentos;
* Aplicação de Machine Learning para sugestão automática de categorias.

---

# Autor

Guilherme Mustafar

Analista de Dados com atuação em Business Intelligence, Governança de Dados, Automação de Processos e Desenvolvimento de Soluções Analíticas utilizando Python, SQL e Power BI.
