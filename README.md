# Esoteric Ebb — Tradução Português (BR)

Tradução **não oficial**, feita por fã, de Esoteric Ebb (Steam) para português do Brasil. Cobre os 12 arquivos de texto do jogo (diálogos, itens, magias, talentos, interface, glossário etc.): cerca de 82 mil linhas.

> Tradução feita com IA (Claude) e **revisada só por amostragem**. Vai ter frase estranha. Veja [Como ajudar](#como-ajudar).

*English: unofficial fan translation of Esoteric Ebb into Brazilian Portuguese, installed as a community language folder. See [AGENTS.md](AGENTS.md) for the machine-readable guide.*

## Instalar

Você precisa do jogo na Steam (versão com a pasta `Localization`).

### Opção 1 — script (Windows)

1. Baixe este repositório (**Code → Download ZIP**) e extraia.
2. No PowerShell, dentro da pasta extraída:

```powershell
.\tools\install.ps1
```

O script procura o jogo nas pastas comuns da Steam. Se não achar, informe o caminho:

```powershell
.\tools\install.ps1 -GamePath "C:\Program Files (x86)\Steam\steamapps\common\Esoteric Ebb"
```

### Opção 2 — manual

Copie a pasta `PortugueseBR` deste repositório para:

```
<pasta do jogo>\Esoteric Ebb_Data\StreamingAssets\Localization\
```

Ficando `...\Localization\PortugueseBR\Dialogs.csv` e os outros 11 arquivos.

### Ativar

Abra o jogo, vá em **Settings** e escolha **Português (BR)** no idioma. Atalhos do próprio jogo (descritos no guia do desenvolvedor): **V / B** trocam de idioma e **Ctrl+R** recarrega os CSVs com o jogo aberto.

Para desinstalar, apague a pasta `PortugueseBR`.

> Atualizações do jogo podem trocar a pasta `Official`, mas não mexem em pastas extras como esta. Se uma atualização adicionar chaves novas, rode o validador (abaixo) e abra uma issue.

## Como funciona (resumo)

O jogo carrega como idioma qualquer pasta nova dentro de `Localization` cujo nome não contenha "Template". Cada CSV precisa ter:

- as mesmas chaves, na mesma ordem, que `Official/`;
- o código do idioma na última coluna do cabeçalho (aqui `PT`);
- em `MiscTexts.csv`: `LanguageDropdown` (nome no menu: `Português (BR)`) e `FallbackLanguage` (aqui `EN`: linha vazia mostra o inglês).

Detalhes e armadilhas (tags `<i>`, `{0}`, `$VAR`, `\n`) estão em [AGENTS.md](AGENTS.md) e [docs/STYLE_GUIDE.md](docs/STYLE_GUIDE.md).

## Como ajudar

Achou erro? Edite o CSV correspondente em `PortugueseBR/` (a chave está na primeira coluna) e abra um Pull Request, ou abra uma issue com a **chave** e o texto sugerido. Antes de enviar, valide:

```bash
python tools/validate.py "<pasta do jogo>/Esoteric Ebb_Data/StreamingAssets/Localization"
```

O validador confere chaves, ordem e se tags e placeholders batem com o inglês. Termos fixos estão no [guia de estilo](docs/STYLE_GUIDE.md) (ex.: DC→CD, feat→talento, spell slot→espaço de magia).

## Limitações conhecidas

- Textos em outros idiomas, símbolos e linhas "corrompidas" propositais foram deixados como no original.
- Regras de reconhecimento de termos do `Glossary.csv` seguem em inglês; links do glossário podem não casar em todo trecho.
- Qualidade não revisada linha a linha.

## Aviso legal

Projeto de fã, sem vínculo com os criadores ou a editora de Esoteric Ebb. Os textos do jogo pertencem aos seus autores; este repositório contém apenas a tradução (sem o texto original em inglês) e deve ser usado por quem possui o jogo. Se os detentores dos direitos pedirem a remoção, será removido. Os scripts em `tools/` estão sob licença MIT ([LICENSE](LICENSE)).
