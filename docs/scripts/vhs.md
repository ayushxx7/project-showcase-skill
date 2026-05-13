# CLI Recording (VHS)

Terminal demo GIFs using [VHS](https://github.com/charmbracelet/vhs) from Charmbracelet.

## How It Works

1. **Tape file** — Define commands in a `.tape` file
2. **VHS execution** — VHS spawns a virtual terminal, "types" commands, records output
3. **GIF output** — High-quality GIF sized for GitHub READMEs

## Template

See `scripts/record_cli.tape` for a working template:

```vhs
Output showcase/cli_demo.gif
Set FontSize 22
Set Width 1200
Set Height 600

Type "pip install my-tool" Enter
Sleep 1s
Type "my-tool --help" Enter
Sleep 2s
```

## Usage

```bash
vhs scripts/record_cli.tape
```

## Best Practices

- **Sleep intervals**: Give viewers time to read output (1-2s between commands)
- **Font size**: 22+ for mobile readability
- **Dimensions**: 1200x600 fits READMEs well
- **Keep it short**: 5-10 seconds max. Trim loading with `Sleep`.
