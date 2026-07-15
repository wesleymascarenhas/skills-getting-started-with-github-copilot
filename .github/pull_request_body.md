# Add extracurricular activities API and participant unregistration feature

## 📋 Resumo da PR

Esta PR implementa dois novos recursos principais:
1. **API de Atividades Extracurriculares** - Adiciona suporte para gerenciar atividades extracurriculares com validação de inscrição
2. **Funcionalidade de Desinscrição de Participantes** - Permite que participantes se desinscrevano de atividades

## 📝 Detalhes dos Commits

### 1️⃣ Add extracurricular activities and signup validation to API
- **Data**: 14 de julho de 2026, 00:53:39 UTC
- **Autor**: Wesley Mascarenhas
- **Mudanças principais**:
  - Adicionada API para gerenciar atividades extracurriculares
  - Implementada validação de inscrição para novos participantes
  - Criação de novos endpoints e modelos de dados para suportar essa funcionalidade

### 2️⃣ Implement participant unregistration feature and add tests
- **Data**: 14 de julho de 2026, 01:27:15 UTC
- **Autor**: Wesley Mascarenhas
- **Mudanças principais**:
  - Implementação completa da funcionalidade de desinscrição de participantes
  - Adicionados testes unitários para cobrir os casos de uso da desinscrição
  - Garantia de integridade dos dados ao remover participantes

### 3️⃣ Refactor tests for participant unregistration to improve readability and maintainability
- **Data**: 14 de julho de 2026, 02:06:31 UTC
- **Autor**: Wesley Mascarenhas
- **Mudanças principais**:
  - Refatoração dos testes de desinscrição para melhor legibilidade
  - Melhorias na manutenibilidade do código de testes
  - Reorganização da estrutura dos testes para seguir melhores práticas

## 📊 Estatísticas

- **Total de commits**: 3
- **Arquivos alterados**: 5
- **Linhas adicionadas**: 211
- **Linhas removidas**: 2
- **Estado**: Aberto
- **Ramo base**: `main`
- **Ramo de desenvolvimento**: `accelerate-with-copilot`

## ✅ Status

- ✅ Mergeable - A PR pode ser feita merge sem conflitos
- ✅ Sem comentários de revisão
- ✅ Sem revisores atribuídos
- ✅ Sem problemas de CI/CD relatados

## 🎯 Objetivo

Esta PR amplia a funcionalidade do sistema adicionando suporte completo para gerenciamento de atividades extracurriculares com a capacidade de participantes se desinscreverem quando necessário.
