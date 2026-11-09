# AGENTS.md — guide for AI agents

Repository: unofficial pt-BR localization of the Unity game **Esoteric Ebb**. Deliverable = folder `PortugueseBR/` (12 CSVs). Humans: see [README.md](README.md) (Portuguese).

## Task recipes

### Install for a user
Copy `PortugueseBR/*.csv` to `<game>/Esoteric Ebb_Data/StreamingAssets/Localization/PortugueseBR/`. Windows helper: `tools/install.ps1 [-GamePath <dir>]`. Do not touch `Official/` or `Template/`. No game code is patched. In game: Settings → language "Português (BR)"; Ctrl+R reloads CSVs at runtime; V/B switch language (per the developer's `Tools/_Localization_Guide.txt`).

### Fix or improve a translation
1. Find the row by key (column 1) in `PortugueseBR/<File>.csv`.
2. Edit only the **last column**. Never change keys, row order, or other columns.
3. Keep the style rules in `docs/STYLE_GUIDE.md` (fixed glossary, "você" not "tu", keep tone/humor, do not censor profanity).
4. Run `python tools/validate.py "<.../StreamingAssets/Localization>"` (needs the game's `Official/` folder). Must report `problemas: 0`.

### Add a new language (same method)
1. Copy `Localization/Template/` to a new folder (name must not contain "Template").
2. In every CSV set the header of the last column to a unique language code (not `EN`, `CH`, or other existing codes). All CSVs must use the same code or they are ignored.
3. In `MiscTexts.csv` fill `LanguageDropdown` (menu label) and `FallbackLanguage` (a code such as `EN`; empty cells show that language).
4. Fill the last column from `Official/*.csv` column `EN` (columns: `Key,Area,Speaker,Type,EN,CH`; some files have fewer metadata columns, so always address the text as the last column of the Template row and the `EN` column by header name).
5. Validate with `tools/validate.py` (adjust the language code assumptions if needed).

## Format rules (break the game or look broken if violated)

- CSV, UTF-8 without BOM, CRLF line endings, RFC-4180 quoting. Use a real CSV library; cells contain commas, quotes, and real newlines. Raise `csv.field_size_limit`.
- Same keys, same order as `Official/`. After a game update, re-sync from `Template/`.
- Preserve exactly, as in the English text: Unity rich-text tags (`<i> <b> <u> <color=...> <size=..> <link=...> <shake> <wiggle>`), placeholders (`{0}`, `{CLERIC}`), variables (`$VAR`), literal `\n` sequences, `|`, `%`, bracketed technical tokens. Translate only visible text, including text inside `<link>` tags.
- If the English line is only a code, proper name or number, copy it.
- Speaker column values (`str dex con int wis cha PC OBJ`...) tell who talks (attribute "voices" in the player's head); type `CHOICE` is a player option; keep quotes/parentheses style.
- Lines in other languages or deliberately glitched (zalgo) text are copied untouched.
- `Glossary.csv`: term titles are translated (used for clickable links); the `Glossary_GlobalMatchRule` / `AdditionalMatchRule_N` rows are left as original.
- English source may itself have unbalanced tags; `tools/tagrule.py:serious()` only flags a translation when it is *worse* than the source.

## Method used to produce this translation (reproducible)

Large-scale machine translation with chunking and mechanical validation:

1. Split the English text (Official `EN` column) into chunks of ~1000 lines, one `key<TAB>[speaker][type]<TAB>text` per line.
2. Translate each chunk with a model under `docs/STYLE_GUIDE.md`, output `key<TAB>translation`, same order, literal `\n`, no tabs/newlines inside a translation.
3. Validate each chunk: format, key order/coverage, `serious()` tag/placeholder check, no unchanged long lines. Re-queue only the failing/missing keys.
4. Pool valid lines by key (so partial output from interrupted runs is reused).
5. Build CSVs from `Template/`: fill last column, force `LanguageDropdown`/`FallbackLanguage`, write with `csv.writer(lineterminator='\r\n')`.
6. Consistency pass: grep term variants across the output and unify (e.g. "Freestriders", "Cidade Abaixo" for City Below).

Pitfalls seen: parallel agents sharing a temp file corrupt output (use per-agent files); heredoc-written scripts mangle backslashes (write files with an editor tool); on Windows run Python with `-X utf8` for console output.

## Do not

- Do not commit the English `Official/` or `Template/` contents or the game's other assets (copyright).
- Do not rename `PortugueseBR/` files or add columns.
- Do not "fix" the glossary match rules to Portuguese without testing in game.

## Layout

```
PortugueseBR/        the translation (12 CSVs)
tools/install.ps1    Windows installer
tools/validate.py    keys/order/tags check vs Official
tools/tagrule.py     tag & placeholder comparison used by validate.py
docs/STYLE_GUIDE.md  glossary and style rules (pt-BR, original working notes)
```
