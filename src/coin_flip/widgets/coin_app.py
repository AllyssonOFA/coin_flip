from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from .coin import Coin

CSS_FILE_PATH = "../style/coin_flip.tcss"

class CoinFlipApp(App):
    """A coin flipping app"""

    CSS_PATH = CSS_FILE_PATH

    BINDINGS = [
        ("space", "flip_coin", "Flip The Coin"),
        ("d", "toggle_dark", "Toggle Dark Mode")
    ]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Coin()
        yield Footer(show_command_palette=False)
    
    def on_mount(self) -> None:
        self.title = "Flip the Coin"
        self.sub_title = "A overengineered app to flip a coin"
    
    def action_toggle_dark(self) -> None:
        return super().action_toggle_dark()

    async def action_flip_coin(self) -> None:
        await self.query_one(Coin).flip_coin()