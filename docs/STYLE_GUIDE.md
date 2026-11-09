# Guia de tradução EN -> pt-BR (Esoteric Ebb)

Jogo: RPG de diálogo estilo D&D 5e, humor ácido/absurdo, você é um clérigo arcano burro e forte; cidade de Norvik, eleição em 5 dias. Tom coloquial brasileiro, vivo, com o mesmo humor; use "você" (não "tu").

## Formato
Entrada: `chunks/<Arquivo>_NNN.tsv`, colunas separadas por TAB: `chave [speaker] [tipo] texto`. O texto é sempre a ÚLTIMA coluna; `\n` literal = quebra de linha.
Saída: `tr/<Arquivo>_NNN.tsv` (mesmo número), com linhas `chave<TAB>tradução`, UMA linha por linha de entrada, mesma ordem, todas as chaves, sem cabeçalho, UTF-8. Mantenha `\n` literal. Nunca coloque TAB ou quebra de linha real dentro da tradução.

## Regras
- Preserve EXATAMENTE tags e códigos: `<i>`, `<b>`, `<color=...>`, `<size=..>`, `<link=...>`, `{0}`, `{CLERIC}`, `$VAR`, `[...]` técnicos, `|`, `%`, e qualquer coisa entre `{}` ou `<>`. Traduza só o texto visível (inclusive dentro de tags de link).
- Se a linha é só um código/nome próprio/número, copie igual.
- Speaker: códigos de atributo (str, dex, con, int, wis, cha, PC, OBJ...) indicam quem fala; "int" é a voz do atributo Inteligência etc. Tipo CHOICE = opção do jogador (fala/ação/pensamento); mantenha aspas e parênteses como no original.
- Mantenha a pontuação expressiva, caixa alta, reticências, estilo de cada voz.
- Não censure palavrões; use equivalentes naturais.

## Glossário fixo
DC → CD (Classe de Dificuldade); FC → FC; HP → PV (pontos de vida); XP → XP; d20 → d20; Chime(s) → Chime(s) (mantém); Dice Check → Teste de Dados; roll → rolar; saving throw → teste de resistência; long/short rest → descanso longo/curto; spell → magia; cantrip → truque; spell slot → espaço de magia; spellbook → grimório; scroll → pergaminho; shrine → santuário; cleric → clérigo; Arcane Cleric → Clérigo Arcano; feat → talento; Questing Tree → Árvore de Missões; quest → missão; ability score → atributo; Strength/Dexterity/Constitution/Intelligence/Wisdom/Charisma → Força/Destreza/Constituição/Inteligência/Sabedoria/Carisma; proficiency → proficiência; exhaustion → exaustão; Shard of Jor → Fragmento de Jor; Jor's Strings → Cordas de Jor; Esoteric Event/Pocket → Evento/Bolsão Esotérico; Journal → Diário; Inventory → Inventário; DM → Mestre; kobold → kobold; Norvik, Jor, Ebb, nomes de pessoas/lugares/deuses → não traduzir.
